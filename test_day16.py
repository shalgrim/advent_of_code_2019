from unittest import TestCase
from day16_1 import main
from day16_2 import main as main2


class TestDay16(TestCase):
    def test_example_1(self):
        self.assertEqual(main('12345678', 1, 8), '48226158')
        self.assertEqual(main('12345678', 2, 8), '34040438')
        self.assertEqual(main('12345678', 3, 8), '03415518')
        self.assertEqual(main('12345678', 4, 8), '01029498')

    def test_examples_2_to_4(self):
        self.assertEqual(main('80871224585914546619083218645595', 100, 8), '24176176')
        self.assertEqual(main('19617804207202209144916044189917', 100, 8), '73745418')
        self.assertEqual(main('69317163492948606335995924319873', 100, 8), '52432133')

    def test_part_2(self):
        self.assertEqual(main2('03036732577212944063491565474664', 100, 8), '84462026')
        # self.assertEqual(main2('02935109699940807407585447034323', 100, 8), '78725270')
        # self.assertEqual(main2('03081770884921959731165446850517', 100, 8), '53553731')
