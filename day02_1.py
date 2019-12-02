from copy import copy


def run_program(list_of_ints):
    output = copy(list_of_ints)
    reading = 0

    while output[reading] != 99:
        if output[reading] == 1:
            output[output[reading+3]] = output[output[reading+1]] + output[output[reading+2]]
        elif output[reading] == 2:
            output[output[reading+3]] = output[output[reading+1]] * output[output[reading+2]]
        reading += 4
    return output


if __name__ == '__main__':
    with open('data/input02.txt') as f:
        content = f.read()
    program_input = [int(x) for x in content.split(',')]
    program_input[1] = 12
    program_input[2] = 2
    output = run_program(program_input)
    print(output[0])
