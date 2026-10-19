import unittest
from unittest.mock import patch
from doctor import inventory
from lab import run_lab


class RepairTests(unittest.TestCase):
    def test_missing_tools_are_not_success(self):
        with patch('doctor.shutil.which', return_value=None):
            result = inventory()
        self.assertFalse(any(result['tools_on_path'].values()))
        self.assertEqual(result['mode'], 'READ_ONLY_INVENTORY')

    def test_inventory_does_not_include_sensitive_fields(self):
        result = inventory()
        self.assertEqual(set(result), {'mode', 'python_version', 'os',
                         'running_in_venv', 'tools_on_path', 'limitations'})

    def test_wrong_interpreter_lab(self):
        result = run_lab()
        self.assertTrue(result['passed'])
        self.assertFalse(result['system_settings_changed'])
        self.assertFalse(result['network_used'])


if __name__ == '__main__':
    unittest.main()
