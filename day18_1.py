import math
from collections import defaultdict
from copy import deepcopy


# known_shortest = None
known_state_distances = {}


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

    @property
    def state(self):
        return self.me, frozenset(self.keys.keys()), frozenset(self.doors.keys())

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

    def get_available_moves(self, reachables=None):
        if not reachables:
            reachables = self.reachable()

        answer = {}
        for k, v in self.reachable_keys(reachables).items():
            answer[v] = reachables[v]

        for k, v in self.reachable_unlockable_doors(reachables).items():
            adjacent_spots = self.reachable_doors(reachables)[k]
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
        print(f'{len(self.keys)=}, {len(self.doors)=}')


def calc_fewest_steps_to_all_keys(old_map, cumulative_distance=0):
    global known_state_distances
    print(f'{cumulative_distance=}')

    if known_state_distances and cumulative_distance > min(known_state_distances.values()):
        return math.inf

    if old_map.got_all_keys:
        print(f'found path of {cumulative_distance}')
        return 0

    if old_map.state in known_state_distances:
        print(f'found path of {cumulative_distance+known_state_distances[old_map.state]}')
        return known_state_distances[old_map.state]

    # # this is the timesaver supposedly breakpoint but it breaks the test so...
    # if known_shortest and cumulative_distance > known_shortest:
    #     return known_shortest + 1

    reachables = old_map.reachable()
    moves = old_map.get_available_moves(reachables)

    distances_by_move = {}

    for move_to, step_distance in moves.items():
        map = deepcopy(old_map)
        map.process_move(move_to)
        distances_by_move[move_to] = step_distance + calc_fewest_steps_to_all_keys(
            map, cumulative_distance + step_distance
        )

    fewest_steps_from_here = min(distances_by_move.values())
    known_state_distances[map.state] = fewest_steps_from_here

    return fewest_steps_from_here


def main(lines):
    map = Map(lines)
    known_state_distances.clear()
    return calc_fewest_steps_to_all_keys(map)


if __name__ == '__main__':
    with open('data/input18.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))  # 7806 too high
