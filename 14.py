# Day 14: Reindeer Olympics

import re

def distance_travelled(total_time, speed, travel_time, rest_time):
    time_cycle = travel_time + rest_time
    cycle_count, remainder = divmod(total_time, time_cycle)
    if remainder >= travel_time:
        rest = travel_time
    else:
        rest = remainder
    total_time_travelled = cycle_count * travel_time + rest
    return total_time_travelled * speed

with open('inputs/input14') as input_file:
    raindeer_input = input_file.readlines()

raindeer_data = {}
re_numbers = re.compile(r'\d+')
for line in raindeer_input:
    raindeer = line.split(' ')[0]
    speed, fly_time, rest_time = map(int, (num for num in re.findall(re_numbers, line)))
    raindeer_data[raindeer] = (speed, fly_time, rest_time)

RACE_DURATION = 2503

part_1 = max(distance_travelled(RACE_DURATION, *raindeer) for raindeer in raindeer_data.values())
print(f'The winning raindeer has travelled {part_1} km!')
# The winning raindeer has travelled 2696 km!

def new_rules():
    total_points = {raindeer: 0 for raindeer in raindeer_data.keys()}
    for time in range(1, RACE_DURATION+1):
        current_points = {raindeer_name: distance_travelled(time, *raindeer) for raindeer_name, raindeer in raindeer_data.items()}
        winning_distance = max(current_points.values())
        for raindeer_name, distance in current_points.items():
            if distance == winning_distance:
                total_points[raindeer_name] += 1
    return max(total_points.values())

part_2 = new_rules()
print(f'Following the new rules, the winning raindeer has {part_2} points!')
# Following the new rules, the winning raindeer has 1084 points!
