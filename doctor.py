"""Local inventory only: no installs, credential reads, network calls or repairs."""
import json
import platform
import shutil
import sys


def inventory():
    return {
        'mode': 'READ_ONLY_INVENTORY',
        'python_version': platform.python_version(),
        'os': platform.system(),
        'running_in_venv': sys.prefix != sys.base_prefix,
        'tools_on_path': {name: shutil.which(name) is not None
                          for name in ('git', 'docker', 'node', 'npm', 'code', 'wsl')},
        'limitations': [
            'Presence on PATH is not proof a tool works.',
            'Docker engine, WSL networking, Copilot authorization and Git authentication are NOT assessed.',
            'No environment variables, account names, paths or credentials are collected.'
        ]
    }


if __name__ == '__main__':
    print(json.dumps(inventory(), indent=2))
