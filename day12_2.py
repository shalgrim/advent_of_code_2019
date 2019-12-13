import logging
import sys
from collections import Counter
from logging import StreamHandler
from math import pow

from day12_1 import run_time
from moon import Moon

logger = logging.getLogger('advent_of_code_2019.day12_2')
logging.basicConfig(
    filename='day12_2.log',
    level=logging.INFO,
    format='%(levelname) -10s %(asctime)s %(module)s at line %(lineno)d: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger.addHandler(StreamHandler(sys.stdout))

KNOWN_PRIMES = []
KNOWN_PRIME_FACTORIZATIONS = {}


def convert_moons_to_states(moons):
    states = []
    for i in range(3):
        states.append(
            [moon.position[i] for moon in moons] + [moon.velocity[i] for moon in moons]
        )

    x_state = tuple(states[0])
    y_state = tuple(states[1])
    z_state = tuple(states[2])
    return x_state, y_state, z_state


def prime_generator(n):
    global KNOWN_PRIMES
    i = 1
    while i < n:
        i += 1
        primes_to_check = [kp for kp in KNOWN_PRIMES if kp <= i/2]
        for prime in primes_to_check:
            if i % prime == 0:
                break
        else:
            KNOWN_PRIMES.append(i)
            yield i


def find_smallest_prime(n):
    pg = prime_generator(n)
    for prime in pg:
        if n % prime == 0:
            return prime


def get_prime_factorization(n):  #, factors=None):
    global KNOWN_PRIME_FACTORIZATIONS
    # if factors is None:
    #     factors = []

    if n == 1:
        return []

    if n in KNOWN_PRIME_FACTORIZATIONS:
        return KNOWN_PRIME_FACTORIZATIONS[n]
    smallest_prime = find_smallest_prime(n)
    reduced = n // smallest_prime
    # factors.append(smallest_prime)
    answer = [smallest_prime] + get_prime_factorization(reduced)
    # new_factors = factors + [smallest_prime] if factors else [smallest_prime]
    # answer = get_prime_factorization(reduced, factors)
    KNOWN_PRIME_FACTORIZATIONS[n] = answer
    return answer


def least_common_multiple(numbers):
    prime_factorizations = [get_prime_factorization(n) for n in numbers]
    counters = [Counter(pf) for pf in prime_factorizations]
    all_factors = set(counters[0].keys()).union(set(counters[1].keys()).union(set(counters[2].keys())))
    most_used = {}
    for factor in all_factors:
        most_used[factor] = max([c.get(factor, 0) for c in counters])

    answer = 1
    for k, v in most_used.items():
        answer *= (pow(k, v))

    return answer


def get_cycle_times(moons):
    initial_states = convert_moons_to_states(moons)
    cycle_times = [None, None, None]
    moons = run_time(moons, 1)
    steps = 1
    current_states = convert_moons_to_states(moons)

    while not all(cycle_times):
        for i in range(3):
            if not cycle_times[i] and current_states[i] == initial_states[i]:
                cycle_times[i] = steps
        moons = run_time(moons, 1)
        steps += 1
        current_states = convert_moons_to_states(moons)

    return cycle_times


def main(moons):
    cycle_times = get_cycle_times(moons)
    return least_common_multiple(cycle_times)

# so
# x goes around every 161428 steps
# y goes around every 231614 steps
# z goes around every 108344 steps
# and...when do those converge?
# 4050872168304448...but that's too high
# consider 6, 9, and 15
# 6 * 9 * 15 = 810
# but they'd converge first at 90
# 90/6 = 15
# 90/9 = 10
# 90/15 = 6
# 6: 1, 2, 3, 6
# 9: 1, 3, 9
# 15: 1, 3, 5, 15
# least common multiples https://www.calculatorsoup.com/calculators/math/lcm.php
# GCF = 3
# (6 * 9 * 15) / 3 =
# prime factors:
# 6: 2, 3
# 9: 3, 3
# 15: 3, 5
# answer = 2 * 3 * 3 * 5


if __name__ == '__main__':
    moons = [
        Moon(-9, 10, -1),
        Moon(-14, -8, 14),
        Moon(1, 5, 6),
        Moon(-19, 7, 8),
    ]
    print(main(moons))  # 231614 is too low
