# Day 9: All in a Single Night

def distance_between(node_1, node_2, nodes_and_distances):
    return nodes_and_distances[node_1][node_2]

def neighbors(node, nodes_and_distances):
    return set(nodes_and_distances[node].keys())

def shortest_path(initial_node, nodes_and_distances):
    visited_set = {initial_node}
    unvisited_set = STARS - visited_set
    current_node = initial_node
    total_distance = 0
    while unvisited_set:
        neighbors_and_distances = ((neighbor, distance_between(current_node, neighbor, nodes_and_distances)) for neighbor in neighbors(current_node, nodes_and_distances) if neighbor not in visited_set)
        neighbors_and_distances = sorted(neighbors_and_distances, key= lambda p: p[1])
        visited, distance = neighbors_and_distances[0]
        unvisited_set -= {visited}
        visited_set |= {visited}
        total_distance += distance
        current_node = visited

    return total_distance
        



with open('inputs/input09') as input_file:
    star_distances = input_file.readlines()

stars_and_distances = {}
STARS = set()
for line in star_distances:
    names, distance = line.strip().split(' = ')
    first, second = names.split(' to ')
    distance = int(distance)
    if first in stars_and_distances:
        stars_and_distances[first][second] = distance
    else:
        stars_and_distances[first] = {second: distance}
    if second in stars_and_distances:
        stars_and_distances[second][first] = distance
    else:
        stars_and_distances[second] = {first: distance}
    STARS |= {first, second}


all_distances = (shortest_path(star, stars_and_distances) for star in STARS)
part_1 = min(all_distances)
print(part_1) # 207
