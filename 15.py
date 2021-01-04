# Day 15: Science for Hungry People

import itertools
from operator import mul
from functools import reduce

def split_properties(in_rest):
    pairs = in_rest.split(', ')
    out_pairs = []
    for pair in pairs:
        prop, value = pair.split(' ')
        out_pairs.append((prop, value))
    return out_pairs


def calculate_cookie_score(in_ingredients, ratios, is_part_2 = False):
    totals = {prop: 0 for prop in PROPERTIES}

    for factor, ingredient in zip(ratios, in_ingredients):
        for prop in totals.keys():
            totals[prop] += factor * ingredient[prop]

    for prop, total in totals.items():
        if total < 0:
            totals[prop] = 0

    if not is_part_2 or (is_part_2 and totals['calories'] == 500):
        return reduce(mul, (total for prop, total in totals.items() if prop != 'calories'))
    else:
        return 0


def get_best_cookie_score(in_ingredients, is_part_2 = False):
    combos = (combo for combo in itertools.permutations(range(1,101), NUM_OF_INGREDIENTS) if sum(combo) == 100)
    return max (calculate_cookie_score(in_ingredients, combo, is_part_2) for combo in combos)


with open('inputs/input15') as input_file:
    ingredients_input = input_file.readlines()

NUM_OF_INGREDIENTS = len(ingredients_input)
ingredients = []

for line in ingredients_input:
    rest = line.strip().split(': ')[1]
    ingredient_properties = {prop: int(value) for prop, value in split_properties(rest)}
    ingredients.append(ingredient_properties)

PROPERTIES = set(ingredients[0].keys())

part_1, part_2 = (get_best_cookie_score(ingredients, is_part_2) for is_part_2 in {False, True})

print(f'Best cookie score is {part_1}!')
# Best cookie score is 222870!

print(f'Best 500-calorie cookie score is {part_2}!')
# Best 500-calorie cookie score is 117936!
