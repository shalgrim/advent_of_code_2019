"""
< x = -9, y = 10, z = -1 >
< x = -14, y = -8, z = 14 >
< x = 1, y = 5, z = 6 >
< x = -19, y = 7, z = 8 >
"""

import itertools

from copy import deepcopy
from moon import Moon


def run_time(moons, steps):
    outmoons = deepcopy(moons)
    for _ in range(steps):
        for moon_pair in itertools.permutations(outmoons, 2):
            moon_pair[0].apply_gravity(moon_pair[1])

        for moon in outmoons:
            moon.apply_velocity()

    return outmoons


def total_energy(moons):
    return sum([m.energy for m in moons])


def main(moons):
    moons = run_time(moons, 1000)
    return total_energy(moons)


if __name__ == '__main__':
    moons = [
        Moon(-9, 10, -1),
        Moon(-14, -8, 14),
        Moon(1, 5, 6),
        Moon(-19, 7, 8),
    ]
    print(main(moons))  # 74074386000 is wrong...8538 is correct even though tests fail
