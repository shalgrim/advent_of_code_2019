from unittest import TestCase

from day04_1 import is_valid_pw


class TestDay04(TestCase):
    def test_is_valid_pw(self):
        self.assertTrue(is_valid_pw(111111, True))
        self.assertFalse(is_valid_pw(223450, True))
        self.assertFalse(is_valid_pw(123789, True))
