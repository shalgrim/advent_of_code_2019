from unittest import TestCase
from day20_1 import Map


class TestDay20(TestCase):
    def setUp(self) -> None:
        with open('data/test20_1.txt') as f:
            lines = [line.rstrip() for line in f.readlines()]
        self.map1 = Map(lines)

    def test_find_start(self):
        self.assertEqual(self.map1.start, (9, 2))

    def test_find_end(self):
        self.assertEqual(self.map1.end, (13, 16))

    def test_find_portals(self):
        self.assertEqual(len(self.map1.portals), 5)
        self.assertEqual(len(self.map1.portals['AA']), 1)
        self.assertEqual(len(self.map1.portals['ZZ']), 1)
        self.assertCountEqual(self.map1.portals['BC'], [(2, 8), (9, 6)])
        self.assertCountEqual(self.map1.portals['DE'], [(6, 10), (2, 13)])
        self.assertCountEqual(self.map1.portals['FG'], [(2, 15), (11, 12)])
