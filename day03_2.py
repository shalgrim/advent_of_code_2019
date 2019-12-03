def get_wire_points_and_steps(wire):
    point_distances = {(0, 0): 0}
    current = (0, 0)
    cumulative_distance = 0
    point_distances = {current: cumulative_distance}
    steps = wire.strip().split(',')

    for step in steps:
        direction = step[0]
        num_spaces = int(step[1:])

        if direction == 'R':
            for _ in range(num_spaces):
                current = (current[0]+1, current[1])
                cumulative_distance += 1
                if current not in point_distances:
                    point_distances[current] = cumulative_distance
        elif direction == 'L':
            for _ in range(num_spaces):
                current = (current[0]-1, current[1])
                cumulative_distance += 1
                if current not in point_distances:
                    point_distances[current] = cumulative_distance
        elif direction == 'D':
            for _ in range(num_spaces):
                current = (current[0], current[1]-1)
                cumulative_distance += 1
                if current not in point_distances:
                    point_distances[current] = cumulative_distance
        elif direction == 'U':
            for _ in range(num_spaces):
                current = (current[0], current[1]+1)
                cumulative_distance += 1
                if current not in point_distances:
                    point_distances[current] = cumulative_distance
        else:
            raise Exception(f'What direction {direction}')

    return point_distances


def find_least_distance_intersection(wire1, wire2):
    pd1 = get_wire_points_and_steps(wire1)
    pd2 = get_wire_points_and_steps(wire2)
    common_points = set(pd1.keys()).intersection(set(pd2.keys()))
    combined_distances = {}

    for cp in common_points:
        if pd1[cp] + pd2[cp]:
            combined_distances[cp] = pd1[cp] + pd2[cp]

    return min(combined_distances.values())


if __name__ == '__main__':
    with open('data/input03.txt') as f:
        lines = f.readlines()

    print(find_least_distance_intersection(lines[0], lines[1]))

