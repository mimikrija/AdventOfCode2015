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

def solution_wrapper(instructions, wire):

    def memoize(function):
        """ function to memoize whatever is going on in solve_wire """
        memoized = {}
        def wrap(instructions, wire):
            if wire not in memoized:
                memoized[wire] = function(instructions, wire)
            return memoized[wire]
        return wrap


    def apply_operation(operation, wire_1, wire_2 = ''):
        expression = ''.join([str(wire_1), OPERATORS[operation], str(wire_2)])
        return abs(eval(expression)) # see commit for more info about this hackiness


    @memoize # this is the same as writing: solve_wire = memoize(solve_wire)
    def solve_wire(instructions, wire):
        """ returns value of `wire` given the input `instructions` dict
        if the value does not exists, it calls itself recursively until it is returned """
        try:
            return int(wire)
        except:
            pass

        operator, arguments = instructions[wire]
        if len(arguments) == 1:
            return apply_operation(operator, solve_wire(instructions, arguments[0]))
        if len(arguments) == 2:
            return apply_operation(operator, solve_wire(instructions, arguments[0]), solve_wire(instructions, arguments[1]))

    return solve_wire(instructions, wire)



circuit = parse_input('inputs/input07')


part_1 = solution_wrapper(circuit, 'a')
print(f'The value of wire "a" is {part_1}!')
# The value of wire "a" is 46065!

# part 2: set the value of wire 'b' to solution of part 1, run the whole thing again
circuit['b'] = Instruction('EQ', [str(part_1)])
part_2 = solution_wrapper(circuit, 'a')

print(f'The value of wire "a" (after rewiring "b" to point to part 1 solution) is {part_2}!')
