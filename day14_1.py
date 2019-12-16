class Rule(object):
    def __init__(self, line):
        lhs, rhs = line.split('=>')
        lhs = [l.strip().split() for l in lhs.strip().split(',')]
        self.lhs = {t[1]: int(t[0]) for t in lhs}
        self.rhs_ingredient = rhs.strip().split()[1]
        self.rhs_quantity = int(rhs.strip().split()[0])

    @property
    def output(self):
        return self.rhs_ingredient

    @property
    def num_produced(self):
        return self.rhs_quantity


def does_produce(a, b, rules):
    """True if a produces b"""
    if b not in rules:
        return False

    if rules[b].lhs.get(a, False):
        return True
    else:
        return any(does_produce(a, c, rules) for c in rules[b].lhs)


num_inputs_produced = 0
resources = {}


def find_missing_ingredient(rule):
    global resources
    lhs = rule.lhs
    for ingredient, required in lhs.items():
        if resources.get(ingredient, 0) < required:
            return ingredient
    return None


def get_required(input_ingredient, output_ingredient, rules):
    global num_inputs_produced, resources
    output_rule = rules[output_ingredient]

    missing_ingredient = find_missing_ingredient(output_rule)
    while missing_ingredient:
        if missing_ingredient == input_ingredient:
            total_needed = output_rule.lhs[missing_ingredient]
            new_inputs_needed = output_rule.lhs[input_ingredient] - resources.get(input_ingredient, 0)
            resources[input_ingredient] = total_needed
            num_inputs_produced += new_inputs_needed
        else:
            get_required(input_ingredient, missing_ingredient, rules)

        missing_ingredient = find_missing_ingredient(output_rule)

    try:
        resources[output_ingredient] += output_rule.num_produced
    except KeyError:
        resources[output_ingredient] = output_rule.num_produced
    for ing, num in output_rule.lhs.items():
        resources[ing] -= num


def main(lines, input_ingredient='ORE', outupt_ingredient = 'FUEL'):
    global num_inputs_produced, resources
    resources = {}
    num_inputs_produced = 0
    rules = [Rule(line) for line in lines]
    rules = {rule.output: rule for rule in rules}
    get_required('ORE', 'FUEL',  rules)
    return num_inputs_produced


if __name__ == '__main__':
    with open('data/input14.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))  # 870051
    print(resources)
