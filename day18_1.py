from collections import defaultdict
from copy import deepcopy


class Map(object):
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.keys = {}
        self.doors = {}
        self.door_adjacent = defaultdict(set)
        self.walls = set()
        self.passages = set()
        self.picked_up_keys = set()

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                loc = (x, y)

                if c == '#':
                    self.walls.add(loc)
                elif c == '.':
                    self.passages.add(loc)
                elif c == '@':
                    self.passages.add(loc)
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
            elif direction not in reachable or reachable[direction] > distance:
                reachable[direction] = distance
                self._reachable(direction, reachable, distance + 1)

        return reachable

    def reachable_keys(self, reachables=None):
        if reachables is None:
            reachables = self.reachable()

        return {k: v for k, v in self.keys.items() if v in reachables.keys()}

    def reachable_doors(self, reachables=None):
        if reachables is None:
            reachables = self.reachable()

        return {
            k: v.intersection(reachables.keys())
            for k, v in self.door_adjacent.items()
            if v.intersection(reachables.keys())
        }

    def reachable_unlockable_doors(self, reachables=None):
        return {
            k: v
            for k, v in self.doors.items()
            if k in self.reachable_doors(reachables)
            and chr(ord(k) + 32) in self.picked_up_keys
        }

    @property
    def got_all_keys(self):
        return len(self.keys) == 0

    def get_available_moves(self):
        reachables = self.reachable()
        answer = {}
        for k, v in self.reachable_keys(reachables).items():
            answer[v] = reachables[v]

        for k, v in self.reachable_unlockable_doors(reachables).items():
            adjacent_spots = self.reachable_doors()[k]
            answer[v] = min(reachables[spot] for spot in adjacent_spots) + 1

        return answer

    def pick_up_key(self):
        for k, v in self.keys.items():
            if self.me == v:
                break
        self.picked_up_keys.add(k)
        del self.keys[k]
        print(f'picked up key {k}')

    def unlock_door(self):
        for k, v in self.doors.items():
            if self.me == v:
                break
        del self.doors[k]
        print(f'unlocked door {k}')

    def process_move(self, move_to):
        self.me = move_to
        if self.me in self.keys.values():
            self.pick_up_key()
        elif self.me in self.doors.values():
            self.unlock_door()


def calc_fewest_steps_to_all_keys(old_map):
    moves = old_map.get_available_moves()

    if not moves:
        # must have all keys
        return 0

    distances_by_move = {}

    for move_to, step_distance in moves.items():
        map = deepcopy(old_map)
        map.process_move(move_to)
        distances_by_move[move_to] = step_distance + calc_fewest_steps_to_all_keys(map)

    return min(distances_by_move.values())


def main(lines):
    map = Map(lines)
    return calc_fewest_steps_to_all_keys(map)


if __name__ == '__main__':
    with open('data/input18.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))
