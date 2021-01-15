import re

def paper_needed(dimensions):
    l, w, h = dimensions
    areas = (l*w, w*h, h*l)
    slack = min(areas)
    return 2 * sum(areas) + slack

def ribbon_needed(dimensions):
    l, w, h = sorted(dimensions)
    bow = l * w * h
    ribbon = 2 * (l + w)
    return ribbon + bow

with open('inputs/input02') as input_file:
    inputs = input_file.readlines()

re_numbers = re.compile(r'\d+')
all_boxes = [tuple(map(int,re.findall(re_numbers, line))) for line in inputs]

# part 1
total_paper_needed = sum(paper_needed(box) for box in all_boxes)
print(f'The elves need to order a total of {total_paper_needed} sq. feet of wraping paper!')
# The elves need to order a total of 1588178 sq. feet of wraping paper!

# part 2
total_ribbon_needed = sum(ribbon_needed(box) for box in all_boxes)
print(f'The elves need to order a total of {total_ribbon_needed} feet of ribbon!')
# The elves need to order a total of 3783758 feet of ribbon!!
