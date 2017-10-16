# -*- coding : utf-8 -*-
"""
@author : Alban CREPEL
@brief : a simple example of queue publishing or reading whether the argument -read is passed when calling the script
"""

import argparse, os


parser = argparse.ArgumentParser(description='Adding an option to read the queues')
parser.add_argument('-read', action='store_true', help='read the queues')
parser.add_argument('-concurrency', action='store_true', help='persist the messages')

arg = parser.parse_args().read
concurrency = parser.parse_args().concurrency

if concurrency:
	os.system('python simple_queue_read.py -concurrency')
	os.system('python simple_queue_read.py -concurrency')
	os.system('python simple_queue_publish.py -concurrency -n 100')
elif arg:
	os.system('python simple_queue_read.py' + additional_parameters)
	os.system('python simple_queue_read.py' + additional_parameters)
else:
	os.system('python simple_queue_publish.py' + additional_parameters)