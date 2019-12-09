from copy import copy
from day05_1 import parse_instruction


def get_params(list_of_ints, instruction_pointer, opcode, param_modes, relative_base=0):
    params = []
    if opcode in (1, 2, 5, 6, 7, 8):  # two input params, one output param
        for i in range(2):
            if param_modes[i] == 0:  # position
                try:
                    params.append(list_of_ints[list_of_ints[instruction_pointer + i + 1]])
                except IndexError:
                    params.append(0)
            elif param_modes[i] == 1:  # immediate
                params.append(list_of_ints[instruction_pointer + i + 1])
            elif param_modes[i] == 2:  # relative
                the_index = list_of_ints[instruction_pointer + 1 + i] + relative_base
                params.append(list_of_ints[the_index])
            else:
                raise Exception(f'what mode {param_modes[i]}, {i=}')

        if param_modes[2] == 0:
            params.append(list_of_ints[instruction_pointer + 3])
        elif param_modes[2] == 2:
            params.append(list_of_ints[instruction_pointer + 3] + relative_base)
        else:
            raise Exception(f'what mode {param_modes[2]=}')

        params.append(list_of_ints[instruction_pointer + 3])
    elif opcode in (3, 4):
        # we handle position vs relative later...
        params.append(list_of_ints[instruction_pointer + 1])
    elif opcode == 9:
        if param_modes[0] == 0:  # position
            params.append(list_of_ints[list_of_ints[instruction_pointer + 1]])
        elif param_modes[0] == 1:  # immediate
            params.append(list_of_ints[instruction_pointer + 1])
        elif param_modes[0] == 2:  # relative
            try:
                value_index = list_of_ints[instruction_pointer + 1] + relative_base
            except IndexError:
                value_index = 0
            params.append(list_of_ints[value_index])
        else:
            raise Exception(f'what mode {param_modes[0]}')

    else:
        raise Exception('what opcode')

    return params


def special_assign(the_list, index, value):
    assert index >= len(the_list)
    zeros_to_add = [0] * (index - len(the_list) + 1)
    the_list += zeros_to_add
    the_list[index] = value


def process_instruction(opcode, params, output, instruction_pointer, the_outputs, param_modes, relative_base):
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
        in_param = int(input('need some input please: '))
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
            print(output[params[0]])
            the_outputs.append(output[params[0]])
        elif param_modes[0] == 1:
            print(params[0])
            the_outputs.append(params[0])
        elif param_modes[0] == 2:
            print(output[params[0] + relative_base])
            the_outputs.append(output[params[0] + relative_base])
        else:
            raise Exception('what mode?')
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
    memory = copy(instructions)  # + ([0] * 2000000)  # doesn't seem to help
    instruction_pointer = 0
    the_outputs = []

    while memory[instruction_pointer] != 99:
        instruction = memory[instruction_pointer]
        opcode, param_modes = parse_instruction(instruction)
        params = get_params(memory, instruction_pointer, opcode, param_modes, relative_base)
        instruction_pointer, relative_base = process_instruction(
            opcode, params, memory, instruction_pointer, the_outputs, param_modes, relative_base
        )

    return memory, the_outputs


if __name__ == '__main__':
    with open('data/input09.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    output = run_program(program_instructions)
    print(output)  # 203 is too low
