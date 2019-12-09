from unittest import TestCase
from day02_1 import run_program
from day09_1 import run_program as rp9


class TestDay02(TestCase):
    def test_run_program(self):
        self.assertEqual(
            run_program([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]),
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        )
        self.assertEqual(run_program([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])
        self.assertEqual(run_program([2, 3, 0, 3, 99]), [2, 3, 0, 6, 99])
        self.assertEqual(run_program([2, 4, 4, 5, 99, 0]), [2, 4, 4, 5, 99, 9801])
        self.assertEqual(
            run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]), [30, 1, 1, 4, 2, 5, 6, 0, 99]
        )

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
