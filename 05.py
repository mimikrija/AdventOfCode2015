# Day 5: Doesn't He Have Intern-Elves For This?

from collections import Counter

def has_vowels(in_string):
    count_vowels = sum(Counter(in_string)[vowel] for vowel in 'aeiou')
    return count_vowels >= 3


def has_double(in_string):
    for first, second in zip(list(in_string), list(in_string)[1:]):
        if first == second:
            return True
    return False


def is_nice(in_string):
    if any(sub in in_string for sub in {'ab', 'cd', 'pq', 'xy'}):
        return False

    if not has_vowels(in_string):
        return False
    
    return has_double(in_string)


def parse_input(filename):
    with open(filename) as infile:
        inputs = infile.readlines()

    return [line.strip() for line in inputs]


part_1 = sum(is_nice(word) for word in parse_input('inputs/input05'))
print(f'There are {part_1} nice strings in my input!')
# There are 238 nice strings in my input!
