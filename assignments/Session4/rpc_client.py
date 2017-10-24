# -*- coding : utf-8 -*-
"""
@author : Alban CREPEL
@brief : a simple example of a remote procedure call on the client side
"""

import pika, os, uuid


amqp_url='amqp://hflgmxzc:NAq2Gon5-i8fq_28URuADcF0jJnrpM8K@impala.rmq.cloudamqp.com/hflgmxzc'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

#initiate the connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()


result = channel.queue_declare(exclusive=True)
callback_queue = result.method.queue

request_msg = "Hi, how fine ?"
print(request_msg)
corr_id = str(uuid.uuid4())
channel.basic_publish(exchange='',
                           routing_key='rpc_queue',
                           properties=pika.BasicProperties(
                                 reply_to = callback_queue,
                                 correlation_id = corr_id,),
                           body=request_msg)



response=None

def on_response(ch, method, props, body):
	"""
    Basic function able to process response from the server,
    """
    if corr_id == props.correlation_id:
        global response
        response=str(body)
        print(response)
    else:
    	raise ValueError("the correlation id does not match")

print('Starting to wait on the response queue...')

channel.basic_consume(on_response, no_ack=True,
                      queue=callback_queue)

while response is None: # wait for an answer
    connection.process_data_events()
connection.close()