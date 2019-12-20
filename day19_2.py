from copy import copy
from day05_1 import parse_instruction
from day09_1 import get_params, special_assign

provided_x = False


def process_instruction(
        opcode, params, output, instruction_pointer, the_inputs, param_modes, relative_base
):
    """Note I messed with the arguments in this version"""
    global provided_x
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
        if provided_x:
            in_param = the_inputs[1]
            provided_x = False
        else:
            in_param = the_inputs[0]
            provided_x = True
        if param_modes[0] == 2:
            try:
                output[params[0] + relative_base] = in_param
            except IndexError:
                special_assign(output, params[0] + relative_base, in_param)
        else:
            output[params[0]] = in_param
        instruction_pointer += 2
    elif opcode == 4:
        if param_modes[0] == 0:
            out_param = output[params[0]]
        elif param_modes[0] == 1:
            out_param = params[0]
        elif param_modes[0] == 2:
            out_param = output[params[0] + relative_base]
        else:
            raise Exception('what mode?')
        return -1, out_param
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
        try:
            output[params[2]] = 1 if params[0] < params[1] else 0
        except IndexError:
            # val_to_set = 1 if params[0] < params[1] else 0
            special_assign(output, params[2], 1 if params[0] < params[1] else 0)
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


def run_program(instructions, x, y):
    print(f'running run_program {x=}, {y=}')
    global provided_x
    provided_x = False
    relative_base = 0
    memory = copy(instructions)
    instruction_pointer = 0

    while memory[instruction_pointer] != 99 and instruction_pointer >= 0:
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
            (x, y),
            param_modes,
            relative_base,
        )

    assert instruction_pointer == -1
    print(f'returning {relative_base=}')
    return relative_base  # i store it here in this output opcode 4 instruction processing


def calc_beam_width_and_start(program_instructions, y):
    print(f'running calc_beam_width_and_start with {y=}')
    program_output = 0
    x = -1

    while not program_output and x < 200:
        x += 1
        program_output = run_program(program_instructions, x, y)

    beam_start = x  # never get here if y == 1 or y == 2

    while program_output:
        x += 1
        program_output = run_program(program_instructions, x, y)

    beam_width = x - beam_start

    return beam_width, beam_start


def main(program_instructions):
    beam_width = 0
    y = 1
    while beam_width < 1000:
        y += 1
        beam_width, beam_start = calc_beam_width_and_start(program_instructions, y)
        print(f'{y=}, {beam_start=}, {beam_width=}')

    return beam_start, y


if __name__ == '__main__':
    with open('data/input19.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    print(main(program_instructions))
