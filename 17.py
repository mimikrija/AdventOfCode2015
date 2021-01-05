# Day 17: No Such Thing as Too Much
import itertools

with open('inputs/input17') as input_file:
    input_containers = input_file.readlines()

CONTAINERS = tuple(int(num) for num in input_containers)
LITERS = 150
#CONTAINERS = (5, 5, 10, 15, 20)


combos = (combo for combo in itertools.product({1,0}, repeat = len(CONTAINERS)))

counter = 0
for combo in combos:
    if sum(container * factor for container, factor in zip(CONTAINERS, combo)) == LITERS:
        counter += 1


print(counter) # 1638