#!/bin/env python
#-*- encoding:utf-8 -*-
'''
生成器测试
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Fab(object):
    def __init__(self, _max):
        self._max = _max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self._max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        raise StopIteration #当超出迭代边界时，终止迭代，否则会一直返回 None
    

#DEF Fab(_max):
#    a, b, n = 0, 1, 0
#
#    while n < _max:
#        yield b 
#        a, b = b, a+b
#        n += 1

for x in Fab(5):
    print x
