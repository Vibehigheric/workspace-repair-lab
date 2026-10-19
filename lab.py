"""Synthetic wrong-interpreter demo. Creates only a temporary isolated venv."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import uuid
import venv


def run_lab():
    with tempfile.TemporaryDirectory(prefix='workspace-repair-demo-') as directory:
        root = Path(directory)
        env = root / 'demo-env'
        venv.EnvBuilder(with_pip=False).create(env)
        python = env / ('Scripts/python.exe' if sys.platform == 'win32' else 'bin/python')
        site = subprocess.run(
            [str(python), '-I', '-c', 'import sysconfig; print(sysconfig.get_path("purelib"))'],
            check=True, capture_output=True, text=True, timeout=30).stdout.strip()
        module = 'repair_fixture_' + uuid.uuid4().hex
        Path(site, module + '.py').write_text('VALUE = 42\n', encoding='utf-8')
        command = f'import {module}; assert {module}.VALUE == 42; print("PASS")'
        before = subprocess.run([sys.executable, '-I', '-c', command], cwd=root,
                                capture_output=True, text=True, timeout=30)
        after = subprocess.run([str(python), '-I', '-c', command], cwd=root,
                               capture_output=True, text=True, timeout=30)
        passed = (before.returncode != 0 and 'ModuleNotFoundError' in before.stderr
                  and after.returncode == 0 and after.stdout.strip() == 'PASS')
        return {'scenario': 'SYNTHETIC_WRONG_INTERPRETER', 'passed': passed,
                'before': 'IMPORT_FAILED' if before.returncode else 'UNEXPECTED_SUCCESS',
                'after': 'IMPORT_PASSED' if after.returncode == 0 else 'IMPORT_FAILED',
                'repair': 'Run the same code using the interpreter that owns the dependency.',
                'scope': 'Independent lab only; no client machine or VS Code GUI repair claimed.',
                'system_settings_changed': False, 'network_used': False}


if __name__ == '__main__':
    result = run_lab()
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['passed'] else 1)
