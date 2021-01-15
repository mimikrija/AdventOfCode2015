# Day 24: It Hangs in the Balance

import itertools
from operator import mul
from functools import reduce


def parse_input(in_file):
    with open(in_file) as input_file:
        inputs = input_file.readlines()

    return list(map(int, inputs))


def find_smallest_group(weights, groups):
    target_weight = sum(weights) // groups
    for group_size in range(1, len(weights)-1):
        combos = itertools.permutations(weights, group_size)
        for combo in combos:
            if sum(combo) == target_weight:
                return combo


weights = parse_input('inputs/input24')


part_1, part_2 = (reduce(mul,find_smallest_group(weights, groups)) for groups in {3, 4})
print(f'The cosmic entanglement value for the smallest group if divided into 3 groups is {part_1}!')
print(f'The cosmic entanglement value for the smallest group if divided into 4 groups is {part_2}!')

# The cosmic entanglement value for the smallest group if divided into 3 groups is 10439961859!
# The cosmic entanglement value for the smallest group if divided into 4 groups is 72050269!
