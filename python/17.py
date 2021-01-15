# Day 17: No Such Thing as Too Much
import itertools

with open('inputs/input17') as input_file:
    input_containers = input_file.readlines()

CONTAINERS = tuple(int(num) for num in input_containers)
LITERS = 150
#LITERS = 25
#CONTAINERS = (5, 5, 10, 15, 20)

all_valid_combos = [combo for n in range(2, len(CONTAINERS)+1) for combo in itertools.combinations(CONTAINERS, n) if sum(combo) == LITERS]
part_1 = len(all_valid_combos)

print(f'There are {part_1} possible container combinations to fit {LITERS} liters of eggnog!')
# There are 1638 possible container combinations to fit 150 liters of eggnog!


# because of the way all_valid_combos is generated, it is actually already sorted on combo length
min_num_of_containers_used = len(all_valid_combos[0])

combos_with_min_number_of_containers = list(filter(lambda x: len(x) == min_num_of_containers_used, all_valid_combos))
part_2 = len(combos_with_min_number_of_containers)

print(f'There are {part_2} possible combinations that use a minimal number of containers ({min_num_of_containers_used})!')
# There are 17 possible combinations that use a minimal number of containers (4)!
