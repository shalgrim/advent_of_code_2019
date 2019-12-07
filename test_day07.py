from unittest import TestCase
from day07_1 import run_all_amplifiers, find_max_signal


class TestDay07(TestCase):
    def test_run_all_amplifiers(self):
        content = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        this_input = [int(x) for x in content.split(',')]
        self.assertEqual(run_all_amplifiers(this_input, [4, 3, 2, 1, 0]), 43210)
        self.assertEqual(find_max_signal(this_input), 43210)
        content = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
        this_input = [int(x) for x in content.split(',')]
        self.assertEqual(run_all_amplifiers(this_input, [0, 1, 2, 3, 4]), 54321)
        self.assertEqual(find_max_signal(this_input), 54321)
        content = (
            '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,'
            '0'
        )
        this_input = [int(x) for x in content.split(',')]
        self.assertEqual(run_all_amplifiers(this_input, [1, 0, 4, 3, 2]), 65210)
        self.assertEqual(find_max_signal(this_input), 65210)
