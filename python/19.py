# Day 19: Medicine for Rudolph

import re

def parse_input(in_file):
    with open(in_file) as input_file:
        reactions, molecule = input_file.read().split('\n\n')
    all_reactions = [tuple(line.split(' => ')) for line in reactions.split('\n')]
    return all_reactions, molecule

def react(reaction, in_molecule):
    left, right = reaction
    positions = [m.start() for m in re.finditer(left, in_molecule)]
    out_molecules = set()
    for pos in positions:
        new_molecule = in_molecule[:pos] + in_molecule[pos:pos+len(left)].replace(left,right) + in_molecule[pos+len(left):]
        out_molecules.add(new_molecule)
    return out_molecules


all_reactions, molecule = parse_input('inputs/input19')
generated_molecules = set()
for reaction in all_reactions:
    generated_molecules |= react(reaction, molecule)

part_1 = len(generated_molecules)
print(f'We can create {part_1} distinct molecules!')

# part 2, I don't really get it because it has to do with "unamigous grammar" which I never heard of
# https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju/ this sort of makes sense so I'll go with it

elements = set(left for left, right in all_reactions) | {'Ar', 'Rn', 'Y'}
count_all_elements = sum(molecule.count(element) for element in elements)

count_ArRn = molecule.count('Ar') + molecule.count('Rn')
count_Y = molecule.count('Y')

part_2 = count_all_elements - count_ArRn - 2 * count_Y - 1
print(f'Not entirely sure how, but part 2 solution is: {part_2}!') #\\
# Not entirely sure how, but part 2 solution is: 207!
