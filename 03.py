DIRECTIONS = {
    '>': 1 + 0j,
    '<': -1 + 0j,
    '^': 0 + 1j,
    'v': 0 -1j,
}

with open('inputs/input03') as input_file:
    inputs = input_file.read().strip()

house = 0 + 0j
visited_houses = {house}
for arrow in inputs:
    house += DIRECTIONS[arrow]
    visited_houses.add(house)

part_1 = len(visited_houses)

print(f'The number of houses which recieve at least one present is {part_1}!')
# The number of houses which recieve at least one present is 2081!


