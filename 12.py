import json

def get_int_items(in_item, out):
    for item in in_item:
        if isinstance(item, int):
            out.append(item)
        if isinstance(item, list):
            get_int_items(item, out)
        if isinstance(item, dict):
            get_int_items(item.values(), out)
    return out

dict_json = dict()
with open('inputs/input12') as input_file:
    input_json = json.loads(input_file.read())

solution = list()
get_int_items(input_json, solution)
part_1 = sum(item for item in solution)
print(part_1) # 156366
