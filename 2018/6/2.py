# See: https://adventofcode.com/2018/day/6#part2

import re

input_file_name = 'input.txt'
TOTAL_DISTANCE = 10000

with open(input_file_name) as f:
    content = f.readlines()

def parse_coordinate(coordinate_str):
    toks = coordinate_str.split(',')
    return (int(toks[0]),int(toks[1]))

coordinates = [parse_coordinate(x.strip()) for x in content]

max_x = max(coordinates, key=lambda k: k[0])[0] + 1
max_y = max(coordinates, key=lambda k: k[1])[1] + 1

def get_distance(x, y, coord):
    return abs(x - coord[0]) + abs(y - coord[1])

area_size = 0
for x in range(max_x):
    for y in range(max_y):
        distances = [get_distance(x, y, coord) for coord in coordinates]
        total_dist = sum(distances)
        if total_dist < TOTAL_DISTANCE:
            area_size += 1
     
print (area_size)