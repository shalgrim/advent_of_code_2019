from day01_1 import INPUT_FN


def calc_fuel(mass):
    fuel = 0
    incremental_fuel = mass
    while incremental_fuel > 0:
        incremental_fuel = incremental_fuel // 3 - 2
        fuel += max(incremental_fuel, 0)

    return fuel


if __name__ == '__main__':
    with open(INPUT_FN) as f:
        masses = [int(line.strip()) for line in f.readlines()]

    fuel = [calc_fuel(mass) for mass in masses]
    print(sum(fuel))
