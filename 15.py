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

def calculate_cookie_score(in_properties, ratios, is_part_2 = False):
    total_capacity = 0
    total_durability = 0
    total_flavor = 0
    total_texture = 0
    total_calories = 0
    for factor, props in zip(ratios, in_properties.values()):
        total_capacity += factor * props['capacity']
        total_durability += factor * props['durability']
        total_flavor += factor * props['flavor']
        total_texture += factor * props['texture']
        total_calories += factor * props['calories']

    totals = (total if total > 0 else 0 for total in (total_capacity, total_durability, total_flavor, total_texture))

    if not is_part_2 or (is_part_2 and total_calories == 500):
        return reduce(mul, totals)
    else:
        return 0

def get_best_cookie_score(in_properties, is_part_2 = False):
    combos = (combo for combo in itertools.permutations(range(1,101), NUM_OF_INGREDIENTS) if sum(combo) == 100)
    return max (calculate_cookie_score(all_properties, combo, is_part_2) for combo in combos)

with open('inputs/input15') as input_file:
    ingredients_input = input_file.readlines()

NUM_OF_INGREDIENTS = len(ingredients_input)
all_properties = {}

for line in ingredients_input:
    ingredient, rest = line.strip().split(': ')
    properties = {prop: int(value) for prop, value in split_properties(rest)}
    all_properties[ingredient] = properties


part_1, part_2 = (get_best_cookie_score(all_properties, is_part_2) for is_part_2 in {False, True})

print(f'Best cookie score is {part_1}!')
# Best cookie score is 222870!

print(f'Best 500-calorie cookie score is {part_2}!')
# Best 500-calorie cookie score is 117936!
