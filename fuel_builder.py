def can_produce(rule, resources):
    for ing, num in rule.lhs.items():
        if resources[ing] < num:
            return False
    return True


class BuilderUtils:
    def __init__(self, rules, resources):
        self.rules = rules
        self.resources = resources if resources else {}

    def find_missing_ingredient(self, output_rule):
        lhs = output_rule.lhs
        for ingredient, num_required in lhs.items():
            if self.resources.get(ingredient, 0) < num_required:
                return ingredient
        return None


class FuelBuilder(BuilderUtils):
    def __init__(self, rules, initial_resources=None):
        super().__init__(rules, initial_resources)
        self.num_inputs_produced = 0

    def calc_min_to_produce_one(self, input_ingredient='ORE', output_ingredient='FUEL'):
        """also returns leftovers"""
        # magic happens
        output_rule = self.rules[output_ingredient]
        missing_ingredient = self.find_missing_ingredient(output_rule)

        while missing_ingredient:
            if missing_ingredient == input_ingredient:
                total_needed = output_rule.lhs[missing_ingredient]
                new_inputs_needed = output_rule.lhs[input_ingredient] - self.resources.get(input_ingredient, 0)
                self.resources[input_ingredient] = total_needed
                self.num_inputs_produced += new_inputs_needed
            else:
                self.calc_min_to_produce_one(input_ingredient, missing_ingredient)

            missing_ingredient = self.find_missing_ingredient(output_rule)

        try:
            self.resources[output_ingredient] += output_rule.num_produced
        except KeyError:
            self.resources[output_ingredient] = output_rule.num_produced
        for ing, num in output_rule.lhs.items():
            self.resources[ing] -= num

        return self.num_inputs_produced, self.resources


class MaxIngredientBuilder(BuilderUtils):
    def __init__(self, rules, initial_resources=None):
        super().__init__(rules, initial_resources)
        self.short_on_ore = False

    def produce_ingredient(self, ingredient):
        rule = self.rules[ingredient]
        while not can_produce(rule, self.resources):
            short_ingredient = self.find_missing_ingredient(rule)
            if short_ingredient == 'ORE':
                self.short_on_ore = True
                return
            self.produce_ingredient(short_ingredient)
        self.resources[ingredient] += rule.num_produced
        for ing, num in rule.lhs.items():
            self.resources[ing] -= num

    def produce_max(self, output_ingredient='FUEL'):
        if output_ingredient == 'ORE':
            raise Exception('should never try to produce max ORE')

        output_rule = self.rules[output_ingredient]
        short_ingredient = None

        while not self.short_on_ore:
            short_ingredient = self.find_missing_ingredient(output_rule)
            if short_ingredient:
                self.produce_ingredient(short_ingredient)
            else:
                self.resources[output_ingredient] += output_rule.num_produced
                for ing, num in output_rule.lhs.items():
                    self.resources[ing] -= num
