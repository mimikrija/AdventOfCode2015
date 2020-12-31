DIRECTIONS = {
    '>': 1 + 0j,
    '<': -1 + 0j,
    '^': 0 + 1j,
    'v': 0 -1j,
}

with open('inputs/input03') as input_file:
    eggnogg_instructions = input_file.read().strip()

def visit_houses(instructions):
    house = 0 + 0j
    visited_houses = {house}
    for arrow in instructions:
        house += DIRECTIONS[arrow]
        visited_houses.add(house)
    return visited_houses

part_1 = len(visit_houses(eggnogg_instructions))
print(f'The number of houses which receive at least one present is {part_1}!')
# The number of houses which receive at least one present is 2081!

santa_instructions = (instruction for n, instruction in enumerate(eggnogg_instructions) if n%2 == 0)
robo_santa_instructions = (instruction for n, instruction in enumerate(eggnogg_instructions) if n%2 == 1)

part_2 = len(visit_houses(santa_instructions) | visit_houses(robo_santa_instructions))
print(f'When Robo-Santa helps, the number of houses which receive at least one present is {part_2}!')
# When Robo-Santa helps, the number of houses which receive at least one present is 2341!
