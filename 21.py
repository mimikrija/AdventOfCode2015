# Day 21: RPG Simulator 20XX

me = {'hit_points': 8,
      'damage': 5,
      'armor': 5,
      }

boss = {'hit_points': 12,
        'damage': 7,
        'armor': 2,
        }

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

print(take_turns(me, boss))
