import math
from collections import defaultdict


class Layout(object):
    def __init__(self, lines):
        self.current_state = lines
        self.height = len(lines)
        self.width = len(lines[0])
        self.time = 0
        self.seen_states = defaultdict(set)
        self.seen_states['\n'.join(self.current_state)].add(self.time)

    @property
    def repeated(self):
        return any(len(v) > 1 for k, v in self.seen_states.items())

    def adjacent_bugs(self, x, y):
        adjacent_string = ''
        if y == 0:
            adjacent_string += self.current_state[1][x]
            if x == 0:
                adjacent_string += self.current_state[0][1]
            elif x == self.width - 1:
                adjacent_string += self.current_state[0][x-1]
            else:
                adjacent_string += self.current_state[0][x+1] + self.current_state[0][x-1]
        elif y == self.height - 1:
            adjacent_string += self.current_state[y-1][x]
            if x == 0:
                adjacent_string += self.current_state[y][1]
            elif x == self.width - 1:
                adjacent_string += self.current_state[y][x-1]
            else:
                adjacent_string += self.current_state[y][x+1] + self.current_state[y][x-1]
        else:
            adjacent_string += self.current_state[y-1][x] + self.current_state[y+1][x]
            if x == 0:
                adjacent_string += self.current_state[y][x+1]
            elif x == self.width - 1:
                adjacent_string += self.current_state[y][x-1]
            else:
                adjacent_string += self.current_state[y][x+1] + self.current_state[y][x-1]

        return adjacent_string.count('#')

    def tick(self):
        new_lines = []
        for y in range(self.height):
            line = ''
            for x in range(self.width):
                if self.current_state[y][x] == '#':  # bug
                    if self.adjacent_bugs(x, y) == 1:
                        next_char = '#'
                    else:
                        next_char = '.'
                else:  # empty
                    if self.adjacent_bugs(x, y) in (1, 2):
                        next_char = '#'
                    else:
                        next_char = '.'

                line += next_char
            new_lines.append(line)
        self.current_state = new_lines
        self.time += 1
        self.seen_states['\n'.join(self.current_state)].add(self.time)

    def biodiversity(self):
        exponent = 0
        rv = 0
        for line in self.current_state:
            for char in line:
                if char == '#':
                    rv += int(math.pow(2, exponent))
                exponent += 1
        return rv


if __name__ == '__main__':
    # with open('data/test24_1.txt') as f:
    with open('data/input24.txt') as f:
            lines = [line.strip() for line in f.readlines()]
    layout = Layout(lines)

    while not layout.repeated:
        print()
        print('\n'.join(layout.current_state))
        layout.tick()
    print()
    print('\n'.join(layout.current_state))
    print(layout.biodiversity())
