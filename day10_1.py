def check_viz_horizontal(a, other, asteroids, slope):
    start = a[0]
    stop = other[0]
    step = 1 if other[0] >= a[0] else -1

    for i in range(start, stop, step):
        new_position = (a[0] + i, a[1] * slope * i)
        if new_position != other and new_position in asteroids:
            return False
    return True


def can_see(a, other, asteroids):
    assert a != other
    if a[1] == other[1]:  # on the same horizontal line
        y = a[1]
        x_coords = sorted([a[0], other[0]])
        for x in range(x_coords[0] + 1, x_coords[1]):
            if (x, y) in asteroids:
                return False
    elif a[0] == other[0]:   # on the same vertical line
        x = a[0]
        y_coords = sorted([a[1], other[1]])
        for y in range(y_coords[0] + 1, y_coords[1]):
            if (x, y) in asteroids:
                return False
    else:  # some kind of slope involved
        rise = other[1] - a[1]
        run = other[0] - a[0]
        slope = rise / run
        if a[0] < other[0]:
            left = a
            right = other
        else:
            left = other
            right = a
        for x in range(left[0] + 1, right[0]):
            current_run = x - left[0]
            y = (slope * current_run) + left[1]
            if (x, y) in asteroids:
                return False

    return True


def get_visible_asteroids(a, asteroids):
    visible_set = set()
    for other in asteroids:
        if a == other:
            continue
        if can_see(a, other, asteroids):
            visible_set.add(other)

    return visible_set


def find_best_asteroid(lines):
    asteroids = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                asteroids.add((x, y))
    those_visible = {}
    for a in asteroids:
        those_visible[a] = get_visible_asteroids(a, asteroids)

    sorted_asteroids = sorted([(c, len(v)) for c, v in those_visible.items()], key=lambda t: t[1], reverse=True)
    return sorted_asteroids[0]


if __name__ == '__main__':
    with open('data/input10.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(find_best_asteroid(lines))
