#!/bin/env python
#coding=utf-8
# 任务：爬取疾病知识库的所有疾病的描述信息

'''
由于 GIL 的存在，python 在执行cpu密集型任务时，启用多线程效果并不明显
但是在IO密集型任务中，python多线程还是有用的。本例为使用多线程进行爬虫测试
'''

import re
import threading
import time
import urllib2
import socket

def MyException(Exception):
    pass

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

def getDiseaseLink(catgory_list, host):
    '''
    根据类型列表，获取各类型的疾病列表
    '''
    disease_dic = {}
    re1 = re.compile(r'\d+')
    re2 = re.compile(r'.*(/dkd/disease/.*/)".*') 
    
    for cat in catgory_list:
        page = 1
        disease_dic[cat] = []
        while True:
            
            replace_url = host +re1.sub(str(page), cat)
            try:
                content = getContent(replace_url)
            except Exception as e:
                break 
            else:
                links = getMatchItems(re2, content)
                if links:
                    disease_dic[cat].extend(links)
                    page += 1
                else:
                    break
    return disease_dic
                
def getDisease(disease_dic, host):
    '''
    获取疾病的描述信息
    '''
    re1 = re.compile(r'.*<p>(.*)</p>.*') 
    for k,v in disease_dic.items():
        for link in v:
            link = host + link
            time.sleep(1)
            try:
                content = getContent(link)
            except:
                print "Can't access to %s" % link
            else:
                introduction =  getMatchItems(re1, content)[0]
                print introduction 

def __main__():
    host = 'http://172.16.36.14'
    home = '/dkd/'

    category_list = getCategory(host + home)
    disease_dic = getDiseaseLink(category_list, host)
    #print disease_dic
    getDisease(disease_dic, host)
    
if __name__ == "__main__":
    __main__()
