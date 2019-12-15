from copy import copy

from day05_1 import parse_instruction
from day09_1 import get_params
from day15_1 import OPEN, OXYGEN, map, process_instruction


def run_program(instructions):
    relative_base = 0
    memory = copy(instructions)
    instruction_pointer = 0
    the_outputs = []

    while memory[instruction_pointer] != 99:
        instruction = memory[instruction_pointer]
        opcode, param_modes = parse_instruction(instruction)
        params = get_params(
            memory, instruction_pointer, opcode, param_modes, relative_base
        )
        instruction_pointer, relative_base = process_instruction(
            opcode,
            params,
            memory,
            instruction_pointer,
            the_outputs,
            param_modes,
            relative_base,
        )


def oxygenize(map):
    original_oxygen_locations = [k for k, v in map.items() if v == OXYGEN]

    for ool in original_oxygen_locations:
        north = ool[0], ool[1]-1
        south = ool[0], ool[1]+1
        east = ool[0]+1, ool[1]
        west = ool[0]-1, ool[1]

        for new_loc in [north, south, east, west]:
            if map[new_loc] == OPEN:
                map[new_loc] = OXYGEN


def count_steps_to_full_oxygenization(map):
    steps = 0
    while OPEN in map.values():
        oxygenize(map)
        steps += 1

    return steps


if __name__ == '__main__':
    with open('data/input15.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    run_program(program_instructions)
    print('have the final map')
    print(count_steps_to_full_oxygenization(map))
