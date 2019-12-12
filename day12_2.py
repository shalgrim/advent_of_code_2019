import logging
from datetime import datetime
from collections import Counter

from day12_1 import run_time
from moon import Moon

# import sys
# from logging import StreamHandler

logger = logging.getLogger('advent_of_code_2019.day12_2')
logging.basicConfig(
    filename='day12_2.log',
    level=logging.INFO,
    format='%(levelname) -10s %(asctime)s %(module)s at line %(lineno)d: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
# logger.addHandler(StreamHandler(sys.stdout))


def convert_moons_to_states(moons):
    state = [(tuple(moon.position), tuple(moon.velocity)) for moon in moons]
    return tuple(state)


ONE_MILLION = 1_000_000


def main(moons):
    state = convert_moons_to_states(moons)
    states = set()
    steps = 0
    print(datetime.now(), 0)

    while state not in states:
        logger.info(f'{state=}, {steps=}')
        states.add(state)
        moons = run_time(moons, 1)
        steps += 1
        state = convert_moons_to_states(moons)
        if steps % ONE_MILLION == 0:
            print(datetime.now(), steps // ONE_MILLION, 'M')

    return steps


if __name__ == '__main__':
    moons = [
        Moon(-9, 10, -1),
        Moon(-14, -8, 14),
        Moon(1, 5, 6),
        Moon(-19, 7, 8),
    ]
    print(main(moons))
