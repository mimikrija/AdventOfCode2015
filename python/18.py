# Day 18: Like a GIF For Your Yard
import itertools

DELTAS = set(itertools.product({-1, 0, 1}, repeat=2)) - {(0,0)}

def parse_input(in_file):
    with open(in_file) as input_file:
        light_lines = input_file.readlines()
    DIMENSION = len(light_lines)
    return DIMENSION, {(row, column) for row, line in enumerate(light_lines) for column, light in enumerate(line) if light == '#' }


def add_coordinates(tuple_1, tuple_2):
    return tuple(one + two for one, two in zip(tuple_1, tuple_2))


def neighbors(in_coordinate):
    return set(add_coordinates(in_coordinate, delta) for delta in DELTAS
                if all(0 <= t < DIMENSION for t in add_coordinates(in_coordinate, delta)))


def turn_on_the_lights(in_lights_on, always_on_lights = set()):
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
    return out_lights_on | always_on_lights


def lights_on_after_cycles(in_lights_on, cycles, always_on_lights = set()):
    lights_on = set(in_lights_on) | always_on_lights
    for _ in range(cycles):
        lights_on = turn_on_the_lights(lights_on, always_on_lights)
    return len(lights_on)


DIMENSION, all_lights = parse_input('inputs/input18')
cycles = 100

part_1 = lights_on_after_cycles(all_lights, cycles)
print(f'After {cycles} cycles, there are {part_1} lights left on!')
# After 100 cycles, there are 814 lights left on!

# part 2: four corners are always on!
always_on_lights = set(itertools.product({0, DIMENSION-1}, repeat=2))

part_2 = lights_on_after_cycles(all_lights, cycles, always_on_lights)
print(f'After {cycles} cycles, and four corner lights always on, there are {part_2} lights left on!')
# After 100 cycles, and four corner lights always on, there are 924 lights left on!
