from copy import copy

from day14_1 import Rule

out_of_ore_sentinel = False

def find_short_ingredient(rule, resources):
    lhs = rule.lhs
    for ingredient, required in lhs.items():
        available = resources.get(ingredient, 0)
        needed = required - available
        if needed > 0:
            return ingredient, needed
    return None, 0


def can_produce(rule, resources):
    for ing, num in rule.lhs.items():
        if resources[ing] < num:
            return False
    return True


def produce_ingredient(ingredient, rules, resources):
    global out_of_ore_sentinel
    print(f'producing {ingredient}')
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
            for ing, num in output_rule.lhs.items():
                resources[ing] -= num

    return resources


def main(lines, resources):
    global out_of_ore_sentinel
    out_of_ore_sentinel = False
    rules = [Rule(line) for line in lines]
    rules = {rule.output: rule for rule in rules}
    resources = produce_max_ingredient('FUEL', rules, resources)
    return resources['FUEL']


if __name__ == '__main__':
    with open('data/input14.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))  # , 870051))
