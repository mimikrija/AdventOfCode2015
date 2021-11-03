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

# 2021 warm-up challenge
def help_santa_out(instructions, extra_helpers=1):
    helpers = 1 + extra_helpers # santa + extras
    helper_instructions = [instructions[start::helpers] for start in range(0, helpers)]
    visited_houses = set()
    for helper in helper_instructions:
        visited_houses |= visit_houses(helper)
    return len(visited_houses)

part_1 = len(visit_houses(eggnogg_instructions))
print(f'The number of houses which receive at least one present is {part_1}!')
# The number of houses which receive at least one present is 2081!

part_2 = help_santa_out(eggnogg_instructions)
print(f'When Robo-Santa helps, the number of houses which receive at least one present is {part_2}!')
# When Robo-Santa helps, the number of houses which receive at least one present is 2341!
