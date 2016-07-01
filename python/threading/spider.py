#!/bin/env python
#coding=utf-8
# 任务：爬取疾病知识库的所有疾病的描述信息

'''
由于 GIL 的存在，python 在执行cpu密集型任务时，启用多线程效果并不明显
但是在IO密集型任务中，python多线程还是有用的。本例为使用多线程进行爬虫测试
'''

import re
import threading
import Queue
import time
import urllib2
import socket

def MyException(Exception):
    pass

class Consumer(threading.Thread):
    def __init__(self, queue, target):
       threading.Thread.__init__(self)
       self._queue = queue
       self._target = target

    def run(self):
        while True:
            content = self._queue.get()
            if isinstance(content, str) and content == 'quit':
                break
            self._target(content)
            print self.getName(),content
            
def Poll(queue, target, size):
    workers = []
    for _ in range(size):
        worker = Consumer(queue, target)
        worker.start()
        workers.append(worker)
    return workers

def Producer(urls, type, threads=4):
    queue = Queue.Queue()
    if type == "disease_list":
        target = getDiseaseLink
    else:
        target = getDisease
    worker_threads = Poll(queue, target, threads)
    start_time = time.time()

    for url in urls:
        queue.put(url)

    for worker in worker_threads:
        queue.put('quit')

    for worker in worker_threads:
        worker.join()

    print 'Done! Time taken: {}'.format(time.time() - start_time)
   
def getContent(req_url, req_data={}):
    '''
    处理http请求和响应 
    '''
    header = { 
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'
        }       
    if req_data:
        req_data = urllib.urlencode(req_data)
        req = urllib2.Request(req_url, req_data, header)
    else:
        req = urllib2.Request(req_url)

    try:
        resp = urllib2.urlopen(req, timeout=5)
    except urllib2.HTTPError as e:
        raise MyException("HttpError: code=>%s reason=>%s" % (e.code,e.reason))
    except urllib2.URLError as e:
        raise MyException("URLError: %s" % e.reason)
    except socket.timeout as e:
        raise MyException("Socket timeout:%s" % e)
    else:
        return resp.read()

def getMatchItems(re1, content):
    match_items = []
    if re1.search(content):
        for link in re1.findall(content):
            if link not in match_items:
                match_items.append(link)
    return match_items

def getCategory(req_url):
    '''
    获取类型列表 
    '''
    re1 = re.compile(r'.*(/dkd/category/.*/1/).*') 
    content = getContent(req_url)
    return getMatchItems(re1, content)

def getDiseaseLink(catgory):
    '''
    根据类型列表，获取各类型的疾病列表
    '''
    global disease_list
    global host
    global lock
    
    re1 = re.compile(r'\d+')
    re2 = re.compile(r'.*(/dkd/disease/.*/)".*') 
    
    page = 1
    while True:
        replace_url = host +re1.sub(str(page), catgory)
        try:
            content = getContent(replace_url)
        except Exception as e:
            break 
        else:
            links = getMatchItems(re2, content)
            
            if links:
                lock.acquire()
                try:
                    page += 1
                    for link in links:
                        if link not in disease_list:
                            disease_list.append(link)
                finally:
                    lock.release()
            else:
                break
                    
    return disease_list
                
def getDisease(disease_link):
    '''
    获取疾病的描述信息
    '''
    global host
    global disease_list
    global disease_info
    re1 = re.compile(r'.*<p>(.*)</p>.*')
    
    link = host + disease_link
    time.sleep(1)
    try:
        content = getContent(link)
    except:
        print "Can't access to %s" % link
    else:
        introduction =  getMatchItems(re1, content)[0]
        print introduction 

def __main__():
    global host
    global disease_list
    home = '/dkd/'
   
    category_list = getCategory(host + home)
    Producer(category_list, 'disease_list', 4)
    Producer(disease_list, 'disease', 4)
    
if __name__ == "__main__":
    host = 'http://172.16.36.14'
    disease_list = []
    disease_info = []
    lock = threading.Lock()
    lock2 = threading.Lock()
    __main__()
