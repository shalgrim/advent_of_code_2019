from unittest import TestCase
from day01_2 import calc_fuel


class TestDay01PartTwo(TestCase):
    def test_calc_fuel(self):
        self.assertEqual(calc_fuel(14), 2)
        self.assertEqual(calc_fuel(1969), 966)
        self.assertEqual(calc_fuel(100756), 50346)
