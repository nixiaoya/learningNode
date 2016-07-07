#!/bin/env python
# chapter 1 exercies 1

import redis

r = redis.Redis()

while True:
    print r.brpop('comments')
