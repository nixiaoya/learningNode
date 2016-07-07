#!/bin/env python
# chapter 1 exercies 1

import redis

r = redis.Redis()

for c in ['hi', 'hello']:
    r.rpush('comments', c)

