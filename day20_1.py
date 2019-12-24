import math
import re
from collections import defaultdict


class Map(object):
    def __init__(self, lines):
        self.portals = defaultdict(list)
        self.walls = set()
        self.passages = set()
        self.build_map(lines)
        self.start = self.portals['AA'][0]
        self.end = self.portals['ZZ'][0]
        self.distances = defaultdict(lambda: math.inf)
        self.portal_travel = {}

        for k, v in self.portals.items():
            if k in ('AA', 'ZZ'):
                continue
            self.portal_travel[v[0]] = v[1]
            self.portal_travel[v[1]] = v[0]

    def calc_all_distances(self, location=None, current_distance=0):
        if location is None:
            location = self.start

        if (
            self.distances[location] <= current_distance
        ):  # I've already been here and at least as short
            return
        self.distances[location] = current_distance

        north = location[0], location[1] - 1
        south = location[0], location[1] + 1
        east = location[0] + 1, location[1]
        west = location[0] - 1, location[1]
        # portal = ... figure this out
        directions = [north, south, east, west]  # add portal

        for direction in [d for d in directions if d in self.passages]:
            self.calc_all_distances(direction, current_distance + 1)

        if location in self.portal_travel:
            self.calc_all_distances(self.portal_travel[location], current_distance + 1)

    def display(self):
        lines = []
        max_x = max(w[0] for w in self.walls)
        max_y = max(w[1] for w in self.walls)

        for y in range(max_y+1):
            line = []
            for x in range(max_x+1):
                if (x, y) in self.walls:
                    line.append('#')
                elif (x, y) in self.distances:
                    val = self.distances[(x,y)]
                    if val < 10:
                        line.append(str(val))
                    elif val % 10 == 0:
                        line.append(str(val // 10))
                    else:
                        line.append(str(val % 10))
                else:
                    line.append(' ')
            lines.append(''.join(line))
        for line in lines:
            print(line)

    def build_map(self, lines):
        horizontal_label = re.compile('[A-Z]{2}')
        vertical_label = re.compile('(?<![A-Z])[A-Z](?![A-Z])')

        for y, line in enumerate(lines[:-1]):
            for x, c in enumerate(line):
                if c == '#':
                    self.walls.add((x, y))
                elif c == '.':
                    self.passages.add((x, y))
            for hl in horizontal_label.findall(line):
                label_start = line.find(hl)
                if label_start == 0:
                    self.portals[hl].append((2, y))
                elif label_start == len(line) - 2:
                    self.portals[hl].append((len(line) - 3, y))
                else:
                    if line[label_start - 1] == '.':
                        self.portals[hl].append((label_start - 1, y))
                    else:
                        self.portals[hl].append((label_start + 2, y))

            vertical_labels = [
                (m.group(), m.start()) for m in vertical_label.finditer(line)
            ]
            for txt, x in vertical_labels:
                if y == 0:
                    self.portals[txt + lines[y + 1][x]].append((x, 2))
                elif (
                    ord('A') <= ord(lines[y - 1][x]) <= ord('Z')
                ):  # processed last time through
                    pass
                else:
                    if y == len(lines) - 2:
                        portal_y = len(lines) - 3
                        self.portals[txt + lines[y + 1][x]].append((x, y - 1))
                    elif lines[y + 2][x] == '.':
                        self.portals[txt + lines[y + 1][x]].append((x, y + 2))
                    else:
                        self.portals[txt + lines[y + 1][x]].append((x, y - 1))


if __name__ == '__main__':
    with open('data/test20_1.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    map = Map(lines)
    map.calc_all_distances()
    map.display()
    with open('data/test20_2.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    map = Map(lines)
    map.calc_all_distances()
    map.display()
    with open('data/input20.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    map = Map(lines)
    try:
        map.calc_all_distances()  # max recursion depth?
    except Exception:
        pass
    print(map.distances[map.end])  # 580 is correct
