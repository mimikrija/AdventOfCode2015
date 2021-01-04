# Day 16: Aunt Sue

import re

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

print(find_correct_sue(all_aunts)) # 103
