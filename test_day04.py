from unittest import TestCase

from day04_1 import LO, HI
from day04_1 import is_valid_pw, count_valid_pws


class TestDay04(TestCase):
    def test_is_valid_pw(self):
        self.assertTrue(is_valid_pw(111111, True))
        self.assertFalse(is_valid_pw(223450, True))
        self.assertFalse(is_valid_pw(123789, True))

    def test_count_valid_pws(self):
        self.assertEqual(count_valid_pws(LO, HI), 2220)
        self.assertEqual(count_valid_pws(LO, HI, strict=True), 1515)

    def test_is_valid_pw_strict(self):
        self.assertFalse(is_valid_pw(111111, True, strict=True))
        self.assertFalse(is_valid_pw(223450, True, strict=True))
        self.assertFalse(is_valid_pw(123789, True, strict=True))
        self.assertTrue(is_valid_pw(112233, True, strict=True))
        self.assertFalse(is_valid_pw(123444, True, strict=True))
        self.assertTrue(is_valid_pw(111122, True, strict=True))
