with open('inputs/input01') as input_file:
    inputs = input_file.read()

go = lambda p: 1 if p == '(' else -1

final_floor = sum(go(direction) for direction in inputs)

print(f'The instructions take Santa to floor no. {final_floor}!')
# The instructions take Santa to floor no. 74!

def find_instruction(inputs, first_time_at_floor):
    current_floor = 0
    for pos, direction in enumerate(inputs):
        current_floor += go(direction)
        if current_floor == -1:
            return pos + 1

first_time_in_basement = find_instruction(inputs, -1)

print(f'The first instruction for which Santa ends up in the basement is {first_time_in_basement}!')
# The first instruction for which Santa ends up in the basement is 1795!
