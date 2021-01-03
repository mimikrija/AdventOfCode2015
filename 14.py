# Day 14: Reindeer Olympics

import re

with open('inputs/input14') as input_file:
    raindeer_input = input_file.readlines()

raindeer_data = {}
re_numbers = re.compile(r'\d+')
for line in raindeer_input:
    raindeer = line.split(' ')[0]
    speed, fly_time, rest_time = map(int, (num for num in re.findall(re_numbers, line)))
    raindeer_data[raindeer] = (speed, fly_time, rest_time)
