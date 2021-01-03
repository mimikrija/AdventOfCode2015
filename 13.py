import re
import itertools

sign = lambda line: 1 if 'gain' in line else -1

def calculate_change_in_happiness(seating_arangement):
    score = 0
    for n in range(len(seating_arangement)):
        left, middle, right = seating_arangement[n-1], seating_arangement[n], seating_arangement[(n+1)%(len(seating_arangement))]
        score += HAPPINESS_CALCULATION[(middle, left)] + HAPPINESS_CALCULATION[(middle, right)]
    return score


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

possible_seating_arrrangements = list(combo for combo in itertools.permutations(NAMES))
scores = (calculate_change_in_happiness(combo) for combo in possible_seating_arrrangements)
print(max(scores)) # 618

for name in NAMES:
    pair_1 = (name, "me")
    pair_2 = ("me", name)
    HAPPINESS_CALCULATION[pair_1] = 0
    HAPPINESS_CALCULATION[pair_2] = 0


possible_seating_arrrangements = list(combo for combo in itertools.permutations(NAMES|{"me"}))
scores = (calculate_change_in_happiness(combo) for combo in possible_seating_arrrangements)

print(max(scores)) # 601

