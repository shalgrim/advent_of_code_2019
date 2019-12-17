if __name__ == '__main__':
    with open('data/input17.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    assert program_instructions[0] == 1
    program_instructions[0] = 2
