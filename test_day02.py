from unittest import TestCase

from day02_1 import main as main_part1
from day02_2 import main as main_part2
from day09_1 import run_program as rp9
from intcode import Intcode


class TestDay02(TestCase):
    def test_run_program(self):
        intcode = Intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        intcode.run()
        self.assertEqual(intcode.memory, [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
        intcode = Intcode([1, 0, 0, 0, 99])
        intcode.run()
        self.assertEqual(intcode.memory, [2, 0, 0, 0, 99])
        intcode = Intcode([2, 3, 0, 3, 99])
        intcode.run()
        self.assertEqual(intcode.memory, [2, 3, 0, 6, 99])
        intcode = Intcode([2, 4, 4, 5, 99, 0])
        intcode.run()
        self.assertEqual(intcode.memory, [2, 4, 4, 5, 99, 9801])
        intcode = Intcode([1, 1, 1, 4, 99, 5, 6, 0, 99])
        intcode.run()
        self.assertEqual(intcode.memory, [30, 1, 1, 4, 2, 5, 6, 0, 99])

    def test_backward_compatibility(self):
        self.assertEqual(
            rp9([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])[0],
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        )
        self.assertEqual(rp9([1, 0, 0, 0, 99])[0], [2, 0, 0, 0, 99])
        self.assertEqual(rp9([2, 3, 0, 3, 99])[0], [2, 3, 0, 6, 99])
        self.assertEqual(rp9([2, 4, 4, 5, 99, 0])[0], [2, 4, 4, 5, 99, 9801])
        self.assertEqual(
            rp9([1, 1, 1, 4, 99, 5, 6, 0, 99])[0], [30, 1, 1, 4, 2, 5, 6, 0, 99]
        )

    def test_part_1(self):
        self.assertEqual(main_part1(), 3850704)

    def test_part_2(self):
        self.assertEqual(main_part2(), 6718)
