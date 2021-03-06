#-*- coding-utf-8 -*-
#!/bin/env python

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'annoymouse.info'

message = ' '.join(sys.argv[2:]) or 'info: Hello World!'

channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)

print '[X] Sent %r:%r' % (routing_key,message,)

connection.close()
