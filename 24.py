# Day 24: It Hangs in the Balance

def parse_input(in_file):
    with open(in_file) as input_file:
        inputs = input_file.readlines()

    return list(map(int, inputs))


weights = parse_input('inputs/input24')
