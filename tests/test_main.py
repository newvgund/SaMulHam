__author__ = 'JiNooNi'

import unittest

class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        self.assertEqual(10, 10)

    def test_fail(self):
        self.assertEqual(10, 0)