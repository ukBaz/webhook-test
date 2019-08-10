import unittest


class Test101(unittest.TestCase):
    def test_always_pass(self):
        self.assertTrue(True)

    def test_always_fail(self):
        self.assertTrue(False)