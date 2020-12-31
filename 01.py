with open('inputs/input01') as input_file:
    inputs = input_file.read()

go = lambda p: 1 if p == '(' else -1

final_floor = sum(go(direction) for direction in inputs)

print(f'The instructions take Santa to floor no. {final_floor}!')
# The instructions take Santa to floor no. 74!

current_floor = 0
for pos, direction in enumerate(inputs):
    current_floor += go(direction)
    if current_floor == -1:
        first_time_in_basement = pos + 1
        break

print(f'The first instruction for which Santa ends up in the basement is {first_time_in_basement}!')
# The first instruction for which Santa ends up in the basement is 1795!
