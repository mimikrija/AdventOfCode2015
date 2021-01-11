# Day 7: Some Assembly Required
from collections import namedtuple

Instruction = namedtuple('Instruction', ['operator', 'arguments'])

OPERATORS = {
    'EQ': '',
    'NOT': '-65535',
    'AND': '&',
    'OR': '|',
    'RSHIFT': '>>',
    'LSHIFT': '<<',
}


def parse_input(filename):
    with open(filename) as in_file:
        inputs = in_file.readlines()
    instructions = {}
    for line in inputs:
        expression, wire = line.strip().split(' -> ')
        expression = expression.split()
        if len(expression) == 1: # e.g. 123 -> x
            instructions[wire] = Instruction('EQ', [expression[0]])
        if len(expression) == 2: # e.g. NOT x -> h
            instructions[wire] = Instruction(expression[0], [expression[1]])
        if len(expression) == 3: # e.g. x LSHIFT 2 -> f
            instructions[wire] = Instruction(expression[1], [expression[pos] for pos in [0, 2]])
    return instructions

