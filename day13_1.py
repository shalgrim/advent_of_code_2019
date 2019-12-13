from copy import copy
from collections import defaultdict

from day05_1 import parse_instruction
from day09_1 import get_params, special_assign

CHARACTERS = defaultdict(lambda: ' ')
CHARACTERS[1] = '|'
CHARACTERS[2] = '#'
CHARACTERS[3] = '_'
CHARACTERS[4] = 'O'

current_outputs = []
tiles_to_draw = {}
score = 0
ball_x = 0
paddle_x = 0


def process_instruction(
        opcode, params, output, instruction_pointer, the_outputs, param_modes, relative_base
):
    global current_outputs, tiles_to_draw, score, ball_x, paddle_x

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
        render_game_screen(tiles_to_draw)
        # in_param = None
        # while in_param not in ['-1', '0', '1']:
        #     in_param = input('move joystick (-1 left, 0 neutral, 1 right): ')
        # in_param = int(in_param)
        if ball_x < paddle_x:
            in_param = -1
        elif ball_x > paddle_x:
            in_param = 1
        else:
            in_param = 0
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
        current_outputs.append(out_param)
        if len(current_outputs) == 3:
            if current_outputs[0] == -1 and current_outputs[1] == 0:
                score = current_outputs[2]
                render_game_screen(tiles_to_draw, score)
            else:
                tiles_to_draw[(current_outputs[0]), current_outputs[1]] = current_outputs[2]
                if current_outputs[2] == 3:
                    paddle_x = current_outputs[0]
                elif current_outputs[2] == 4:
                    ball_x = current_outputs[0]
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


def render_game_screen(tiles, score=0):
    min_x = min(k[0] for k in tiles.keys())
    max_x = max(k[0] for k in tiles.keys())
    min_y = min(k[1] for k in tiles.keys())
    max_y = max(k[1] for k in tiles.keys())

    lines = []

    for y in range(min_y, max_y+1):
        line = []
        for x in range(min_x, max_x+1):
            line.append(CHARACTERS[tiles[(x, y)]])
        lines.append(''.join(line))

    print(f'{score=}')
    print ('\n'.join(lines))


if __name__ == '__main__':
    with open('data/input13.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    run_program(program_instructions)
    print(len([v for v in tiles_to_draw.values() if v == 2]))  # 284
    render_game_screen(tiles_to_draw)
