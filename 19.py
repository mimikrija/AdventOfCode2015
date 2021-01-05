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

print(len(generated_molecules))
