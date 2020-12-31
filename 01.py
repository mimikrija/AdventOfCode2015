go = lambda p: 1 if p == '(' else -1

def find_instruction(instructions, first_time_at_floor):
    current_floor = 0
    for pos, direction in enumerate(instructions):
        current_floor += go(direction)
        if current_floor == -1:
            return pos + 1

with open('inputs/input01') as input_file:
    elevator_instructions = input_file.read()

# part 1
final_floor = sum(go(direction) for direction in elevator_instructions)
print(f'The instructions take Santa to floor no. {final_floor}!')
# The instructions take Santa to floor no. 74!

# part 2
first_time_in_basement = find_instruction(elevator_instructions, -1)
print(f'The first instruction for which Santa ends up in the basement is {first_time_in_basement}!')
# The first instruction for which Santa ends up in the basement is 1795!
