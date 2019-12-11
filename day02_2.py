from day02_1 import run_program


def main():
    with open('data/input02.txt') as f:
        content = f.read()
    program_input = [int(x) for x in content.split(',')]

    for noun in range(100):
        program_input[1] = noun
        for verb in range(100):
            program_input[2] = verb
            output = run_program(program_input)
            if output[0] == 19690720:
                print(f'{noun=}')
                print(f'{verb=}')
                return 100 * noun + verb


if __name__ == '__main__':
    print(main())
