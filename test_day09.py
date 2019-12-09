from unittest import TestCase
from day09_1 import run_program


class TestDay09(TestCase):
    def test_run_program(self):
        self.assertEqual(
            run_program([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])[1],
            [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],
        )
        foo = run_program([1102, 34915192, 34915192, 7, 4, 7, 99, 0])[1]
        self.assertTrue(isinstance(foo[0], int))
        self.assertEqual(len(str(foo[0])), 16)
        self.assertEqual(
            run_program([104,1125899906842624,99])[1][0],
            1125899906842624,
        )
