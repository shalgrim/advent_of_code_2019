from unittest import TestCase

from day12_1 import main as main_part_1, run_time, total_energy
from day12_2 import main as main_part_2
from moon import Moon


class TestDay12(TestCase):
    def setUp(self) -> None:
        self.moons = [
            Moon(-1, 0, 2),
            Moon(2, -10, -7),
            Moon(4, -8, 8),
            Moon(3, 5, -1),
        ]

    def test_run_time_1(self):
        inmoons = [
            Moon(-1, 0, 2),
            Moon(2, -10, -7),
            Moon(4, -8, 8),
            Moon(3, 5, -1),
        ]
        moons_0001 = [
            Moon(2, -1, 1, [3, -1, -1]),
            Moon(3, -7, -4, [1, 3, 3]),
            Moon(1, -7, 5, [-3, 1, -3]),
            Moon(2, 2, 0, [-1, -3, 1]),
        ]
        moons_0002 = [
            Moon(5, -3, -1, [3, -2, -2]),
            Moon(1, -2, 2, [-2, 5, 6]),
            Moon(1, -4, -1, [0, 3, -6]),
            Moon(1, -4, 2, [-1, -6, 2]),
        ]
        moons_0010 = [
            Moon(2, 1, -3, [-3, -2, 1]),
            Moon(1, -8, 0, [-1, 1, 3]),
            Moon(3, -6, 1, [3, 2, -3]),
            Moon(2, 0, 4, [1, -1, -1]),
        ]
        self.assertListEqual(run_time(inmoons, 0), inmoons)
        self.assertListEqual(run_time(inmoons, 1), moons_0001)
        self.assertListEqual(run_time(inmoons, 2), moons_0002)
        self.assertListEqual(run_time(inmoons, 10), moons_0010)

    def test_main_1(self):
        moons = [
            Moon(-8, -10, 0),
            Moon(5, 5, 10),
            Moon(2, -7, 3),
            Moon(9, -8, -3),
        ]
        post_run_moons = run_time(moons, 100)
        self.assertEqual(total_energy(post_run_moons), 1940)

    def test_part_1(self):
        moons = [
            Moon(-9, 10, -1),
            Moon(-14, -8, 14),
            Moon(1, 5, 6),
            Moon(-19, 7, 8),
        ]
        self.assertEqual(main_part_1(moons), 8538)

    def test_main_2(self):
        self.assertEqual(main_part_2(self.moons), 2772)

    # def test_main_2_longtime(self):  # would take 195 hours-ish as currently written
    #     moons = [
    #         Moon(-8, -10, 0),
    #         Moon(5, 5, 10),
    #         Moon(2, -7, 3),
    #         Moon(9, -8, -3),
    #     ]
    #     self.assertEqual(main_part_2(moons), 4686774924)
