from unittest import TestCase
from day20_1 import Map


class TestDay20(TestCase):
    def setUp(self) -> None:
        with open('data/test20_1.txt') as f:
            lines = [line.rstrip() for line in f.readlines()]
        self.map1 = Map(lines)
        with open('data/test20_2.txt') as f:
            lines = [line.rstrip() for line in f.readlines()]
        self.map2 = Map(lines)
        with open('data/input20.txt') as f:
            lines = [line.rstrip() for line in f.readlines()]
        self.map3 = Map(lines)
        self.map1.calc_all_distances()
        self.map2.calc_all_distances()

    def test_find_start(self):
        self.assertEqual(self.map1.start, (9, 2))
        self.assertEqual(self.map2.start, (19, 2))
        self.assertEqual(self.map3.start, (61, 2))

    def test_find_end(self):
        self.assertEqual(self.map1.end, (13, 16))
        self.assertEqual(self.map2.end, (2, 17))
        self.assertEqual(self.map3.end, (71, 2))

    def test_find_portals(self):
        self.assertEqual(len(self.map1.portals), 5)
        self.assertEqual(len(self.map1.portals['AA']), 1)
        self.assertEqual(len(self.map1.portals['ZZ']), 1)
        self.assertCountEqual(self.map1.portals['BC'], [(2, 8), (9, 6)])
        self.assertCountEqual(self.map1.portals['DE'], [(6, 10), (2, 13)])
        self.assertCountEqual(self.map1.portals['FG'], [(2, 15), (11, 12)])
        self.assertEqual(len(self.map2.portals), 12)
        self.assertEqual(len(self.map2.portals['AA']), 1)
        self.assertEqual(len(self.map2.portals['ZZ']), 1)
        self.assertCountEqual(self.map2.portals['JO'], [(2, 19), (13, 28)])
        self.assertCountEqual(self.map2.portals['JP'], [(21, 28), (15, 34)])
        self.assertCountEqual(self.map2.portals['VT'], [(32, 11), (26, 23)])
        self.assertCountEqual(self.map2.portals['AS'], [(17, 8), (32, 17)])

    def test_calc_shortest_path(self):
        self.assertEqual(self.map1.distances[self.map1.end], 23)
        self.assertEqual(self.map2.distances[self.map2.end], 58)
