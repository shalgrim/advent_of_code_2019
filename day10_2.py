from day10_1 import find_best_asteroid, map_asteroids, get_visible_asteroids
import math


def get_radians(center, other):
    assert center != other
    if center[0] == other[0]:
        if center[1] < other[1]:  # meaning center is higher as my eyes work
            return math.pi
        else:
            return 0
    elif center[1] == other[1]:
        if center[0] < other[0]:  # meaning center is to left
            return math.pi/2
        else:
            return 3*math.pi/2
    elif other[0] > center[0] and other[1] < center[1]:  # quadrant I
        adjacent = center[1] - other[1]
        opposite = other[0] - center[0]
        tangent = opposite / adjacent
        radians = math.atan(tangent)
    elif other[0] > center[0] and other[1] > center[1]:  # quadrant II
        adjacent = other[0] - center[0]
        opposite = other[1] - center[1]
        tangent = opposite / adjacent
        radians = math.atan(tangent) + math.pi/2
    elif other[0] < center[0] and other[1] > center[1]:  # quadrant III
        adjacent = other[1] - center[1]
        opposite = center[0] - other[0]
        tangent = opposite / adjacent
        radians = math.atan(tangent) + math.pi
    elif other[0] < center[0] and other[1] < center[1]:  # quadrant IV
        adjacent = center[0] - other[0]
        opposite = center[1] - other[1]
        tangent = opposite / adjacent
        radians = math.atan(tangent) + 3*math.pi/2
    else:
        raise Exception(f'{center=}, {other=}')
    return radians


def get_next_asteroid(visibles_and_radians, rotation, never_fired):
    sorted_by_radians = sorted(visibles_and_radians, key=lambda c: c[1])
    if never_fired and sorted_by_radians[0][1] == 0:
        return sorted_by_radians[0]
    for a, r in sorted_by_radians:
        if r > rotation:
            return a, r
    return sorted_by_radians[0]  # laser resets


def get_vaporization_list(lines):
    asteroids = map_asteroids(lines)
    laser = find_best_asteroid(lines)[0]
    rotation = 0.0
    vaporized = []
    never_fired = True
    while len(asteroids) > 1:
        visible_asteroids = get_visible_asteroids(laser, asteroids)
        visibles_and_radians = [(a, get_radians(laser, a)) for a in visible_asteroids]
        next_asteroid, rotation = get_next_asteroid(visibles_and_radians, rotation, never_fired)
        never_fired = False
        vaporized.append(next_asteroid)
        asteroids.remove(next_asteroid)
        # if len(vaporized) == 299:
        #     return vaporized

    return vaporized


if __name__ == '__main__':
    with open('data/input10.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    vl = get_vaporization_list(lines)
