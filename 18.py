# Day 18: Like a GIF For Your Yard
import itertools

def parse_input(in_file):
    with open(in_file) as input_file:
        light_lines = input_file.readlines()

    return {(row, column) for row, line in enumerate(light_lines) for column, light in enumerate(line) if light == '#' }


all_lights = parse_input('inputs/input18')
