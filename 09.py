# Day 9: All in a Single Night

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
