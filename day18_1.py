class Map(object):
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.keys = {}
        self.doors = {}
        self.walls = set()
        self.passages = set()

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                loc = (x, y)

                if c == '#':
                    self.walls.add(loc)
                elif c == '.':
                    self.passages.add(loc)
                elif c == '@':
                    self.me = loc
                elif ord('a') <= ord(c) <= ord('z'):
                    self.keys[c] = loc
                elif ord('A') <= ord(c) <= ord('Z'):
                    self.doors[c] = loc

    def reachable(self):
        """do a depth-first walking search"""
        reachable = set([self.me])  # TODO: turn into a dict where I track distance
        return self._reachable(self.me, reachable)

    def _reachable(self, scout, reachable):
        north = scout[0], scout[1] - 1
        south = scout[0], scout[1] + 1
        east = scout[0] + 1, scout[1]
        west = scout[0] - 1, scout[1]
        directions = [north, east, south, west]
        unreachables = self.walls.union(set(list(self.doors.values())))

        for direction in directions:
            if direction in reachable or direction in unreachables:
                continue
            else:
                reachable.add(direction)
                self._reachable(direction, reachable)

        return reachable


def calc_fewest_steps_to_all_keys(lines):
    map = Map(lines)


if __name__ == '__main__':
    with open('data/input18.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(calc_fewest_steps_to_all_keys(lines))
