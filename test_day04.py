from unittest import TestCase

from day04_1 import LO, HI
from day04_1 import is_valid_pw, count_valid_pws
from day04_2 import is_valid_pw_stricter


class TestDay04(TestCase):
    def test_is_valid_pw(self):
        self.assertTrue(is_valid_pw(111111, True))
        self.assertFalse(is_valid_pw(223450, True))
        self.assertFalse(is_valid_pw(123789, True))

    def test_count_valid_pws(self):
        self.assertEqual(count_valid_pws(LO, HI), 2220)

    def test_is_valid_pw_stricter(self):
        self.assertFalse(is_valid_pw_stricter(111111, True))
        self.assertFalse(is_valid_pw_stricter(223450, True))
        self.assertFalse(is_valid_pw_stricter(123789, True))
        self.assertTrue(is_valid_pw_stricter(112233, True))
        self.assertFalse(is_valid_pw_stricter(123444, True))
        self.assertTrue(is_valid_pw_stricter(111122, True))
