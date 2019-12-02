from unittest import TestCase
from day02_1 import run_program


class TestDay01(TestCase):
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
