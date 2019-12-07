INPUT_FN = 'data/input01.txt'


def calc_fuel(mass):
    return mass // 3 - 2


if __name__ == '__main__':
    with open(INPUT_FN) as f:
        masses = [int(line.strip()) for line in f.readlines()]

    fuel = [calc_fuel(mass) for mass in masses]
    print(sum(fuel))
