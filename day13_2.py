from day13_1 import run_program


if __name__ == '__main__':
    with open('data/input13.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    program_instructions[0] = 2  # 2 quarters inserted so we can play for free
    run_program(program_instructions)  # 13581
