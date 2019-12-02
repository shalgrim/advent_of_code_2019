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
