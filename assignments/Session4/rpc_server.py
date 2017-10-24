# -*- coding : utf-8 -*-
"""
@author : Alban CREPEL
@brief : a simple example of a remote procedure call on the server side
"""

import pika, os
import msgpack
import msgpack_numpy as m
import numpy as np #if Numpy is required.

amqp_url='amqp://hflgmxzc:NAq2Gon5-i8fq_28URuADcF0jJnrpM8K@impala.rmq.cloudamqp.com/hflgmxzc'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

#initiate the connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def on_request(ch, method, props, body):
	"""
	Basic function able to process the message sent and reply to it
	"""
	decoded_message = msgpack.unpackb(str(body), object_hook = m.decode)
	print("Message received from client : " + decoded_message['value'])
	response = {"type":0, "value":"Fine, and you ?"}
	encoded_message = msgpack.packb(response, default = m.encode)
	print("Message sent to the client : " + response['value'])
	ch.basic_publish(exchange='', #reply
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                     	correlation_id = props.correlation_id),
                        body=encoded_message)
	ch.basic_ack(delivery_tag = method.delivery_tag) #acknowledge 


# wait for requests
channel.basic_qos(prefetch_count=1)


channel.basic_consume(on_request, queue='rpc_queue')

print(" [*] Waiting or messages. To exit press CTRL+C'")

channel.start_consuming()