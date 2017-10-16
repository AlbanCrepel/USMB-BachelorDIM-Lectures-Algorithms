# -*- coding : utf-8 -*-
"""
@author : Alban CREPEL
@brief : a simple example of queue reading
"""

import pika, os, argparse, time

parser = argparse.ArgumentParser(description='Adding an option to persist the messages')
parser.add_argument('-concurrency', action='store_true', help='persist the messages')

arg = parser.parse_args().concurrency


amqp_url='amqp://hflgmxzc:NAq2Gon5-i8fq_28URuADcF0jJnrpM8K@impala.rmq.cloudamqp.com/hflgmxzc'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5


counter = 0

#initiate the connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='presentation')

def callback(ch, method, properties, body):
	global counter
	counter += 1
	print(" [X] Received " + str(body))
	print("You received " + str(counter) + " message(s)")
	if arg:
		ch.basic_ack(delivery_tag = method.delivery_tag)

if arg:
	channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
	queue='presentation',
	no_ack=not arg)

print(" [*] Waiting or messages. To exit press CTRL+C'")

channel.start_consuming()