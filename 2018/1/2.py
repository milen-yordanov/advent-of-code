# See: https://adventofcode.com/2018/day/1#part2

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]

seen_frequencies = set()
frequency = 0
frequency_reached_twice = None

seen_frequencies.add(frequency)
while frequency_reached_twice is None:
    for c in content:
        frequency += c
        if frequency in seen_frequencies:
            frequency_reached_twice = frequency
            break
        seen_frequencies.add(frequency)

print frequency_reached_twice
