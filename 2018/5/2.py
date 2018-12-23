# See: https://adventofcode.com/2018/day/5#part2

import re
import pprint

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

records = [x.strip() for x in content]
