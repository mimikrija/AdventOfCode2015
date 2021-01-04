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



with open('inputs/input15') as input_file:
    ingredients_input = input_file.readlines()

NUM_OF_INGREDIENTS = len(ingredients_input)
all_properties = {}
for line in ingredients_input:
    ingredient, rest = line.strip().split(': ')
    properties = {prop: int(value) for prop, value in split_properties(rest)}
    all_properties[ingredient] = properties


combos = (combo for combo in itertools.permutations(range(1,101), NUM_OF_INGREDIENTS) if sum(combo) == 100)

#print(calculate_cookie_score(all_properties, (44, 56)))

all_scores = (calculate_cookie_score(all_properties, combo) for combo in combos)

print(max(all_scores))