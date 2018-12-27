# See: https://adventofcode.com/2018/day/6#part1

import re
import pprint

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

def parse_coordinate(coordinate_str):
    toks = coordinate_str.split(',')
    return (int(toks[0]),int(toks[1]))

coordinates = [parse_coordinate(x.strip()) for x in content]

max_x = max(coordinates, key=lambda k: k[0])[0] + 1
max_y = max(coordinates, key=lambda k: k[1])[1] + 1

MAT_EQ_MULT = -4

def get_distance(x, y, coord):
    return abs(x - coord[0]) + abs(y - coord[1])

def get_closest_coord(distances):
    ds = sorted(distances)
    if ds[0] == ds[1]:
        return MAT_EQ_MULT
    return distances.index(ds[0])

freq_coord_all = {}
border_set = set()
for x in range(max_x):
    for y in range(max_y):
        distances = [get_distance(x, y, coord) for coord in coordinates]
        v = get_closest_coord(distances)
        if (v >= 0):
            if v in freq_coord_all:
                freq_coord_all[v] += 1
            else:
                freq_coord_all[v] = 1

            if (x == 0) or (y == 0) or (x == (max_x-1)) or (y == (max_y-1)):
                border_set.add(v)
     

freq_coord_value_list = []
for coord_index in freq_coord_all:
    if not (coord_index in border_set):
        freq_coord_value_list.append(freq_coord_all[coord_index])

print (max(freq_coord_value_list))