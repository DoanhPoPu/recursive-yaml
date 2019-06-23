import unittest
from pathlib import Path

import recursive_yaml


class MyTestCase(unittest.TestCase):
    def test_recursive_yaml(self):
        current_dir = Path(Path(__file__).parent)
        master_path = current_dir / 'master.yaml'

        result = recursive_yaml.load(config_path=master_path)
        self.assertEqual(result, [{
            'master': {
                'slave': "I'm Groot",
            },
        }, {
            'master2': {
                'slave': "I'm Groot",
            },
        }])


if __name__ == '__main__':
    unittest.main()
