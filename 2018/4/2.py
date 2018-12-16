# See: https://adventofcode.com/2018/day/4#part2

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


guard_asleep_stats = []
for guard_id in guard_asleep:
    intervals = guard_asleep[guard_id]
    minutes_stats = [0 for x in range(60)]
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            minutes_stats[i] += 1

    guard_asleep_stats.append({
        'guard_id': guard_id,
        'max_val': max(minutes_stats),
        'max_val_index': minutes_stats.index(max(minutes_stats))
    })

guard_asleep_stats = sorted(guard_asleep_stats, key=lambda k: k['max_val'])
guard = guard_asleep_stats[-1]
print (guard['guard_id'] * guard['max_val_index'])
