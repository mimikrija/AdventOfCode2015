import json

def get_int_items(in_item, out, is_part_2 = False):
    for item in in_item:
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

dict_json = dict()
with open('inputs/input12') as input_file:
    input_json = json.loads(input_file.read())

solution_1 = list()
get_int_items(input_json, solution_1)
part_1 = sum(solution_1)
print(part_1) # 156366 # 96852 part 2

solution_2 = list()
get_int_items(input_json, solution_2, True)
part_2 = sum(solution_2)
print(part_2)

