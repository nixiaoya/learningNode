#!/bin/env python
#coding=utf-8
'''
使用队列在线程间同步数据
'''

from Queue import Queue  

import random  
import threading  
import time  

class Producer(threading.Thread):  
    def __init__(self, t_name, queue):  
        threading.Thread.__init__(self, name=t_name)  
        self.data=queue  

    def run(self):  
        for i in range(5):  
            print "%s: %s is producing %d to the queue!" %(time.ctime(), self.getName(), i)  
            self.data.put(i)  
            time.sleep(random.randrange(10)/5)  
        
        print "%s: %s finished!" %(time.ctime(), self.getName())  

class Consumer(threading.Thread):  
    def __init__(self, t_name, queue):  
        threading.Thread.__init__(self, name=t_name)  
        self.data=queue  

    def run(self):  
        for i in range(5):  
            val = self.data.get()  
            print "%s: %s is consuming. %d in the queue is consumed!" %(time.ctime(), self.getName(), val)  
            time.sleep(random.randrange(10))  

        print "%s: %s finished!" %(time.ctime(), self.getName())  

def main():  
    queue = Queue()  
    producer = Producer('Pro.', queue)  
    consumer = Consumer('Con.', queue)  
    producer.start()  
    consumer.start()  
    producer.join()  
    consumer.join()  
    print 'All threads terminate!'  

if __name__ == '__main__':  
    main()

