# Day 25: Let It Snow

input_row, input_column = 2947, 3029

def generate_code(member):
    value = 20151125
    for _ in range(member-1):
        value = (value * 252533) % 33554393
    return value


def which_member(row, column):
    return sum(n for n in range(1, row + column - 1)) + column


part_1 = generate_code(which_member(input_row, input_column))
print(f'I give the machine code {part_1}!')
# I give the machine code 19980801!
