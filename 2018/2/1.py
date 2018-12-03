# See: https://adventofcode.com/2018/day/2#part1

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

content = [x.strip() for x in content] 

two_letters = 0
three_letters = 0

def contains_letters(id, lc):
    letter_count = {}
    for letter in id:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    count = 0
    for letter in letter_count:
        if letter_count[letter] == lc:
            count += 1

    if count > 1:
        count = 1

    return count

for id in content:
    two_letters += contains_letters(id, 2)
    three_letters += contains_letters(id, 3)


checksum = two_letters * three_letters
print checksum