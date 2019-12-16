from day14_1 import Rule

resources = {'ORE': 1_000_000_000_000}


def find_missing_ingredient(rule):
    global resources
    lhs = rule.lhs
    for ingredient, required in lhs.items():
        if resources.get(ingredient, 0) < required:
            return ingredient
    return None


def produce_max_fuel(output_ingredient, rules, ore_requirement):
    global resources
    output_rule = rules[output_ingredient]

    while resources['ORE'] >= ore_requirement:
        missing_ingredient = find_missing_ingredient(output_rule)
        if missing_ingredient:
            produce_max_fuel(missing_ingredient, rules, ore_requirement)
        else:
            try:
                resources[output_ingredient] += output_rule.num_produced
            except KeyError:
                resources[output_ingredient] = output_rule.num_produced
            for ing, num in output_rule.lhs.items():
                resources[ing] -= num

            if output_ingredient != 'FUEL':
                return


def main(lines, ore_requirement):
    global resources
    resources = {'ORE': 1_000_000_000_000}
    rules = [Rule(line) for line in lines]
    rules = {rule.output: rule for rule in rules}
    produce_max_fuel('FUEL', rules, ore_requirement)
    return resources['FUEL']


if __name__ == '__main__':
    with open('data/input14.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines, 870051))
