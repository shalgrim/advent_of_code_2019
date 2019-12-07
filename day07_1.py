import itertools
from copy import copy
from day05_1 import parse_instruction, get_params

inputs = [0, 0]
next_input = 0
output_val = 0


def basic_input():
    the_input = input('need some input please: ')
    return the_input


def basic_output(val):
    print(val)


def process_instruction(
    opcode,
    params,
    output,
    instruction_pointer,
    the_outputs,
):
    global inputs, next_input, output_val

    if opcode == 1:
        output[params[2]] = params[0] + params[1]
        instruction_pointer += 4
    elif opcode == 2:
        output[params[2]] = params[0] * params[1]
        instruction_pointer += 4
    elif opcode == 3:
        in_param = inputs[next_input]
        next_input += 1
        output[params[0]] = int(in_param)
        instruction_pointer += 2
    elif opcode == 4:
        output_val = output[params[0]]
        instruction_pointer += 2
    elif opcode == 5:
        if params[0] != 0:
            instruction_pointer = params[1]
        else:
            instruction_pointer += 3
    elif opcode == 6:
        if params[0] == 0:
            instruction_pointer = params[1]
        else:
            instruction_pointer += 3
    elif opcode == 7:
        output[params[2]] = 1 if params[0] < params[1] else 0
        instruction_pointer += 4
    elif opcode == 8:
        output[params[2]] = 1 if params[0] == params[1] else 0
        instruction_pointer += 4

    return instruction_pointer


def returns_vals(*args):
    my_vals = args

    def inner():
        for v in my_vals:
            yield v

    return inner


def new_output(val):
    return val


def run_all_amplifiers(instructions, phases):
    global inputs, next_input, output_val
    output_val = 0
    for p in phases:
        inputs = [p, output_val]
        next_input = 0
        run_program(instructions)

    return output_val


def run_program(instructions):
    memory = copy(instructions)
    instruction_pointer = 0
    the_outputs = []

    while memory[instruction_pointer] != 99:
        instruction = memory[instruction_pointer]
        opcode, param_modes = parse_instruction(instruction)
        params = get_params(memory, instruction_pointer, opcode, param_modes)
        instruction_pointer = process_instruction(
            opcode, params, memory, instruction_pointer, the_outputs
        )

    return the_outputs


def find_max_signal(instructions):
    phases = [0, 1, 2, 3, 4]
    signals = [run_all_amplifiers(instructions, list(perm)) for perm in itertools.permutations(phases)]
    return max(signals)


if __name__ == '__main__':
    with open('data/input07.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    # final_output = run_all_amplifiers(program_instructions, [4, 3, 2, 1, 0])
    # print(final_output)
    max_signal = find_max_signal(program_instructions)
    print(max_signal)
