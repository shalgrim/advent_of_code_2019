"""
Going to bed idea
Keep track of how much input_ingredient you used, since that's always magically created
Try to run the rule giving you the output you want with available resources
If all the ingredients are there in the necessary quantity, run it
If not, run a rule to produce an ingredient you're short on...note that this will update available resources
Yep, that's the way to do it
All input ingredient then is the resource you track
Other than that it's just: Do I have all the ingredients to run this rule?
"""

import math
from copy import copy
import itertools


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


# def get_required(input_ingredient, output_ingredient, num_needed, rules):
#     input_production_rules = [v for k, v in rules.items() if input_ingredient in v.lhs]
#
#     direct_rules = [
#         ipr for ipr in input_production_rules if ipr.output == output_ingredient
#     ]
#     if direct_rules:
#         rule = direct_rules[0]
#         return rule.lhs[input_ingredient] * math.ceil(num_needed / rule.num_produced)
#
#     # if any(ipr.output == output_ingredient for ipr in input_production_rules):
#     #     rule = [ipr for ipr in input_production_rules if ]
#
#     answer = 0
#     for ipr in input_production_rules:
#         num_times_to_run_rule = math.ceil(
#             get_required(ipr.output, output_ingredient, num_needed, rules)
#             / ipr.num_produced
#         )
#         answer += ipr.lhs[input_ingredient] * num_times_to_run_rule
#     return answer
#

# def get_required(input_ingredient, output_ingredient, num_needed, rules):
#     # next try reducing as much as possible
#     if input_ingredient == output_ingredient:
#         return num_needed
#
#     rule = rules[output_ingredient]
#
#     if input_ingredient in rule.lhs:
#         return rule.lhs[input_ingredient] * math.ceil(num_needed / rule.num_produced)
#
#     # assume two input ingredients
#     ingredient_item_list = list(rule.lhs.items())
#     ing1, needed1 = ingredient_item_list[0]
#     ing2, needed2 = ingredient_item_list[1]
#     if does_produce(ing1, ing2, rules):
#         num_ing1_needed_to_produce_ing2 = get_required(ing1, ing2, needed2, rules)
#         total_ing1_needed = needed1 + num_ing1_needed_to_produce_ing2
#         return get_required(
#             input_ingredient, ing1, total_ing1_needed * math.ceil(num_needed / rule.num_produced), rules
#         ) + get_required(input_ingredient, ing2, needed2, rules)
#     elif does_produce(ing2, ing1, rules):
#         num_ing2_needed_to_produce_ing1 = get_required(ing2, ing1, needed1, rules)
#         total_ing2_needed = needed2 + num_ing2_needed_to_produce_ing1
#         return get_required(
#             input_ingredient, ing2, total_ing2_needed * math.ceil(num_needed / rule.num_produced), rules
#         )
#     else:
#         return get_required(
#             input_ingredient, ing1, needed1 * math.ceil(num_needed / rule.num_produced), rules
#         ) + get_required(
#             input_ingredient, ing2, needed2 * math.ceil(num_needed / rule.num_produced), rules
#         )
#
#     # intermediate_ingredients = copy(rule.lhs)
#     # for perm in itertools.permutations(rule.lhs.items(), 2):
#     #     ing_a, needed_a = perm[0]
#     #     ing_b, needed_b = perm[1]
#     #     if does_produce(ing_a, ing_b, rules):
#     #         intermediate_ingredients[ing_a] += get_required(ing_a, ing_b, math.ceil(num_needed / needed_b), rules)
#     #         del intermediate_ingredients[ing_b]
#     #
#     # answer = 0
#     # for ii, nn in intermediate_ingredients.items():
#     #     answer += get_required(ii, output_ingredient, math.ceil(num_needed / nn), rules)
#     #
#     # return answer
#

# def get_required(input_ingredient, output_ingredient, num_needed, rules):
#     if input_ingredient == output_ingredient:
#         return num_needed
#
#     try:
#         rule = rules[output_ingredient]
#     except KeyError:
#         return 0
#
#     # if input_ingredient in rule.lhs:
#     #     times_to_run_rule = math.ceil(num_needed / rule.num_produced)
#     #     input_needed_per_run = rule.lhs[input_ingredient]
#     #     answer = times_to_run_rule * input_needed_per_run
#     #     TODO: recurse
#     #
#     # else:
#
#     answer = 0
#
#     for ingredient, quantity in rule.lhs.items():
#         answer += get_required(
#             input_ingredient,
#             ingredient,
#             quantity * math.ceil(num_needed / rule.num_produced),
#             rules,
#         )
#
#     return answer

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

    print(main(lines))
    print(resources)
