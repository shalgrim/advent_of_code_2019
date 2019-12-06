from collections import defaultdict


def count_all_orbits(inlines):
    direct_orbits = {}
    for line in inlines:
        orbited, orbiter = line.split(')')
        direct_orbits[orbiter] = orbited

    orbiter_counts = {}
    for orbiter in direct_orbits:
        orbiter_counts[orbiter] = 1
        suborbiter = orbiter

        while direct_orbits[suborbiter] != 'COM':
            suborbiter = direct_orbits[suborbiter]
            orbiter_counts[orbiter] += 1

    return sum(list(orbiter_counts.values()))


if __name__ == '__main__':
    with open('data/input06.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(count_all_orbits(lines))
