from unittest import TestCase

from day07_1 import find_max_signal, run_all_amplifiers
from day07_2 import find_max_signal_in_feedback_mode, run_amplifier_series


class TestDay07(TestCase):
    def test_run_all_amplifiers(self):
        content = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        this_input = [int(x) for x in content.split(',')]
        self.assertEqual(run_all_amplifiers(this_input, [4, 3, 2, 1, 0]), 43210)
        self.assertEqual(find_max_signal(this_input), 43210)
        content = (
            '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
        )
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

    def test_run_amplifier_series(self):
        content = (
            '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,'
            '27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
        )
        instructions = [int(x) for x in content.split(',')]
        phases = [9, 8, 7, 6, 5]
        self.assertEqual(run_amplifier_series(instructions, phases), 139629729)
        content = (  # actually is 18216
            '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,'
            '-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,'
            '53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
        )
        instructions = [int(x) for x in content.split(',')]
        phases = [9, 7, 8, 5, 6]
        self.assertEqual(run_amplifier_series(instructions, phases), 18216)

    def test_run_find_max_signal_in_feedback_mode(self):
        content = (
            '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,'
            '27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
        )
        instructions = [int(x) for x in content.split(',')]
        self.assertEqual(find_max_signal_in_feedback_mode(instructions), 139629729)
        content = (  # actually is 18216
            '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,'
            '-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,'
            '53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
        )
        instructions = [int(x) for x in content.split(',')]
        self.assertEqual(find_max_signal_in_feedback_mode(instructions), 18216)
