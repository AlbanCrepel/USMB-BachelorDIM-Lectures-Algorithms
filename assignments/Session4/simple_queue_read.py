# -*- coding : utf-8 -*-
"""
@author : Alban CREPEL
@brief : a simple example of queue reading
"""

import pika, os
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
	
channel.basic_consume(callback,
	queue='presentation',
	no_ack=True)

print(" [*] Waiting or messages. To exit press CTRL+C'")

channel.start_consuming()