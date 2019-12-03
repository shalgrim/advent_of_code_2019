def get_wire_points(wire):
    points = set([(0, 0)])
    current = (0, 0)
    steps = wire.strip().split(',')

    for step in steps:
        direction = step[0]
        num_spaces = int(step[1:])

        if direction == 'R':
            for _ in range(num_spaces):
                current = (current[0]+1, current[1])
                points.add(current)
        elif direction == 'L':
            for _ in range(num_spaces):
                current = (current[0]-1, current[1])
                points.add(current)
        elif direction == 'D':
            for _ in range(num_spaces):
                current = (current[0], current[1]-1)
                points.add(current)
        elif direction == 'U':
            for _ in range(num_spaces):
                current = (current[0], current[1]+1)
                points.add(current)
        else:
            raise Exception(f'What direction {direction}')

    return points


def manhattan_distance(p1, p2):
    x_dist = abs(p1[0] - p2[0])
    y_dist = abs(p1[1] - p2[1])
    return x_dist + y_dist


def find_closest_intersection(wire1, wire2):
    points1 = get_wire_points(wire1)
    points2 = get_wire_points(wire2)
    common_points = points1.intersection(points2)
    distances = [manhattan_distance(cp, (0, 0)) for cp in common_points]
    distances = [d for d in distances if d]
    return min(distances)


if __name__ == '__main__':
    with open('data/input03.txt') as f:
        lines = f.readlines()

    print(find_closest_intersection(lines[0], lines[1]))
