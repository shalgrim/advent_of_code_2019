from copy import copy
from day05_1 import parse_instruction
from day09_1 import get_params, special_assign


the_output = {}
exploring_x = 49
exploring_y = -1
provided_x = False


def print_map():
    global the_output
    lines = []
    for y in range(50):
        intline = [the_output[(x, y)] for x in range(50)]
        charline = ['#' if il == 1 else '.' for il in intline]
        lines.append(''.join(charline))

    for line in lines:
        print(line)


def run_program(instructions):
    global provided_x
    provided_x = False
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
    # print(f'completed point {exploring_x}, {exploring_y}')


def process_instruction(
        opcode, params, output, instruction_pointer, the_outputs, param_modes, relative_base
):
    global the_output, exploring_x, exploring_y, provided_x

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
            in_param = exploring_y
            provided_x = False
        else:
            in_param = exploring_x
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
        the_output[(exploring_x, exploring_y)] = out_param
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


def main(program_instructions):
    global exploring_x, exploring_y
    for exploring_y in range(50):
        for exploring_x in range(50):
            run_program(program_instructions)


if __name__ == '__main__':
    with open('data/input19.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    main(program_instructions)
    print_map()  # don't consistently get a beam until y == 7
    print(sum(the_output.values()))  # 160 is the right answer
