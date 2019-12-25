import logging
import sys
from collections import defaultdict
from copy import deepcopy
from logging import StreamHandler

logger = logging.getLogger('advent_of_code_2019.day18_1')
logging.basicConfig(
    filename='day18_1.log',
    level=logging.INFO,
    format='%(levelname) -10s %(asctime)s %(module)s at line %(lineno)d: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger.addHandler(StreamHandler(sys.stdout))


known_shortest = None
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
        # print(f'picked up key {k}')

    def unlock_door(self):
        for k, v in self.doors.items():
            if self.me == v:
                break
        del self.doors[k]
        # print(f'unlocked door {k}')

    def process_move(self, move_to):
        self.me = move_to
        if self.me in self.keys.values():
            self.pick_up_key()
        elif self.me in self.doors.values():
            self.unlock_door()
        # logger.info(f'{len(self.keys)=}, {len(self.doors)=}')


def generate_new_maps(old_map, incoming_distance):
    new_maps = []
    reachables = old_map.reachable()
    moves = old_map.get_available_moves(reachables)
    for move_to, step_distance in moves.items():
        new_map = deepcopy(old_map)
        new_map.process_move(move_to)
        new_maps.append((new_map, incoming_distance + step_distance))
    return new_maps


def reduce_maps(maps):
    rv = []
    seen_states = set()
    for m, d in maps:
        if m.state in seen_states:
            continue
        seen_states.add(m.state)
        rv.append((m, d))

    return rv


def bfs(start_map):
    maps = [(deepcopy(start_map), 0)]
    i = 0

    while not any(mt[0].got_all_keys for mt in maps):
        i += 1
        logger.info(
            f'going around while {i}th time: {len(maps)} maps, {len(maps[0][0].keys) + len(maps[0][0].doors)} keys and doors'
        )
        new_maps = []
        for m, d in maps:
            new_maps += generate_new_maps(m, d)

        maps = reduce_maps(new_maps)

    return min([d for m, d in maps if m.got_all_keys])
    # for m, d in maps:
    #
    #     if m.got_all_keys:
    #         return d


def calc_fewest_steps_to_all_keys(old_map, cumulative_distance=0):
    global known_state_distances, known_shortest
    if not cumulative_distance and known_shortest:
        known_shortest = None
    # print(f'{cumulative_distance=}')

    if old_map.got_all_keys:
        logger.info(f'found path of {cumulative_distance}')

        if not known_shortest or known_shortest > cumulative_distance:
            known_shortest = cumulative_distance
            logger.info(f'new {known_shortest=}')

        return 0

    if old_map.state in known_state_distances:
        full_path_length = cumulative_distance + known_state_distances[old_map.state]
        logger.info(f'found path of {full_path_length}')

        if not known_shortest or known_shortest > full_path_length:
            known_shortest = full_path_length
            logger.info(f'new {known_shortest=}')

        return known_state_distances[old_map.state]

    reachables = old_map.reachable()
    moves = old_map.get_available_moves(reachables)

    distances_by_move = {}

    for move_to, step_distance in moves.items():
        if known_shortest and cumulative_distance + step_distance > known_shortest:
            continue
        map = deepcopy(old_map)
        map.process_move(move_to)
        that_moves_fewest_steps = calc_fewest_steps_to_all_keys(
            map, cumulative_distance + step_distance
        )
        if that_moves_fewest_steps == 'unknown':
            continue
        distances_by_move[move_to] = that_moves_fewest_steps + step_distance

    if distances_by_move:
        fewest_steps_from_here = min(distances_by_move.values())
        known_state_distances[old_map.state] = fewest_steps_from_here
    else:
        fewest_steps_from_here = 'unknown'

    return fewest_steps_from_here


def main(lines):
    map = Map(lines)
    known_state_distances.clear()
    return calc_fewest_steps_to_all_keys(map)


if __name__ == '__main__':
    with open('data/input18.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    # logger.info(main(lines))  # 7698 too high. other non-correct: 7678, 7624, 5942
    # really tho this needs to be converted to a BFS
    map = Map(lines)
    print(bfs(map))
