import unittest
import os
import shutil

from datacoco_core.logger import Logger


class TestDefaultLogger(unittest.TestCase):

    log_dir = "logs"
    log_message = "This is a test"

    @classmethod
    def setUpClass(cls):
        cls.l = Logger()

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
        self.l.l(self.log_message)
        filename = os.listdir(self.log_dir)[0]
        open_file = open(self.log_dir + "/" + filename)
        contents = open_file.read()
        if self.log_message in contents:
            logged = True
        open_file.close()
        self.assertTrue(logged)


class TestCustomLognameLogger(unittest.TestCase):

    log_dir = "logs"
    logname_prefix = "custom_logs"
    log_message = "Testing log file creation."

    @classmethod
    def setUpClass(cls):
        cls.l = Logger(logname=cls.logname_prefix)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.log_dir)

    def test_log_file_creation(self):
        self.l.l(self.log_message)
        test_logger_file = False
        for f in os.listdir(self.log_dir):
            if self.logname_prefix in f:
                test_logger_file = True
        self.assertTrue(test_logger_file)
