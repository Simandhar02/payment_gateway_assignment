import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
from app import create_test_app


class TestFactory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestFactory, cls).setUpClass()
        cls.app = create_test_app()
        cls.request_params = dict()

    @classmethod
    def tearDownClass(cls):
        super(TestFactory, cls).tearDownClass()
