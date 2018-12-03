# See: https://adventofcode.com/2018/day/1#part1

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

content = [int(x.strip()) for x in content] 
print sum(content)