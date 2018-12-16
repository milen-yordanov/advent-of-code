# See: https://adventofcode.com/2018/day/4#part1

import re
import pprint

input_file_name = 'input-test.txt'

with open(input_file_name) as f:
    content = f.readlines()

def parse_record(record_str):
    # [1518-11-01 00:00] Guard #10 begins shift
    splits = re.split(' |\\[|\\]|:|#',record_str)
    date = splits[1]
    hour = int(splits[2])
    minute = int(splits[3])
    action = splits[5]
    guard_id = 0
    if action == 'Guard':
        guard_id = int(splits[7])

    return {
       'date': date,
       'hour':  hour,
       'minute': minute,
       'action': action,
       'guard_id': guard_id, 
       'ts': '{} {}:{}'.format(splits[1], splits[2], splits[3])
    }

records = [parse_record(x.strip()) for x in content]
pprint.pprint(records)
# print records

