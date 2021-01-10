# Day 6: Probably a Fire Hazard
import re
from collections import namedtuple

Command = namedtuple('Command', ['command', 'from_x', 'from_y', 'to_x', 'to_y'])


def parse_input(filename):
    with open(filename) as in_file:
        inputs = in_file.readlines()

    instructions = []
    for line in inputs:
        command = re.findall(r'toggle|turn on|turn off', line)[0]
        from_x, from_y, to_x, to_y = map(int, re.findall(r'\d+', line))
        instructions.append(Command(command, from_x, from_y, to_x, to_y))
    return instructions


def create_range(from_x, to_x, from_y, to_y):
    return {(x, y) for x in range(from_x, to_x+1)
                   for y in range(from_y, to_y+1)}


def turn_on_the_lights(instructions):
    lights_on = set()
    for instruction in instructions:
        if instruction.command == 'turn on':
            lights_on |= create_range(instruction.from_x, instruction.to_x, instruction.from_y, instruction.to_y)
        if instruction.command == 'toggle':
            lights_on ^= create_range(instruction.from_x, instruction.to_x, instruction.from_y, instruction.to_y)
        if instruction.command == 'turn off':
            lights_on -= create_range(instruction.from_x, instruction.to_x, instruction.from_y, instruction.to_y)

    return len(lights_on)


instructions = parse_input('inputs/input06')


part_1 = turn_on_the_lights(instructions)
print(f'After processing all instructions, there are {part_1} lights on!')

