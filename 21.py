# Day 21: RPG Simulator 20XX

import itertools

# me = {'hit_points': 100,
#       'damage': 5,
#       'armor': 5,
#       }

# boss = {'hit_points': 12,
#         'damage': 7,
#         'armor': 2,
#         }

def play_a_round(attacker, defender):
    damage_dealt = attacker['damage'] - defender['armor']
    if damage_dealt < 0:
        damage_dealt = 1
    defender['hit_points'] -= damage_dealt

def take_turns(me, boss):
    while True:
        play_a_round(me, boss)
        if boss['hit_points'] <= 0:
            return 'me'
        play_a_round(boss, me)
        if me['hit_points'] <= 0:
            return 'boss'


# the other part is to 'go shopping'
# I would create all possible combos of shopping, sort them on the amount of gold spent
# take turns until first time I win
# tuple represents (cost, damage, armor)

WEAPONS = {(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)}
ARMORS = {(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)}
RINGS = {(0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)}


weapon_armor_combos = [combo for combo in itertools.product(*[WEAPONS, ARMORS])]
ring_combos = [p for p in itertools.permutations(RINGS, 2)]
ring_combos.append(((0, 0, 0), (0, 0,0))) # add case when we buy no rings

def get_values_from_combo():
    shopping_combos = []
    for weapon, arm in weapon_armor_combos:
        for ring_1, ring_2 in ring_combos:
            gold, damage, armor = (one + two + three + four for one, two, three, four in zip(weapon, arm, ring_1, ring_2))
            shopping_combos.append((gold, damage, armor))

    shopping_combos.sort(key = lambda x: x[0], reverse=True)
    return shopping_combos

BOSS = {'hit_points': 103, 
        'damage': 9,
        'armor': 2,
        }

me = {}

def find_cheapest_win():
    for combo in get_values_from_combo():
        gold, my_damage, my_armor = combo
        me['hit_points'] = 100
        me['damage'] = my_damage
        me['armor'] = my_armor
        boss = dict(BOSS)

        if take_turns(me, boss) == 'boss':
            return gold

part_1 = find_cheapest_win()
print(part_1)
