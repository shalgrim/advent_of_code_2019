from collections import defaultdict


class Map(object):
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.keys = {}
        self.doors = {}
        self.door_adjacent = defaultdict(set)
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
                    self.door_adjacent[c].add((loc[0] - 1, loc[1]))
                    self.door_adjacent[c].add((loc[0] + 1, loc[1]))
                    self.door_adjacent[c].add((loc[0], loc[1] - 1))
                    self.door_adjacent[c].add((loc[0], loc[1] + 1))
                    # keep changing my mind on how I want to do it
                    # self.door_adjacent[(loc[0]-1, loc[1])].add(c)
                    # self.door_adjacent[(loc[0]+1, loc[1])].add(c)
                    # self.door_adjacent[(loc[0], loc[1]-1)].add(c)
                    # self.door_adjacent[(loc[0], loc[1]+1)].add(c)

    def reachable(self):
        """do a depth-first walking search"""
        reachable = {self.me: 0}
        return self._reachable(self.me, reachable, 1)

    def _reachable(self, scout, reachable, distance):
        north = scout[0], scout[1] - 1
        south = scout[0], scout[1] + 1
        east = scout[0] + 1, scout[1]
        west = scout[0] - 1, scout[1]
        directions = [north, east, south, west]
        unreachables = self.walls.union(set(list(self.doors.values())))

        for direction in directions:
            if direction in unreachables:
                continue
            else:
                reachable[direction] = (
                    distance
                    if direction not in reachable
                    else min(reachable[direction], distance)
                )

        return reachable

    @property
    def reachable_keys(self, reachables=None):
        if reachables is None:
            reachables = self.reachable()

        return {k: v for k, v in self.keys.items() if v in reachables.keys()}

    @property
    def reachable_doors(self, reachables=None):
        if reachables is None:
            reachables = self.reachable()

        return {
            k: v.intersection(reachables.keys())
            for k, v in self.door_adjacent.items()
            if v.intersection(reachables.keys())
        }

    def reachable_unlockable_doors(self, reachables=None):
        raise NotImplementedError


def calc_fewest_steps_to_all_keys(lines):
    map = Map(lines)


if __name__ == '__main__':
    with open('data/input18.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(calc_fewest_steps_to_all_keys(lines))
