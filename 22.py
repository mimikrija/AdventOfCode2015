# Day 22: Wizard Simulator 20XX

from collections import namedtuple

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


input_boss = ['Hit Points: 55',
              'Damage: 8',
              ]

input_me = ['Hit Points: 50',
            'Mana: 500',
            ]
