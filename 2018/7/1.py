# See: https://adventofcode.com/2018/day/7#part1

import re
import pprint

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

def parse_dependency(coordinate_str):
    toks = coordinate_str.split(' ')
    return (toks[1], toks[7])

dependencies = [parse_dependency(x.strip()) for x in content]

steps_set = set()
for dep in dependencies:
    steps_set.add(dep[0])
    steps_set.add(dep[1])

steps = list(steps_set)

dependencies_map = {}
for dep in dependencies:
    step_first = dep[0]
    step_n = dep[1]
    if not (step_n in dependencies_map):
        dependencies_map[step_n] = set()

    dependencies_map[step_n].add(step_first)


def dependecies_fulfilled(step, steps_ready_set, deps_map):
    if step not in deps_map:
        return True

    for dep in deps_map[step]:
        if dep not in steps_ready_set:
            return False

    return True


steps_sorted = []
steps_to_sort = set(steps)
steps_sorted_set = set()

while len(steps_to_sort) > 0:
    new_steps_ready = []
    for step in steps_to_sort:
        if dependecies_fulfilled(step, steps_sorted_set, dependencies_map):
            new_steps_ready.append(step)

    new_steps_ready = sorted(new_steps_ready)
    new_steps_ready = new_steps_ready[0:1]
    for step in new_steps_ready:
        steps_sorted_set.add(step)
        steps_to_sort.remove(step)

    steps_sorted += new_steps_ready

print (''.join(steps_sorted))
