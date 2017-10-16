# -*- coding : utf-8 -*-
"""
@author : Alban CREPEL
@brief : a simple example of queue publishing
"""

import pika, os
amqp_url='amqp://hflgmxzc:NAq2Gon5-i8fq_28URuADcF0jJnrpM8K@impala.rmq.cloudamqp.com/hflgmxzc'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

#initiate the connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')


message = "Alban Crepel"

channel.basic_publish(exchange='',
	routing_key='presentation',
	body=message)

print(" [X] Username sent!'")

connection.close()