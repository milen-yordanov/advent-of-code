# See: https://adventofcode.com/2018/day/3#part2

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

def parse_claim(claim_str):
    splits = claim_str.split()
    stl = splits[2].split(',')
    swh = splits[3].split('x')
    return {
        'id': int(splits[0][1:]),
        'left': int(stl[0]),
        'top':  int(stl[1].split(':')[0]),
        'width': int(swh[0]),
        'height': int(swh[1])
    }

#1 @ 906,735: 28x17
claims = [parse_claim(x.strip()) for x in content]

w, h = 1500, 1500;
matrix = [[0 for x in range(w)] for y in range(h)]
unoverlapped_claims = set()

for claim in claims:
    claim_id = claim['id']
    unoverlapped_claims.add(claim_id)
    for x in range(claim['left'], claim['left'] + claim['width']):
        for y in range(claim['top'], claim['top'] + claim['height']):
            if (matrix[x][y] > 0):
                unoverlapped_claims.discard(matrix[x][y])
                unoverlapped_claims.discard(claim_id)
            else:
                matrix[x][y] = claim_id

print unoverlapped_claims
