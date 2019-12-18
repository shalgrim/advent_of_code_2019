import unittest
from unittest import TestCase
from day18_1 import calc_fewest_steps_to_all_keys, Map


MAP1_0 = [
    '#########',
    '#b.A.@.a#',
    '#########',
]

MAP2_2 = [
    '########################',
    '#f.D.E.e.C.@.........c.#',
    '######################.#',
    '#d.....................#',
    '########################',
]


class TestMap(TestCase):
    def setUp(self):
        self.map1_0 = Map(MAP1_0)
        self.map2_2 = Map(MAP2_2)
        self.maps2_2_reachables = set()
        for x in range(10, 23):
            self.maps2_2_reachables.add((x, 1))
        self.maps2_2_reachables.add((22, 2))
        for x in range(1, 23):
            self.maps2_2_reachables.add((x, 3))

    @unittest.skip('may not build')
    def test_can_reach(self):
        self.assertFalse(self.map1_0.can_reach((0, 0)))
        self.assertFalse(self.map1_0.can_reach((9, 2)))
        self.assertFalse(self.map1_0.can_reach((1, 1)))
        self.assertFalse(self.map1_0.can_reach((2, 1)))
        self.assertFalse(self.map1_0.can_reach((3, 1)))
        self.assertTrue(self.map1_0.can_reach((4, 1)))
        self.assertTrue(self.map1_0.can_reach((5, 1)))
        self.assertTrue(self.map1_0.can_reach((6, 1)))
        self.assertTrue(self.map1_0.can_reach((7, 1)))

    def test_reachable(self):
        self.assertEqual(self.map1_0.reachable(), set([(4, 1), (5, 1), (6, 1), (7, 1)]))
        maps2_2_reachables = set()
        for x in range(10, 23):
            maps2_2_reachables.add((x, 1))
        maps2_2_reachables.add((22, 2))
        for x in range(1, 23):
            maps2_2_reachables.add((x, 3))
        self.assertEqual(self.map2_2.reachable(), maps2_2_reachables)


@unittest.skip('later')
class TestDay18(TestCase):
    def test_calc_fewest_steps(self):
        self.assertEqual(
            calc_fewest_steps_to_all_keys(['#########', '#b.A.@.a#', '#########',]), 8
        )
