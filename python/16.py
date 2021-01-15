# Day 16: Aunt Sue

import re
import operator

CORRECT_AUNT_SUE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

def find_correct_sue(in_aunts):
    for num, aunt in enumerate(in_aunts):
        if aunt.items() & CORRECT_AUNT_SUE.items() == aunt.items():
            return num + 1

def check_items(in_aunt, set_to_check, oper, inc):
    return all(oper(in_aunt.get(key, CORRECT_AUNT_SUE[key] + inc), CORRECT_AUNT_SUE[key]) for key in set_to_check)

def find_real_aunt_sue(in_aunts):
    more_than = ({'cats', 'trees'}, operator.gt, 1)
    less_than = ({'pomeranians', 'goldfish'}, operator.lt, -1)
    same = (CORRECT_AUNT_SUE.keys() - less_than[0] - more_than[0], operator.eq, 0)

    for num, aunt in enumerate(in_aunts):
        if all(check_items(aunt, *rule) for rule in (more_than, less_than, same)):
            return num + 1


re_words = re.compile(r'[a-z]+')
re_numbers = re.compile(r'\d+')

with open('inputs/input16') as input_file:
    aunts_input = input_file.readlines()

all_aunts = []
for line in aunts_input:
    aunt_keys = re.findall(re_words, line)[1:]
    aunt_values = map(int, re.findall(re_numbers, line)[1:])
    aunt = {aunt_key: aunt_value for aunt_key, aunt_value in zip(aunt_keys, aunt_values)}
    all_aunts.append(aunt)

part_1, part_2 = find_correct_sue(all_aunts), find_real_aunt_sue(all_aunts)

print(f'The aunt we are looking for is aunt Sue {part_1}!')
# The aunt we are looking for is aunt Sue 103!

print(f'Actually, the real aunt we are looking for is aunt Sue {part_2}!')
# Actually, the real aunt we are looking for is aunt Sue 405!
