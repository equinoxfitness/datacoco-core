import unittest

from datacoco_core.config import config
from datacoco_core.config import find_config_path


class TestConfig(unittest.TestCase):

    good_config_path = "tests/test_data/test.cfg"
    bad_config_path = "tests/test_data/bad_etl.cfg"

    config_name = "test.cfg"
    bad_config_name = "bad_test.cfg"
    config_path = "tests/test_data"

    expected_config = {
        "batchy": {
            "password": "thisIsAPassword",
            "server": "localhost",
            "port": "8050",
        }
    }

    def test_find_config_load_type(self):
        c = config(self.good_config_path)
        self.assertIs(type(c), dict)

    def test_config_bad_load(self):
        c = config(self.bad_config_path)
        self.assertEqual(len(c), 0)

    def test_load_config_results(self):
        c = config(self.good_config_path)
        self.assertEqual(self.expected_config, c)

    def test_find_config_path(self):
        c = find_config_path(self.config_name, self.config_path)
        self.assertIs(type(c), str)

    def test_bad_find_config_path(self):
        c = find_config_path(self.bad_config_name, self.config_path)
        self.assertEqual(c, None)
