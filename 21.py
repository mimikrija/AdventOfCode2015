# Day 21: RPG Simulator 20XX

import itertools


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
# each tuple represents (cost, damage, armor)

WEAPONS = {(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)}
ARMORS = {(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)} # I added (0, 0, 0) becaose armor is not mandatory
RINGS = {(0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)} # I added (0, 0, 0) because rings are not mandatory


weapon_armor_combos = [combo for combo in itertools.product(*[WEAPONS, ARMORS])]
ring_combos = [perm for perm in itertools.permutations(RINGS, 2)]
ring_combos.append(((0, 0, 0), (0, 0,0))) # since we may buy max 2 and min 0, I needed to add this combo in case we buy NO rings at all


def get_values_from_combo():
    shopping_combos = []
    for weapon, arm in weapon_armor_combos:
        for ring_1, ring_2 in ring_combos:
            gold, damage, armor = (one + two + three + four for one, two, three, four in zip(weapon, arm, ring_1, ring_2))
            shopping_combos.append((gold, damage, armor))

    return shopping_combos


BOSS = {'hit_points': 103,
        'damage': 9,
        'armor': 2,
        }

me = {}


def gold_spent(is_part_2 = False):
    if is_part_2:
        winner = 'boss'
    else:
        winner = 'me'
    shopping_list = get_values_from_combo()
    shopping_list.sort(key = lambda x: x[0], reverse=is_part_2)
    for combo in shopping_list:
        # initialize me and boss values
        # I get my values from the shopping list
        gold, my_damage, my_armor = combo
        me['hit_points'] = 100
        me['damage'] = my_damage
        me['armor'] = my_armor
        # boss is always the same
        boss = dict(BOSS)

        if take_turns(me, boss) == winner:
            return gold


part_1 = gold_spent()
print(f'The least amount of gold I can spend and still win is {part_1}!')

part_2 = gold_spent(True)
print(f'The most amount of gold I can spend and still lose is {part_2}!')
