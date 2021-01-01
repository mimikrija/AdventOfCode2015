# Day 9: All in a Single Night
import itertools

def calculate_distance(combo, nodes_and_distances):
    distance = 0
    for pair in zip(combo, combo[1:]):
        distance += nodes_and_distances[pair]
    return distance


with open('inputs/input09') as input_file:
    star_distances = input_file.readlines()

DISTANCES_BETWEEN_STARS = {}
STARS = set()
for line in star_distances:
    names, distance = line.strip().split(' = ')
    distance = int(distance)
    for star_pair in itertools.permutations(names.split(' to ')):
        DISTANCES_BETWEEN_STARS[star_pair] = distance
    STARS |= set(star_pair)



all_distances = [calculate_distance(combo, DISTANCES_BETWEEN_STARS) for combo in itertools.permutations(STARS)]
part_1, part_2 = min(all_distances), max(all_distances)
print(f'Shortest distance is {part_1}, longest distance is {part_2}!')
# Shortest distance is 207, longest distance is 804!
