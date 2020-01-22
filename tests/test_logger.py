import unittest
import os
import shutil

from datacoco_core.logger import Logger


class TestDefaultLogger(unittest.TestCase):

    log_dir = "logs"
    log_msg = "This is a test"

    @classmethod
    def setUpClass(cls):
        cls.logger = Logger()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.log_dir)

    def test_log_file_creation(self):
        test_logger_file = False
        for f in os.listdir(self.log_dir):
            if "test_logger.py" in f:
                test_logger_file = True
        self.assertTrue(test_logger_file)

    def test_logging(self):
        logged = False
        self.logger.log_message(self.log_msg)
        filename = os.listdir(self.log_dir)[0]
        open_file = open(self.log_dir + "/" + filename)
        contents = open_file.read()
        if self.log_msg in contents:
            logged = True
        open_file.close()
        self.assertTrue(logged)


class TestCustomLognameLogger(unittest.TestCase):

    log_dir = "logs"
    logname_prefix = "custom_logs"
    log_msg = "Testing log file creation."

    @classmethod
    def setUpClass(cls):
        cls.logger = Logger(logname=cls.logname_prefix)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.log_dir)

    def test_log_file_creation(self):
        self.logger.log_message(self.log_msg)
        test_logger_file = False
        for f in os.listdir(self.log_dir):
            if self.logname_prefix in f:
                test_logger_file = True
        self.assertTrue(test_logger_file)
