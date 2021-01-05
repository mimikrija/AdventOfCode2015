# Day 17: No Such Thing as Too Much
import itertools

LITERS = 150
CONTAINERS = (5, 5, 10, 15, 20)
FACTOR_RANGES = [range(0, LITERS//container + 1) for container in CONTAINERS]



combos = (combo for combo in itertools.product(*FACTOR_RANGES))

counter = 0
for combo in combos:
    if sum(container * factor for container, factor in zip(CONTAINERS, combo)) == LITERS:
        print(combo)
        counter += 1


print(counter) # 2724 too high