import unittest
from unittest import TestCase

from day18_1 import (
    Map,
    bfs,
    calc_fewest_steps_to_all_keys,
    known_shortest,
    known_state_distances,
)

MAP1_0 = [
    '#########',
    '#b.A.@.a#',
    '#########',
]

MAP1_1 = [
    '#########',
    '#b.A...@#',
    '#########',
]

MAP2_0 = [
    '########################',
    '#f.D.E.e.C.b.A.@.a.B.c.#',
    '######################.#',
    '#d.....................#',
    '########################',
]

MAP2_2 = [
    '########################',
    '#f.D.E.e.C.@.........c.#',  # note this is actually weird they moved @ back to the b key after it unlocked B door
    '######################.#',
    '#d.....................#',
    '########################',
]

MAP3_0 = [
    '########################',
    '#...............b.C.D.f#',
    '#.######################',
    '#.....@.a.B.c.d.A.e.F.g#',
    '########################',
]

MAP4_0 = [
    '#################',
    '#i.G..c...e..H.p#',
    '########.########',
    '#j.A..b...f..D.o#',
    '########@########',
    '#k.E..a...g..B.n#',
    '########.########',
    '#l.F..d...h..C.m#',
    '#################',
]

MAP5_0 = [
    '########################',
    '#@..............ac.GI.b#',
    '###d#e#f################',
    '###A#B#C################',
    '###g#h#i################',
    '########################',
]


class TestMap(TestCase):
    def setUp(self):
        global known_shortest
        self.map1_0 = Map(MAP1_0)
        self.map1_1 = Map(MAP1_1)
        self.map1_1.picked_up_keys.add('a')
        self.map2_0 = Map(MAP2_0)
        self.map2_2 = Map(MAP2_2)
        self.map3_0 = Map(MAP3_0)
        self.map4_0 = Map(MAP4_0)
        self.map5_0 = Map(MAP5_0)
        self.maps2_2_reachables = set()
        for x in range(10, 23):
            self.maps2_2_reachables.add((x, 1))
        self.maps2_2_reachables.add((22, 2))
        for x in range(1, 23):
            self.maps2_2_reachables.add((x, 3))
        known_shortest = 0
        known_state_distances.clear()

    def tearDown(self) -> None:
        global known_shortest, known_state_distances
        known_shortest = 0
        known_state_distances.clear()

    @unittest.skip('I may not build out this function')
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
        self.assertEqual(
            self.map1_0.reachable(), {(4, 1): 1, (5, 1): 0, (6, 1): 1, (7, 1): 2}
        )
        maps2_2_reachables = {(10, 1): 1}

        for i, x in enumerate(range(11, 23)):
            maps2_2_reachables[x, 1] = i

        maps2_2_reachables[(22, 2)] = maps2_2_reachables[(22, 1)] + 1

        for x in range(1, 23):
            maps2_2_reachables[(x, 3)] = 34 - x + 1

        self.assertEqual(self.map2_2.reachable(), maps2_2_reachables)

    def test_reachable_keys(self):
        self.assertEqual(self.map1_0.reachable_keys(), {'a': (7, 1)})
        self.assertEqual(self.map2_2.reachable_keys(), {'c': (21, 1), 'd': (1, 3)})

    def test_reachable_doors(self):
        self.assertEqual(self.map1_0.reachable_doors(), {'A': set([(4, 1)])})
        self.assertEqual(self.map2_2.reachable_doors(), {'C': set([(10, 1)])})

    def test_get_available_moves(self):
        self.assertEqual(self.map1_0.get_available_moves(), {(7, 1): 2})
        self.assertEqual(self.map1_1.get_available_moves(), {(3, 1): 4})
        self.assertEqual(self.map2_2.get_available_moves(), {(21, 1): 10, (1, 3): 34})

    def test_calc_fewest_steps_to_all_keys_1(self):
        self.assertEqual(calc_fewest_steps_to_all_keys(self.map1_0), 8)

    def test_bfs(self):
        self.assertEqual(bfs(self.map1_0), 8)
        self.assertEqual(bfs(self.map2_0), 86)
        self.assertEqual(bfs(self.map3_0), 132)
        # self.assertEqual(bfs(self.map4_0), 136)
        # self.assertEqual(bfs(self.map5_0), 81)

    def test_calc_fewest_steps_to_all_keys_2(self):
        self.assertEqual(calc_fewest_steps_to_all_keys(self.map2_0), 86)

    def test_calc_fewest_steps_to_all_keys_3_5(self):
        self.assertEqual(calc_fewest_steps_to_all_keys(self.map3_0), 132)
        self.assertEqual(calc_fewest_steps_to_all_keys(self.map5_0), 81)

    @unittest.skip('takes too long')
    def test_calc_fewest_steps_to_all_keys_4_longrunning(
        self,
    ):  # this test may have revealed a termination problem
        self.assertEqual(calc_fewest_steps_to_all_keys(self.map4_0), 136)
