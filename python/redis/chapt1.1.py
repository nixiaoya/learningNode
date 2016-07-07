#!/bin/env python
# chapter 1 exercies 1

import redis

r = redis.Redis()

pipe = r.pipeline()

pipe.set('count', 1)

pipe.incrby('count', 10)

print pipe.execute()
