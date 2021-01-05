# Day 18: Like a GIF For Your Yard
import itertools

DELTAS = set(itertools.product({-1, 0, 1}, repeat=2)) - {(0,0)}

def parse_input(in_file):
    with open(in_file) as input_file:
        light_lines = input_file.readlines()
    global DIMENSION
    DIMENSION = len(light_lines)
    return {(row, column) for row, line in enumerate(light_lines) for column, light in enumerate(line) if light == '#' }


def add_coordinates(tuple_1, tuple_2):
    return tuple(one + two for one, two in zip(tuple_1, tuple_2))


def neighbors(in_coordinate):
    return set(add_coordinates(in_coordinate, delta) for delta in DELTAS
            if 0 <= add_coordinates(in_coordinate, delta)[0] < DIMENSION and 0 <= add_coordinates(in_coordinate, delta)[1] < DIMENSION)


def turn_on_the_lights(in_lights_on):
    out_lights_on = set()
    relevant_off_lights = set()
    for light in in_lights_on:
        relevant_off_lights |= neighbors(light)
    relevant_off_lights -= in_lights_on

    for light in in_lights_on | relevant_off_lights:
        count_neighbors = sum(neighbor in in_lights_on for neighbor in neighbors(light))
        if ((light in in_lights_on and count_neighbors in {2, 3}) or
             light in relevant_off_lights and count_neighbors == 3):
            out_lights_on.add(light)
    return out_lights_on


def lights_on_after_cycles(in_lights_on, cycles):
    lights_on = set(in_lights_on)
    for _ in range(cycles):
        lights_on = turn_on_the_lights(lights_on)
    return len(lights_on)


all_lights = parse_input('inputs/input18')
cycles = 100

part_1 = lights_on_after_cycles(all_lights, cycles)
print(f'After {cycles} cycles, there are {part_1} lights left on!')
# After 100 cycles, there are 814 lights left on!
