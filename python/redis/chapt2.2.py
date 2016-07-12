#!/bin/env python
# chapter 2 : redis cluster 

from rediscluster import StrictRedisCluster
import csv
import time

def multiLoader(user_list, r):
    for email, user in user_list:
        r.set(email, user)

startup_nodes = [
        {"host":"127.0.0.1", "port":"6379"},
        {"host":"127.0.0.1", "port":"6380"},
        {"host":"127.0.0.1", "port":"6381"}
    ]
rc = StrictRedisCluster(startup_nodes=startup_nodes)
set_count = 0
start_time = int(time.time())

rc.flushall()

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
                multiLoader(user_list, rc)
                user_list = []

end_time = int(time.time())
print "%d items in #%d seconds" % (set_count, end_time - start_time)
