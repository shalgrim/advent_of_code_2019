from day06_1 import get_direct_orbits


def me_to_santa_count(lines):
    direct_orbits = get_direct_orbits(lines)
    start = direct_orbits['YOU']
    destination = direct_orbits['SAN']

    orbited_by_santa = [destination]
    new_orbited = destination

    while new_orbited != 'COM':
        new_orbited = direct_orbits[new_orbited]
        orbited_by_santa.append(new_orbited)

    orbited_by_me = [start]
    new_orbited = start

    while new_orbited != 'COM':
        new_orbited = direct_orbits[new_orbited]
        orbited_by_me.append(new_orbited)

    commonly_orbited = set(orbited_by_santa).intersection(set(orbited_by_me))
    distances_from_me = {co: orbited_by_me.index(co) for co in commonly_orbited}
    distance_to_outermost_commonly_orbited = min(list(distances_from_me.values()))

    for co in commonly_orbited:
        if distances_from_me[co] == distance_to_outermost_commonly_orbited:
            outermost_commonly_orbited = co
            break
    else:
        outermost_commonly_orbited = None

    steps_to_commonly_orbited = orbited_by_me.index(outermost_commonly_orbited)
    steps_from_commonly_orbited = orbited_by_santa.index(outermost_commonly_orbited)
    return steps_to_commonly_orbited + steps_from_commonly_orbited


if __name__ == '__main__':
    with open('data/input06.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(me_to_santa_count(lines))
