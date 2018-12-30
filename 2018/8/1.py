# See: https://adventofcode.com/2018/day/8#part1

import re
import pprint

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

license_file_tree_data = [int(x) for x in content[0].split()]

def parse_tree(tree_data, metadata_cb):
    child_nodes_num = tree_data[0]
    metadata_entries_num = tree_data[1]
    pos = 2
    for _ in range(child_nodes_num):
        pos += parse_tree(tree_data[pos:], metadata_cb)

    for _ in range(metadata_entries_num):
        metadata_cb(tree_data[pos])
        pos += 1

    return pos

metadata_sum = 0
def metadata_accumulator(val):
    global metadata_sum
    metadata_sum += val

parse_tree(license_file_tree_data, metadata_accumulator)
print (metadata_sum)
