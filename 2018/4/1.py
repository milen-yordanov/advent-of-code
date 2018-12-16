# See: https://adventofcode.com/2018/day/4#part1

import re
import pprint

input_file_name = 'input.txt'

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
records = sorted(records, key=lambda k: k['ts']) 


guard_id = 0
falls_asleep_min = 0
guard_asleep = {}
for rec in records:
    if (guard_id == 0) and (rec['action'] != 'Guard'):
        print ('Skip record {}'.format(rec))
        continue

    if rec['action'] == 'Guard':
        guard_id = rec['guard_id']
      
    if rec['action'] == 'falls':
        falls_asleep_min = rec['minute']

    if rec['action'] == 'wakes':
        wakes_up_min = rec['minute']
        if not (guard_id in guard_asleep):
            guard_asleep[guard_id] = []

        guard_asleep[guard_id].append( (falls_asleep_min, wakes_up_min) )

guard_asleep_total = []
for guard_id in guard_asleep:
    intervals = guard_asleep[guard_id]
    total_asleep = 0
    for interval in intervals:
        total_asleep += interval[1] - interval[0]

    guard_asleep_total.append({
        'guard_id': guard_id,
        'total_asleep': total_asleep,
    })

guard_asleep_total = sorted(guard_asleep_total, key=lambda k: k['total_asleep']) 
most_asleep_guard_id = guard_asleep_total[-1]['guard_id']

asleep_minutes_stats = [0 for x in range(60)]
for interval in guard_asleep[most_asleep_guard_id]:
    for i in range(interval[0], interval[1]):
        asleep_minutes_stats[i] += 1

asleep_most_during_minute = asleep_minutes_stats.index(max(asleep_minutes_stats))

print (asleep_most_during_minute * most_asleep_guard_id)