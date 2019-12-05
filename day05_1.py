from copy import copy


def parse_instruction(instruction_int):
    instruction_s = str(instruction_int)
    opcode = int(instruction_s[-2:])
    param_modes = [0, 0, 0]

    for i, digit in enumerate(instruction_s[:-2][::-1]):
        param_modes[i] = int(digit)

    return opcode, param_modes


def get_params(list_of_ints, instruction_pointer, opcode, param_modes):
    params = []
    if opcode in (1, 2):  # two input params, one output param
        for i in range(2):
            if param_modes[i] == 0:  # position
                params.append(list_of_ints[list_of_ints[instruction_pointer + i + 1]])
            elif param_modes[i] == 1:  # immediate
                params.append(list_of_ints[instruction_pointer + i + 1])

        params.append(list_of_ints[instruction_pointer + 3])
    elif opcode in (3, 4):
        params.append(list_of_ints[instruction_pointer + 1])

    return params


def process_instruction(opcode, params, output, instruction_pointer, the_outputs):
    if opcode == 1:
        output[params[2]] = params[0] + params[1]
        instruction_pointer += 4
    elif opcode == 2:
        output[params[2]] = params[0] * params[1]
        instruction_pointer += 4
    elif opcode == 3:
        in_param = input('need some input please: ')
        # in_param = 1  # for unit tests
        output[params[0]] = int(in_param)
        instruction_pointer += 2
    elif opcode == 4:
        print(output[params[0]])
        the_outputs.append(output[params[0]])
        instruction_pointer += 2

    return instruction_pointer


def run_program(list_of_ints):
    output = copy(list_of_ints)
    instruction_pointer = 0
    the_outputs = []

    while output[instruction_pointer] != 99:
        # print(f'{instruction_pointer=}')
        instruction = output[instruction_pointer]
        opcode, param_modes = parse_instruction(instruction)
        params = get_params(output, instruction_pointer, opcode, param_modes)
        instruction_pointer = process_instruction(opcode, params, output, instruction_pointer, the_outputs)

    return the_outputs


if __name__ == '__main__':
    with open('data/input05.txt') as f:
        content = f.read()
    program_input = [int(x) for x in content.split(',')]
    output = run_program(program_input)  # 223 is too low, 9431221 is correct
