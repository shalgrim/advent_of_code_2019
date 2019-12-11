from copy import copy


def run_program(instructions):
    memory = copy(instructions)
    instruction_pointer = 0

    while memory[instruction_pointer] != 99:
        if memory[instruction_pointer] == 1:
            memory[memory[instruction_pointer + 3]] = (
                memory[memory[instruction_pointer + 1]]
                + memory[memory[instruction_pointer + 2]]
            )
        elif memory[instruction_pointer] == 2:
            memory[memory[instruction_pointer + 3]] = (
                memory[memory[instruction_pointer + 1]]
                * memory[memory[instruction_pointer + 2]]
            )
        instruction_pointer += 4
    return memory


def main():
    with open('data/input02.txt') as f:
        content = f.read()
    program_input = [int(x) for x in content.split(',')]
    program_input[1] = 12
    program_input[2] = 2
    memory = run_program(program_input)
    return memory[0]


if __name__ == '__main__':
    print(main())  # 3850704
