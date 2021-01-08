# Day 23: Opening the Turing Lock

import re

def parse_input(in_file):
    clean = lambda x: x[0] if len(x) > 0 else None
    with open(in_file) as input_file:
        inputs = input_file.readlines()

    instructions = []
    for line in inputs:
        command = clean(re.findall(r'[a-z]{3}', line))
        register = clean(re.findall(r'\b[a-z]{1}\b', line))
        number = clean([int(num) for num in re.findall(r'[+-][0-9]+', line)])
        instructions.append((command, register, number))

    return instructions


def run_program(instructions, registers):
    next_instruction = 0
    while 0 <= next_instruction < len(instructions):
        command, register, number = instructions[next_instruction]
        #print(next_instruction, command, register, number)
        if command == 'hlf':
            registers[register] = registers[register] // 2
            next_instruction += 1
        if command == 'tpl':
            registers[register] = registers[register] * 3
            next_instruction += 1
        if command == 'inc':
            registers[register] += 1
            next_instruction += 1
        if command == 'jmp':
            next_instruction += number
        if command == 'jie':
            if registers[register] % 2 == 0:
                next_instruction += number
            else:
                next_instruction += 1
        if command == 'jio':
            if registers[register] == 1:
                next_instruction += number
            else:
                next_instruction += 1
    
    return registers['b']


instructions = parse_input('inputs/input23')

# part 1
registers_1 = {'a': 0,
              'b': 0,
              }

part_1 = run_program(instructions, registers_1)
print(f'The value of register b is {part_1}!')

# part 2
registers_2 = {'a': 1,
               'b': 0,
              }

part_2 = run_program(instructions, registers_2)
print(f'The value of register b if register a starts at 1 is {part_2}!')
