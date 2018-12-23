# See: https://adventofcode.com/2018/day/5#part1

import re

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

polymer = content[0].strip()

def isSameTypeOpositePolarity(v1, v2):
    return (v1 != v2) and (v1.lower() == v2.lower())

pos = 0
while pos < (len(polymer) - 1):
    v1 = polymer[pos]
    v2 = polymer[pos + 1]
    if isSameTypeOpositePolarity(v1, v2):
        polymer = polymer[0: pos] + polymer[pos+2:]
        pos = max(pos-1, 0)
    else:
        pos += 1

print (len(polymer))