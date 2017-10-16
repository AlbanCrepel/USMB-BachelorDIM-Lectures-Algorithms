# -*- coding : utf-8 -*-
"""
@author : Alban CREPEL
@brief : a simple example of queue publishing
"""

import pika, os, argparse

parser = argparse.ArgumentParser(description='Adding an option to persist the messages')
parser.add_argument('-concurrency', action='store_true', help='persist the messages')
parser.add_argument('-n', type=int, default=1, help='number of messages to be pusblished')

arg = parser.parse_args().concurrency

property = None

if arg:
	property = pika.BasicProperties(delivery_mode = 2)


amqp_url='amqp://hflgmxzc:NAq2Gon5-i8fq_28URuADcF0jJnrpM8K@impala.rmq.cloudamqp.com/hflgmxzc'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

#initiate the connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')


message = "Alban Crepel"

for i in range(parser.parse_args().n):
	channel.basic_publish(exchange='',
		routing_key='presentation',
		body=message,
		properties=property)

print(" [X] Username sent! " + str(parser.parse_args().n) + " messages sent.")

connection.close()