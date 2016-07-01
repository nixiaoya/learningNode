#!/usr/bin/env python
#coding=utf-8
#

import logging
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.options
import os,sys,json

from tornado.options import define,options

define("port",default=8080,help="run on the given prot",type=int)
define("static",default="/appstatic/tornado",help="all static file dirs",type=str)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/websocket",Chat),
            (r"/chat",MainHandler),
            (r"/testdata/users",UserList),
        ]
        settings = dict(
                debug = True,
                template_path =  os.path.join(os.path.dirname(__file__), "templates"),
            )
        tornado.web.Application.__init__(self,handlers,**settings)

class UserList(tornado.web.RequestHandler):
    def get(self):
        uid = self.get_argument('uid',default=0,strip=True)
        uid = int(uid)
        users = [
            {"id":1,"name":"jack","age":11,"photo":"img/jack.png","is_male":True},
            {"id":2,"name":"jim","age":12,"photo":"img/jim.png","is_male":True},
            {"id":3,"name":"Tom","age":9,"photo":"img/tom.png","is_male":False},
            {"id":4,"name":"haha","age":13,"photo":"img/haha.png","is_male":False},
        ]
        if uid != 0 and uid <= len(users):
            user = users[uid-1]
        else:
            user = users
        self.set_header("Content-Type","application/json;charset=UTF-8")
        self.write(json.dumps(user))

### handler ###
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            static = options.static,
            )

class Chat(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 200
    count = 0

    def allow_draft76(self):
        return True

    def open(self):
        print "new client opened"
        Chat.waiters.add(self)

    def on_close(self):
        Chat.waiters.remove(self)

    @classmethod
    def update_cache(cls,chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cache_size:]

    @classmethod
    def send_updates(cls,chat):
        tmp = {"msg":chat,"c1":Chat.count,"c2":len(Chat.waiters)}
        logging.info("sending msg to %d waiters",len(cls.waiters))
        for w in cls.waiters:
            try:
                w.write_message(tmp)
            except:
                logging.error("Error sending msg",exc_info=True)

    def on_message(self,message):
        logging.info("got message %r",message)
        Chat.send_updates(message)
        Chat.count += 1

    def check_origin(self, origin):
        return True

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

