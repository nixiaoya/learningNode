#!/bin/env python
# chapter 2 

import redis
import csv
import time


r = redis.Redis(host='127.0.0.1', port=6379)
set_count = 0
start_time = int(time.time())

r.flushall()

with open('users.csv', 'rU') as fd:
    csvreader = csv.reader(fd)
    user_list = []
    
    for line in csvreader:
        if csvreader.line_num == 1:
            continue
        email = line[0].strip()
        first_name = line[1].strip()

        if email and first_name:
            r.set(email, first_name)
            set_count += 1

end_time = int(time.time())
print "%d items in #%d seconds" % (set_count, end_time - start_time)
