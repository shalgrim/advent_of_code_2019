from unittest import TestCase
from day16_01 import main


class TestDay16(TestCase):
    def test_example_1(self):
        self.assertEqual(main(12345678, 1, 8), 48226158)
        self.assertEqual(main(12345678, 2, 8), 34040438)
        self.assertEqual(main(12345678, 3, 8), 3415518)
        self.assertEqual(main(12345678, 4, 8), 1029498)

    def test_examples_2_to_4(self):
        self.assertEqual(main(80871224585914546619083218645595, 100, 8), 24176176)
        self.assertEqual(main(19617804207202209144916044189917, 100, 8), 73745418)
        self.assertEqual(main(69317163492948606335995924319873, 100, 8), 52432133)
