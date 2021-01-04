# Day 14: Reindeer Olympics

import re

def distance_travelled(total_time, speed, travel_time, rest_time):
    time_cycle = travel_time + rest_time
    cycle_count, remainder = total_time // time_cycle, total_time % time_cycle
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

race_time = 2503

distances = (distance_travelled(race_time, *raindeer) for raindeer in raindeer_data.values())

print(max(distances)) # 2696

total_points = {raindeer: 0 for raindeer in raindeer_data.keys()}
for time in range(1,race_time+1):
    current_points = {raindeer_name: distance_travelled(time, *raindeer) for raindeer_name, raindeer in raindeer_data.items()}
    winning_distance = max(current_points.values())
    for raindeer_name, distance in current_points.items():
        if distance == winning_distance:
            total_points[raindeer_name] += 1

print(max(total_points.values()))

