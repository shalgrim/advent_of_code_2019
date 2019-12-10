from day03_1 import Wire


def find_least_distance_intersection(wire1, wire2):
    w1 = Wire(wire1)
    w2 = Wire(wire2)
    common_points = w1.point_set.intersection(w2.point_set)
    combined_distances = [
        w1.point_distances[cp] + w2.point_distances[cp]
        for cp in common_points
        if cp != (0, 0)
    ]

    return min(combined_distances)


if __name__ == '__main__':
    with open('data/input03.txt') as f:
        lines = f.readlines()

    print(find_least_distance_intersection(lines[0], lines[1]))
