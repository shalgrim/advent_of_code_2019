from intcode import Intcode


def main():
    with open('data/input02.txt') as f:
        content = f.read()
    program_input = [int(x) for x in content.split(',')]
    intcode = Intcode(program_input)
    intcode.memory[1] = 12
    intcode.memory[2] = 2
    intcode.run()
    return intcode.memory[0]


if __name__ == '__main__':
    print(main())  # 3850704
