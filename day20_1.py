import re
from collections import defaultdict


class Map(object):
    def __init__(self, lines):
        self.portals = Map.find_portals(lines)
        self.start = self.portals['AA'][0]
        self.end = self.portals['ZZ'][0]

    @staticmethod
    def find_portals(lines):
        horizontal_label = re.compile('[A-Z]{2}')
        vertical_label = re.compile('(?<![A-Z])[A-Z](?![A-Z])')

        portals = defaultdict(list)

        for y, line in enumerate(lines[:-1]):
            for hl in horizontal_label.findall(line):
                label_start = line.find(hl)
                if label_start == 0:
                    portals[hl].append((2, y))
                elif label_start == len(line) - 2:
                    portals[hl].append((len(line) - 2, y))
                else:
                    if line[label_start-1] == '.':
                        portals[hl].append((label_start-1, y))
                    else:
                        portals[hl].append((label_start+2, y))

            vertical_labels = vertical_label.findall(line)
            # vertical_labels = [vl for vl in vertical_labels if line.find(vl) not in (0, len(line)-1)]
            vertical_labels = [(m.group(), m.start()) for m in vertical_label.finditer(line)]
            assert len(vertical_labels) == len(set([vl[0] for vl in vertical_labels])), 'This will be trickier'
            for txt, x in vertical_labels:
                if y == 0:
                    portals[txt + lines[y+1][x]].append((x, 2))
                elif ord('A') <= ord(lines[y-1][x]) <= ord('Z'):  # processed last time through
                    pass
                else:
                    if y == len(lines) - 2:
                        portal_y = len(lines) - 3
                        portals[txt + lines[y+1][x]].append((x, y-1))
                    elif lines[y+2][x] == '.':
                        portals[txt + lines[y+1][x]].append((x, y+2))
                    else:
                        portals[txt + lines[y+1][x]].append((x, y-1))

        return portals


if __name__ == '__main__':
    with open('data/test20_1.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
