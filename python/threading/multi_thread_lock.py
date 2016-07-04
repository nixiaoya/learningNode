#!/bin/env python
#coding=utf-8
'''
使用锁控制多线程间数据同步
用 threading 模块类似
'''

import thread  
import time  

mylock = thread.allocate_lock()  
num = 0  

def add_num(name):  
    global num  

    while True:  
        mylock.acquire() 
        print 'Thread %s locked! num=%s' % (name,str(num))  
        
        try:
            if num >= 5:  
                thread.exit_thread()  
            num += 1  
        finally:
            time.sleep(1)
            print 'Thread %s released! num=%s' % (name,str(num))  
            mylock.release()  

def test():  
    thread.start_new_thread(add_num, ('A',))  
    thread.start_new_thread(add_num, ('B',))  

if __name__ == '__main__':  
    test() 
    while True: #如果不加，主线程直接退出，看不到子线程的执行结果
       pass

