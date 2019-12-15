from copy import copy
from day05_1 import parse_instruction
from day09_1 import get_params, special_assign
from day13_1 import process_instruction as process_instruction_13

OPEN = '.'
WALL = '#'
OXYGEN = 'O'
map = {(0, 0): OPEN}
distance_from_origin = {(0, 0): 0}
current_location = (0, 0)
current_path = [(0, 0)]
attempted_location = None


def get_map_char(x, y):
    if current_location == (x, y):
        return 'D'
    return map.get((x, y), '?')


def render_map():
    min_y = min(k[1] for k in map.keys())
    max_y = max(k[1] for k in map.keys())
    min_x = min(k[0] for k in map.keys())
    max_x = max(k[0] for k in map.keys())

    lines = []
    for y in range(min_y, max_y+1):
        lines.append(''.join(get_map_char(x, y) for x in range(min_x, max_x+1)))

    print('\n'.join(lines))


def get_next_move():
    global attempted_location
    # try North, East, South, West
    north = current_location[0], current_location[1] - 1
    south = current_location[0], current_location[1] + 1
    east = current_location[0] + 1, current_location[1]
    west = current_location[0] - 1, current_location[1]

    for i, direction in enumerate([north, south, east, west]):
        if map.get(direction, None) is None:
            attempted_location = direction
            return i + 1  # in_param

    # go back the way we came
    attempted_location = current_path[-2]
    answer = [north, south, east, west].index(attempted_location) + 1
    current_path.pop()
    return answer


def process_out_param(out_param):
    global current_location
    if out_param == 1:
        if attempted_location not in distance_from_origin:
            distance_from_origin[attempted_location] = (
                distance_from_origin[current_location] + 1
            )
        current_location = attempted_location
        if current_location == current_path[-1]:  # i already popped it
            pass
        elif current_location in current_path:
            raise Exception('i didn"t expect to be here')
        else:
            current_path.append(current_location)
        map[current_location] = OPEN
    elif out_param == 0:
        map[attempted_location] = WALL
    elif out_param == 2:
        if attempted_location not in distance_from_origin:
            distance_from_origin[attempted_location] = (
                distance_from_origin[current_location] + 1
            )
        current_location = attempted_location
        current_path.append(current_location)
        map[current_location] = OXYGEN
    else:
        raise Exception(f'what {out_param=}')


def process_instruction(
    opcode, params, output, instruction_pointer, the_outputs, param_modes, relative_base
):
    if opcode in (1, 2, 5, 6, 7, 8):
        return process_instruction_13(
            opcode,
            params,
            output,
            instruction_pointer,
            the_outputs,
            param_modes,
            relative_base,
        )
    elif opcode == 3:
        in_param = get_next_move()
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
        process_out_param(out_param)
        instruction_pointer += 2
        render_map()
    else:
        raise Exception(f'what {opcode=}')

    return instruction_pointer, relative_base


def run_program(instructions):
    relative_base = 0
    memory = copy(instructions)
    instruction_pointer = 0
    the_outputs = []

    # while memory[instruction_pointer] != 99:
    while OXYGEN not in map.values():
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
    with open('data/input15.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    run_program(program_instructions)
    for k, v in map.items():
        if v == OXYGEN:
            oxygen_location = k
            break
    print(distance_from_origin[k])
