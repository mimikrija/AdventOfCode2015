# Day 25: Let It Snow

from collections import namedtuple

input_row, input_column = 2947, 3029

def generate_code(previous_value):
    return (previous_value * 252533) % 33554393

def get_previous_position(row, column):
    if column == 1:
        return 1, row - 1
    else:
        return row + 1, column - 1

def next_position(row, column):
    if row == 1:
        return (column + 1, 1)
    else:
        return (row - 1, column + 1)

Code = namedtuple('Code', ['row', 'column', 'value'])
code_table = [Code(1, 1, 20151125)]


current_position = (1,1)
while True:
    previous_row, previous_column, previous_value = code_table[-1]
    current_row, current_column = next_position(previous_row, previous_column)
    value = generate_code(previous_value)
    if current_row == input_row and current_column == input_column:
        print(value)
        break
    else:
        code_table.append(Code(current_row, current_column, value))

# 19980801