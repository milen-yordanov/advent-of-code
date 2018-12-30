# See: https://adventofcode.com/2018/day/8#part2

import re
import pprint

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

license_file_tree_data = [int(x) for x in content[0].split()]

def parse_tree(tree_data):
    child_nodes_num = tree_data[0]
    metadata_entries_num = tree_data[1]
    val = 0
    pos = 2
    child_val = []
    metadata_val = []
    for _ in range(child_nodes_num):
        res = parse_tree(tree_data[pos:])
        pos += res[0]
        child_val.append(res[1])

    for _ in range(metadata_entries_num):
        metadata_val.append(tree_data[pos])
        pos += 1

    if child_nodes_num == 0:
        val = sum(metadata_val)
    else:
        for i in metadata_val:
            if (i > 0) and (i <= len(child_val)):
                val += child_val[i-1]

    return (pos, val)

res = parse_tree(license_file_tree_data)
print (res[1])


