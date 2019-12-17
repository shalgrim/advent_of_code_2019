from copy import copy
from day05_1 import parse_instruction
from day09_1 import get_params, special_assign
from day13_1 import process_instruction as process_instruction_13


OPEN = '.'
SCAFFOLD = '#'
map_output = ''


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


def process_instruction(
        opcode, params, output, instruction_pointer, the_outputs, param_modes, relative_base
):
    global map_output
    if opcode in (1, 2, 5, 6, 7, 8, 9):
        return process_instruction_13(
            opcode,
            params,
            output,
            instruction_pointer,
            the_outputs,
            param_modes,
            relative_base,
        )
    # elif opcode == 3:
    #     in_param = get_next_move()
    #     if in_param == -1:
    #         return output.index(99), None
    #     if param_modes[0] == 2:
    #         try:
    #             output[params[0] + relative_base] = in_param
    #         except IndexError:
    #             special_assign(output, params[0] + relative_base, in_param)
    #     else:
    #         output[params[0]] = in_param
    #     instruction_pointer += 2
    elif opcode == 4:
        if param_modes[0] == 0:
            out_param = output[params[0]]
        elif param_modes[0] == 1:
            out_param = params[0]
        elif param_modes[0] == 2:
            out_param = output[params[0] + relative_base]
        else:
            raise Exception('what mode?')
        map_output += chr(out_param)
        instruction_pointer += 2
    else:
        print(map_output)
        raise Exception(f'what {opcode=}')

    return instruction_pointer, relative_base


def identify_intersections(amap):
    lines = amap.split()
    intersections = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            try:
                candidates = [lines[y][x], lines[y-1][x], lines[y+1][x], lines[y][x-1], lines[y][x+1]]
            except IndexError:
                continue
            if all(c == SCAFFOLD for c in candidates):
                intersections.add((x, y))

    return intersections


if __name__ == '__main__':
    with open('data/input17.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    run_program(program_instructions)
    print(map_output)
    intersections = identify_intersections(map_output)
    print(intersections)
    alignment_params = [i[0] * i[1] for i in intersections]
    print(sum(alignment_params))
