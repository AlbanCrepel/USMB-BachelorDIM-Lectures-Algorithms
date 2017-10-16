# -*- coding : utf-8 -*-
"""
@author : Alban CREPEL
@brief : a simple example of queue publishing or reading whether the argument -read is passed when calling the script
"""

import argparse, os


parser = argparse.ArgumentParser(description='Adding an option to read the queues')
parser.add_argument('-read', action='store_true', help='read the queues')

arg = parser.parse_args().read

if arg:
	os.system('python simple_queue_read.py')
else:
	os.system('python simple_queue_publish.py')