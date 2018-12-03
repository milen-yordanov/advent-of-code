# See: https://adventofcode.com/2018/day/2#part2

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

content = [x.strip() for x in content] 

two_letters = 0
three_letters = 0

def ids_match(id1, id2):
    m = ''
    c = 0
    for i in range(len(id1)):
        if id1[i] == id2[i]:
            m += id1[i]
        else:
            c += 1

    if c != 1:
        m = None

    return m


match = None
input_count = len(content)
for i in range(input_count - 1):
    if match:
        break

    for j in range(i, input_count):
        match = ids_match(content[i], content[j]) 
        if match:
            break

print match
