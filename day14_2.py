import time
from collections import defaultdict
from datetime import datetime

from day14_1 import Rule, get_required
from fuel_builder import FuelBuilder, MaxIngredientBuilder, can_produce

ONE_TRILLION = 1_000_000_000_000

out_of_ore_sentinel = False
start_time = time.time()


def find_short_ingredient(rule, resources):
    lhs = rule.lhs
    for ingredient, required in lhs.items():
        available = resources.get(ingredient, 0)
        needed = required - available
        if needed > 0:
            return ingredient, needed
    return None, 0


def produce_ingredient(ingredient, rules, resources):
    global out_of_ore_sentinel
    # print(f'producing {ingredient}')
    rule = rules[ingredient]

    while not can_produce(rule, resources):
        short_ingredient, _ = find_short_ingredient(rule, resources)
        if short_ingredient == 'ORE':
            out_of_ore_sentinel = True
            return resources
        resources = produce_ingredient(short_ingredient, rules, resources)
        if out_of_ore_sentinel:
            return resources

    resources[ingredient] += rule.num_produced
    for ing, num in rule.lhs.items():
        resources[ing] -= num
    return resources


def produce_max_ingredient(output_ingredient, rules, resources):
    global start_time
    if output_ingredient == 'ORE':
        raise Exception('should never try to produce max ORE')

    output_rule = rules[output_ingredient]
    short_ingredient = None

    while not out_of_ore_sentinel:
        short_ingredient, needed = find_short_ingredient(output_rule, resources)
        if short_ingredient:
            resources = produce_ingredient(short_ingredient, rules, resources)
        else:
            resources[output_ingredient] += output_rule.num_produced
            if output_ingredient == 'FUEL' and resources['FUEL'] % 1_000 == 0:
                print(f'current time: {datetime.now().time()}')
                elapsed_time = int(time.time() - start_time)
                m, s = divmod(elapsed_time, 60)
                h, m = divmod(m, 60)
                elapsed_time = f'{h}:{m:02}:{s:02}'
                print(f'{elapsed_time=}')
                fuel_produced = resources['FUEL']
                print(f'FUEL: {fuel_produced:,}')
            for ing, num in output_rule.lhs.items():
                resources[ing] -= num

    return resources


def main_brute_force(lines, resources=None):
    global start_time
    start_time = time.time()
    global out_of_ore_sentinel
    out_of_ore_sentinel = False
    if resources is None:
        resources = defaultdict(lambda: 0)
        resources['ORE'] = ONE_TRILLION

    rules = [Rule(line) for line in lines]
    rules = {rule.output: rule for rule in rules}
    resources = produce_max_ingredient('FUEL', rules, resources)
    return resources['FUEL']


def get_leftovers(final_ingredient, first_ingredient, rules):
    """creates intermediate ingredients leftover when creating a single final_ingredient from the minimum of first_ingredient"""
    # it may be better to incorporate this into get_required
    pass


def multiply_leftovers(leftovers, multiplier):
    """multiples each element in leftovers by num_fuel_easy"""
    new_dict = {}
    for k, v in leftovers.items():
        new_dict[k] = v * multiplier

    return new_dict


def get_required_proper(input_ingredient, output_ingredient, rules, resources=None):
    """Assume infinite resources, we're using that arg to track tho"""
    # TODO: write tests
    if resources is None:
        resources = defaultdict(lambda: 0)
    rule = rules[output_ingredient]
    if input_ingredient in rule.lhs:
        # this seems wrong
        return rule.lhs[input_ingredient] - resources[input_ingredient]
    return 0  # i am tired, i'm not sure where i'm going with this


def main_smarter(lines):
    """I think at this point this algorithm is basically the same as brute force just in a class"""
    rules = [Rule(line) for line in lines]
    rules = {rule.output: rule for rule in rules}
    resources = defaultdict(lambda: 0)
    resources['ORE'] = ONE_TRILLION
    mb = MaxIngredientBuilder(rules, resources)
    mb.produce_max('FUEL')
    return mb.resources['FUEL']
    # return num_output_easy + extra_resources['FUEL']


if __name__ == '__main__':
    with open('data/input14.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main_brute_force(lines))
