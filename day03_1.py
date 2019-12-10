class Wire(object):
    def __init__(self, path_string):
        self.point_distances = {(0, 0): 0}
        self.cumulative_distance = 0
        self._build(path_string)

    def _build(self, path_string):
        current = (0, 0)
        steps = path_string.strip().split(',')

        for step in steps:
            current = self.process_step(step, current)

    def process_step(self, step, current):
        direction = step[0]
        num_steps = int(step[1:])
        next_step = current

        for _ in range(num_steps):
            next_step = Wire.apply_direction(direction, next_step)
            self.cumulative_distance += 1
            if next_step not in self.point_distances:
                self.point_distances[next_step] = self.cumulative_distance

        return next_step

    @staticmethod
    def apply_direction(direction, step):
        if direction == 'R':
            return step[0] + 1, step[1]
        elif direction == 'L':
            return step[0] - 1, step[1]
        elif direction == 'U':
            return step[0], step[1] + 1
        elif direction == 'D':
            return step[0], step[1] - 1
        else:
            raise Exception(f'Unknown {direction=}')

    @property
    def point_set(self):
        return set(self.point_distances.keys())


def get_wire_points(wire):
    points = set([(0, 0)])
    current = (0, 0)
    steps = wire.strip().split(',')

    for step in steps:
        direction = step[0]
        num_spaces = int(step[1:])

        if direction == 'R':
            for _ in range(num_spaces):
                current = (current[0] + 1, current[1])
                points.add(current)
        elif direction == 'L':
            for _ in range(num_spaces):
                current = (current[0] - 1, current[1])
                points.add(current)
        elif direction == 'D':
            for _ in range(num_spaces):
                current = (current[0], current[1] - 1)
                points.add(current)
        elif direction == 'U':
            for _ in range(num_spaces):
                current = (current[0], current[1] + 1)
                points.add(current)
        else:
            raise Exception(f'What direction {direction}')

    return points


def manhattan_distance(p1, p2):
    x_dist = abs(p1[0] - p2[0])
    y_dist = abs(p1[1] - p2[1])
    return x_dist + y_dist


def find_closest_intersection(wire1, wire2):
    w1 = Wire(wire1)
    w2 = Wire(wire2)
    common_points = w1.point_set.intersection(w2.point_set)
    distances = [manhattan_distance(cp, (0, 0)) for cp in common_points if cp != (0, 0)]
    return min(distances)


if __name__ == '__main__':
    with open('data/input03.txt') as f:
        lines = f.readlines()

    print(find_closest_intersection(lines[0], lines[1]))
