from copy import copy

from day05_1 import parse_instruction
from day09_1 import get_params, special_assign

points_visited = {}
current_position = (0, 0)
current_direction = 'U'
seen_first_output = False


def paint_panel(color):
    global points_visited, current_position
    if color == 1:
        points_visited[current_position] = '#'
    else:
        points_visited[current_position] = '.'


def turn(direction):
    global current_direction
    if direction == 0:  # turn left
        if current_direction == 'U':
            current_direction = 'L'
        elif current_direction == 'R':
            current_direction = 'U'
        elif current_direction == 'D':
            current_direction = 'R'
        else:
            current_direction = 'D'
    else:  # turn right
        if current_direction == 'U':
            current_direction = 'R'
        elif current_direction == 'R':
            current_direction = 'D'
        elif current_direction == 'D':
            current_direction = 'L'
        else:
            current_direction = 'U'


def advance():
    global current_direction, current_position
    if current_direction == 'U':
        current_position = (current_position[0], current_position[1] - 1)
    elif current_direction == 'D':
        current_position = (current_position[0], current_position[1] + 1)
    elif current_direction == 'L':
        current_position = (current_position[0] - 1, current_position[1])
    else:
        current_position = (current_position[0] + 1, current_position[1])


def process_instruction(
    opcode, params, output, instruction_pointer, the_outputs, param_modes, relative_base
):
    global points_visited, current_position, current_direction, seen_first_output
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
        current_color = points_visited.get(current_position, '.')
        in_param = 0 if current_color == '.' else 1
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
        print(out_param)
        the_outputs.append(out_param)
        instruction_pointer += 2

        if not seen_first_output:
            seen_first_output = True
            paint_panel(out_param)
        else:
            seen_first_output = False
            turn(out_param)
            advance()
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
    memory = copy(instructions)  # + ([0] * 2000000)  # doesn't seem to help
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
    with open('data/input11.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    run_program(program_instructions)
    print(len(points_visited))
