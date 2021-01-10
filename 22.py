# Day 22: Wizard Simulator 20XX

from collections import namedtuple
from queue import Queue

# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

# declare Spell type
Spell = namedtuple('Spell', ['name', 'cost', 'damage', 'heal', 'armor', 'new_mana', 'effect_duration'])

# define spells:
SPELLS = [Spell('Magic Missile', 53, 4, 0, 0, 0, 1),
          Spell('Drain', 73, 2, 2, 0, 0, 1),
          Spell('Shield', 113, 0, 0, 7, 0, 6),
          Spell('Poison', 173, 3, 0, 0, 0, 6),
          Spell('Recharge', 229, 0, 0, 0, 101, 5),
          ]


input_boss = {'hit_points': 55,
              'damage': 8,
              }

input_me = {'hit_points': 50,
            'mana': 500,
            }

# example
# input_boss = {'hit_points': 14,
#               'damage': 8,
#               }

# input_me = {'hit_points': 10,
#             'mana': 250,
#             }


def apply_effects(me, boss, active_effects):
    # apply stuff from active_effects and update active_effects status
    updated_active_effects = []
    me['armor'] = 0
    for spell, timer in active_effects:
        boss['hit_points'] -= spell.damage
        me['hit_points'] += spell.heal
        me['mana'] += spell.new_mana
        # armor is just active, not updated so I must apply it like this
        if spell.armor > 0:
            me['armor'] = spell.armor
        # keeep spells for the next turn if the timer hasn't gone off
        if timer > 1:
            updated_active_effects.append((spell, timer - 1))
    return updated_active_effects


def turn(in_me, in_boss, active_effects, mana_expense_so_far, selected_spell):
    """ Simulate a game turn """
    # initialize stuff
    total_mana_spent = mana_expense_so_far
    me = dict(in_me)
    me['hit_points'] -= 1 #hard mode
    if me['hit_points'] <= 0:
        return
    boss = dict(in_boss)

    # MY TURN
    # apply stuff from active_effects and update active_effects status
    updated_active_effects = apply_effects(me, boss, active_effects)


    # check if I win before casting any new spells:
    if boss['hit_points'] <= 0:
        return total_mana_spent

    # if a spell is already active, I cannot cast this spell:
    # this is not a loss, but an invalid state that needs no further analysis
    if selected_spell in (updated_effect[0] for updated_effect in updated_active_effects):
        return

    # if I cannot afford to cast a spell, I lose
    if selected_spell.cost > me['mana']:
        return

    # ok, finally cast a new spell (the effects of this actually apply for the bosses turn)

    # if it contains an effect, add it to the list of active effects so that they can be
    # applied in the bosses turn
    if selected_spell.effect_duration > 0:
        updated_active_effects.append((selected_spell, selected_spell.effect_duration))
    # else: spells with immediate effects
    else:
        boss['hit_points'] -= selected_spell.damage
        me['hit_points'] += selected_spell.heal

    # do the expenses
    me['mana'] -= selected_spell.cost
    total_mana_spent += selected_spell.cost

    # we can prune here if we are already over the budget
    if total_mana_spent > least_mana:
        return

    
    # BOSS TURN
    # apply stuff from active_effects and update active_effects status
    updated_active_effects = apply_effects(me, boss, updated_active_effects)


    # check if I win:
    if boss['hit_points'] <= 0:
        return total_mana_spent

    # boss turn
    me['hit_points'] -= max(boss['damage'] - me['armor'], 1)

    # check if boss wins:
    if me['hit_points'] <= 0:
        return
    
    # if nothing is returned by this point, it means that no one won so we keep playing:
    return me, boss, updated_active_effects, total_mana_spent


# initialize
initial_game = (dict(input_me), dict(input_boss), [], 0)
states = Queue()
states.put(initial_game)
least_mana = float('inf')
# breadth first
while not states.empty():
    current_state = states.get()
    #print(current_state)
    for spell in SPELLS:
        outcome = turn(*current_state, spell)
        if isinstance(outcome, tuple):
            states.put(outcome)
        elif outcome:
            least_mana = min(least_mana, outcome)

print(least_mana)
# 953

# hard mode 1289