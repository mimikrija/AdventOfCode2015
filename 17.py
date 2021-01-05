# Day 17: No Such Thing as Too Much
import itertools
from collections import Counter

with open('inputs/input17') as input_file:
    input_containers = input_file.readlines()

CONTAINERS = tuple(int(num) for num in input_containers)
LITERS = 150
#CONTAINERS = (5, 5, 10, 15, 20)

combos = (combo for combo in itertools.product({1,0}, repeat = len(CONTAINERS)))

all_valid_combos = [combo for combo in combos if sum(container * factor for container, factor in zip(CONTAINERS, combo)) == LITERS]
part_1 = len(all_valid_combos)
print(part_1)

min_num_of_containers_used = min(Counter(valid_combo)[1] for valid_combo in all_valid_combos)
combos_with_min_number_of_containers = len([valid_combo for valid_combo in all_valid_combos if Counter(valid_combo)[1] == min_num_of_containers_used])
part_2 = combos_with_min_number_of_containers
print(part_2)
