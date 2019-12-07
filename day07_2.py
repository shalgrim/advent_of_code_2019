import itertools
from copy import copy

from day05_1 import get_params, parse_instruction

global_output_val = None


class Amplifier(object):
    def __init__(self, instructions, phase):
        self.memory = copy(instructions)
        self.phase = phase
        self.provided_phase = False
        self.instruction_pointer = 0

    def run_program(self, first_input):
        global global_output_val
        while self.memory[self.instruction_pointer] != 99:
            instruction = self.memory[self.instruction_pointer]
            opcode, param_modes = parse_instruction(instruction)
            params = get_params(
                self.memory, self.instruction_pointer, opcode, param_modes
            )
            if opcode == 1:
                self.memory[params[2]] = params[0] + params[1]
                self.instruction_pointer += 4
            elif opcode == 2:
                self.memory[params[2]] = params[0] * params[1]
                self.instruction_pointer += 4
            elif opcode == 3:
                self.memory[params[0]] = (
                    first_input if self.provided_phase else self.phase
                )
                self.provided_phase = True
                self.instruction_pointer += 2
            elif opcode == 4:
                output_val = self.memory[params[0]]
                self.instruction_pointer += 2
                global_output_val = output_val
                # print(output_val)
                return output_val
            elif opcode == 5:
                if params[0] != 0:
                    self.instruction_pointer = params[1]
                else:
                    self.instruction_pointer += 3
            elif opcode == 6:
                if params[0] == 0:
                    self.instruction_pointer = params[1]
                else:
                    self.instruction_pointer += 3
            elif opcode == 7:
                self.memory[params[2]] = 1 if params[0] < params[1] else 0
                self.instruction_pointer += 4
            elif opcode == 8:
                self.memory[params[2]] = 1 if params[0] == params[1] else 0
                self.instruction_pointer += 4

        return ('Done', global_output_val)


def run_amplifier_series(instructions, phases):
    amplifiers = [Amplifier(instructions, p) for p in phases]
    amp_index = 0
    input_val = amplifiers[amp_index].run_program(0)
    while not (isinstance(input_val, tuple)):
        amp_index = 0 if amp_index == 4 else amp_index + 1
        input_val = amplifiers[amp_index].run_program(input_val)
    return input_val[1]


def find_max_signal_in_feedback_mode(instructions):
    phases = [5, 6, 7, 8, 9]
    signals = [
        run_amplifier_series(instructions, list(perm))
        for perm in itertools.permutations(phases)
    ]
    return max(signals)


if __name__ == '__main__':
    with open('data/input07.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    answer = find_max_signal_in_feedback_mode(program_instructions)
    print(answer)
