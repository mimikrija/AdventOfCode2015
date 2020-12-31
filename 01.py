from collections import Counter

with open('inputs/input01') as input_file:
    inputs = input_file.read()

up_down_count = Counter(inputs)
up = up_down_count['(']
down = up_down_count[')']

current_floor = up - down
print(f'The instructions take Santa to floor no. {current_floor}!')
# The instructions take Santa to floor no. 74!
