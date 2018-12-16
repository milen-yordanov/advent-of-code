# See: https://adventofcode.com/2018/day/3#part1

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

def parse_claim(claim_str):
    splits = claim_str.split()
    stl = splits[2].split(',')
    swh = splits[3].split('x')
    return {
        'left': int(stl[0]),
        'top':  int(stl[1].split(':')[0]),
        'width': int(swh[0]),
        'height': int(swh[1])
    }

#1 @ 906,735: 28x17
claims = [parse_claim(x.strip()) for x in content]

w, h = 1500, 1500;
matrix = [[0 for x in range(w)] for y in range(h)]

print ('claims {}'.format(len(claims)))
for claim in claims:
    for x in range(claim['left'], claim['left'] + claim['width']):
        for y in range(claim['top'], claim['top'] + claim['height']):
            matrix[x][y] += 1

overlaps = 0
for x in range(w):
    for y in range(h):
        if matrix[x][y] > 1:
            overlaps += 1

print ('overlaps: {}'.format(overlaps))
