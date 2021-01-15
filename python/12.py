import json

def get_int_items(in_items, out, is_part_2 = False):
    for item in in_items:
        if isinstance(item, int):
            out.append(item)
        if isinstance(item, list):
            get_int_items(item, out, is_part_2)
        if isinstance(item, dict):
            if any(key=='red' for key in list(item.keys())+list(item.values())) and is_part_2:
                continue
            else:
                get_int_items(item.values(), out, is_part_2)
    return out


def count_all_ints(in_items, is_part_2 = False):
    solution = list()
    get_int_items(in_items, solution, is_part_2)
    return sum(solution)


with open('inputs/input12') as input_file:
    input_json = json.loads(input_file.read())

part_1, part_2 = (count_all_ints(input_json, is_part_2) for is_part_2 in {False, True})

print(f'Part 1 solution is: {part_1}!')
# Part 1 solution is: 156366!

print(f'Part 2 solution is: {part_2}!')
# Part 2 solution is: 96852!
