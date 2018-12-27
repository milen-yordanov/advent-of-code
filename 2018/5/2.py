# See: https://adventofcode.com/2018/day/5#part2

import re

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

polymer = content[0].strip()

def isSameTypeOpositePolarity(v1, v2):
    return (v1 != v2) and (v1.lower() == v2.lower())

def react_polymer(pr):
    pos = 0
    while pos < (len(pr) - 1):
        v1 = pr[pos]
        v2 = pr[pos + 1]
        if isSameTypeOpositePolarity(v1, v2):
            pr = pr[0: pos] + pr[pos+2:]
            pos = max(pos-1, 0)
        else:
            pos += 1
    return pr

def remove_type_from_polymer(pr, t):
    tU = t.upper()
    tL = t.lower()
    res = ''
    for c in pr:
        if (c != tU) and (c != tL):
            res += c

    return res

pr_rem_types = {}
polymer = react_polymer(polymer)

for c in polymer:
    pr_rem_types[c.lower()] = 0

for c in pr_rem_types:
    pr_rem_types[c] = len(react_polymer(remove_type_from_polymer(polymer[:], c)))


min_key = min(pr_rem_types, key=lambda k: pr_rem_types[k])

print (pr_rem_types)
print (min_key)
print (pr_rem_types[min_key])


