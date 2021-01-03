import re
import itertools

sign = lambda line: 1 if 'gain' in line else -1

def calculate_change_in_happiness(seating_arangement, happiness_calc):
    score = 0
    for n in range(len(seating_arangement)):
        left, middle, right = seating_arangement[n-1], seating_arangement[n], seating_arangement[(n+1)%(len(seating_arangement))]
        score += happiness_calc[(middle, left)] + happiness_calc[(middle, right)]
    return score


def get_optimal_seating_score(names, happiness_calc):
    possible_seating_arrrangements = (combo for combo in itertools.permutations(names))
    return max(calculate_change_in_happiness(combo, happiness_calc) for combo in possible_seating_arrrangements)

with open('inputs/input13') as input_file:
    potential_happiness_input = input_file.readlines()

re_names = re.compile(r'[A-Z][a-z]+')
re_numbers = re.compile(r'\d+')

# part 1 input
NAMES = set()
HAPPINESS_CALCULATION = {}
for line in potential_happiness_input:
    name_1, name_2 = re.findall(re_names, line)
    units = sign(line)*int(re.findall(re_numbers, line)[0])
    HAPPINESS_CALCULATION[(name_1, name_2)] = units
    NAMES |= {name_1, name_2}

# part 2 input: add ambivalent "me" to the party
HAPPINESS_CALCULATION_WITH_ME = dict(HAPPINESS_CALCULATION)
for name in NAMES:
    for name_pair in itertools.permutations({name, 'me'}):
        HAPPINESS_CALCULATION_WITH_ME[name_pair] = 0
NAMES_WITH_ME = NAMES | {'me'}

part_1, part_2 = (get_optimal_seating_score(names, happiness_calculation) for names, happiness_calculation in zip((NAMES, NAMES_WITH_ME),(HAPPINESS_CALCULATION, HAPPINESS_CALCULATION_WITH_ME)))

print(f'Total change in happiness for the initial guest list is {part_1}!')
# # Total change in happiness for the initial guest list is 618!

print(f'If I (ambivalent) join the party, total change in happiness is {part_2}!')
# If I (ambivalent) join the party, total change in happiness is 601!
