import re

sign = lambda line: 1 if 'gain' in line else -1


with open('inputs/input13') as input_file:
    potential_happiness_input = input_file.readlines()

re_names = re.compile(r'[A-Z][a-z]+')
re_numbers = re.compile(r'\d+')

NAMES = set()
HAPPINESS_CALCULATION = {}
for line in potential_happiness_input:
    name_1, name_2 = re.findall(re_names, line)
    units = sign(line)*int(re.findall(re_numbers, line)[0])
    HAPPINESS_CALCULATION[(name_1, name_2)] = units
    NAMES |= {name_1, name_2}
