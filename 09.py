# Day 9: All in a Single Night
import itertools

def calculate_distance(combo, nodes_and_distances):
    distance = 0
    for first, second in zip(combo, combo[1:]):
        distance += nodes_and_distances[first][second]
    return distance


with open('inputs/input09') as input_file:
    star_distances = input_file.readlines()

stars_and_distances = {}
STARS = set()
for line in star_distances:
    names, distance = line.strip().split(' = ')
    first, second = names.split(' to ')
    distance = int(distance)
    if first in stars_and_distances:
        stars_and_distances[first][second] = distance
    else:
        stars_and_distances[first] = {second: distance}
    if second in stars_and_distances:
        stars_and_distances[second][first] = distance
    else:
        stars_and_distances[second] = {first: distance}
    STARS |= {first, second}



all_distances = [calculate_distance(combo, stars_and_distances) for combo in itertools.permutations(STARS)]
part_1, part_2 = min(all_distances), max(all_distances)
print(f'Shortest distance is {part_1}, longest distance is {part_2}!')
# Shortest distance is 207, longest distance is 804!
