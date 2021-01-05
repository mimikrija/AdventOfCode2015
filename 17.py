# Day 17: No Such Thing as Too Much
import itertools

with open('inputs/input17') as input_file:
    input_containers = input_file.readlines()

CONTAINERS = tuple(int(num) for num in input_containers)

LITERS = 150
#CONTAINERS = (5, 5, 10, 15, 20)
FACTOR_RANGES = [range(0,2) for container in CONTAINERS]
print(len(CONTAINERS))

combos = (combo for combo in itertools.product(*FACTOR_RANGES))

counter = 0
for combo in combos:
    if sum(container * factor for container, factor in zip(CONTAINERS, combo)) == LITERS:
        print(combo)
        counter += 1


print(counter) # 2724 too high # 609 too low