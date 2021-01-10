# Day 5: Doesn't He Have Intern-Elves For This?

from collections import Counter

def has_vowels(in_string):
    count_vowels = sum(Counter(in_string)[vowel] for vowel in 'aeiou')
    return count_vowels >= 3


def has_double(in_string):
    for first, second in zip(in_string, in_string[1:]):
        if first == second:
            return True
    return False


def substring_appears_twice(in_string):
    for pos in range(len(in_string)-2):
        if in_string[pos+2:].find(in_string[pos:pos+2]) > -1:
            return True
    return False


def has_sandwich(in_string):
    for first, second in zip(in_string, in_string[2:]):
        if first == second:
            return True
    return False


def is_nice(in_string, is_part_2 = False):
    if not is_part_2:
        if any(sub in in_string for sub in {'ab', 'cd', 'pq', 'xy'}):
            return False

        if not has_vowels(in_string):
            return False
        
        return has_double(in_string)

    else:
        if not substring_appears_twice(in_string):
            return False

        return has_sandwich(in_string)


def parse_input(filename):
    with open(filename) as infile:
        inputs = infile.readlines()

    return [line.strip() for line in inputs]

strings_to_test = parse_input('inputs/input05')


part_1 = sum(is_nice(word) for word in strings_to_test)
print(f'There are {part_1} nice strings in my input!')
# There are 238 nice strings in my input!

part_2 = sum(is_nice(word, True) for word in strings_to_test)
print(f'There are {part_2} nice strings in my input!')
# There are 69 nice strings in my input!
