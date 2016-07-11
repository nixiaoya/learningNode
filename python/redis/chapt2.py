#!/bin/env python
# chapter 2  

import redis
import csv
import time

def multiLoader(user_list, r):
    pipe = r.pipeline()

    for email, user in user_list:
        pipe.set(email, user)
    pipe.execute()

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
            user_list.append((email, first_name))
            set_count += 1

            if set_count % 1000 == 0:
                multiLoader(user_list, r)
                user_list = []

end_time = int(time.time())
print "%d items in #%d seconds" % (set_count, end_time - start_time)
