from unittest import TestCase
from unittest.mock import patch

from day05_1 import get_params, parse_instruction, process_instruction, run_program
from day09_1 import run_program as rp9


class TestDay05(TestCase):
    def test_parse_instruction(self):
        self.assertEqual(parse_instruction(1002), (2, [0, 1, 0]))

    def test_get_params(self):
        self.assertEqual(get_params([1002, 4, 3, 4, 33], 0, 2, [0, 1, 0]), [33, 3, 4])

    def test_process_instruction(self):
        output = [1002, 4, 3, 4, 33]
        self.assertEqual(process_instruction(2, [33, 3, 4], output, 0, []), 4)
        self.assertEqual(output, [1002, 4, 3, 4, 99])

    @patch('builtins.input', lambda x: 1)
    def test_run_program_part_1(self):
        with open('data/input05_github_login.txt') as f:
            content = f.read()
        program_input = [int(x) for x in content.split(',')]
        the_outputs = run_program(program_input)
        self.assertEqual(the_outputs[-1], 9431221)

    @patch('builtins.input', lambda x: 1)
    def test_backward_compat(self):
        with open('data/input05_github_login.txt') as f:
            content = f.read()
        program_input = [int(x) for x in content.split(',')]
        the_outputs = rp9(program_input)[1]
        self.assertEqual(the_outputs[-1], 9431221)
