from unittest import TestCase
from day05_1 import parse_instruction, get_params, process_instruction, run_program


class TestDay05(TestCase):
    def test_parse_instruction(self):
        self.assertEqual(parse_instruction(1002), (2, [0, 1, 0]))

    def test_get_params(self):
        self.assertEqual(get_params([1002, 4, 3, 4, 33], 0, 2, [0, 1, 0]), [33, 3, 4])

    def test_process_instruction(self):
        output = [1002, 4, 3, 4, 33]
        self.assertEqual(process_instruction(2, [33, 3, 4], output, 0, []), 4)
        self.assertEqual(output, [1002, 4, 3, 4, 99])

    # def test_run_program_part_1(self):
    #     """Only works if we mock out the input for opcode 3"""
    #     with open('data/input05.txt') as f:
    #         content = f.read()
    #     program_input = [int(x) for x in content.split(',')]
    #     the_outputs = run_program(program_input)
    #     self.assertEqual(the_outputs[-1], 9431221)

    # I have to learn how to mock out input
    # def test_run_program_part_2(self):
    #     the_outputs = run_program()

