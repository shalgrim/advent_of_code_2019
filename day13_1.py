from copy import copy

from day05_1 import parse_instruction
from day09_1 import get_params, special_assign


current_outputs = []
tiles_to_draw = {}


def process_instruction(
        opcode, params, output, instruction_pointer, the_outputs, param_modes, relative_base
):
    global current_outputs, tiles_to_draw

    if opcode == 1:
        try:
            output[params[2]] = params[0] + params[1]
        except IndexError:
            special_assign(output, params[2], params[0] + params[1])
        instruction_pointer += 4
    elif opcode == 2:
        try:
            output[params[2]] = params[0] * params[1]
        except IndexError:
            special_assign(output, params[2], params[0] * params[1])
        instruction_pointer += 4
    elif opcode == 3:
        raise Exception('no input expected')
    elif opcode == 4:
        if param_modes[0] == 0:
            out_param = output[params[0]]
        elif param_modes[0] == 1:
            out_param = params[0]
        elif param_modes[0] == 2:
            out_param = output[params[0] + relative_base]
        else:
            raise Exception('what mode?')
        current_outputs.append(out_param)
        if len(current_outputs) == 3:
            tiles_to_draw[(current_outputs[0]), current_outputs[1]] = current_outputs[2]
            current_outputs = []
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
        val = 1 if params[0] == params[1] else 0
        try:
            output[params[2]] = val
        except IndexError:
            special_assign(output, params[2], val)
        instruction_pointer += 4
    elif opcode == 9:
        relative_base += params[0]
        instruction_pointer += 2
    else:
        raise Exception('what opcode')

    return instruction_pointer, relative_base


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


if __name__ == '__main__':
    with open('data/input13.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    run_program(program_instructions)
    print(len([v for v in tiles_to_draw.values() if v == 2]))
