"""
@author : Alban CREPEL
@brief : tests of all the Session1's functions
"""

import S1_algotools as algo
import pytest

def test_average_above_zero_with_positive_and_negative_values():
	"""
	Function that tests the function average_above_zero 
	with both negative and positive values
	"""
	list = [1,2,3,4,-7]
	assert algo.average_above_zero(list) == 2.5

def test_average_above_zero_with_negative_values():
	"""
	Function that tests the function average_above_zero 
	with negative values
	"""
	list = [-1,-2,-3,-4,-7]
	assert algo.average_above_zero(list) == 0

def test_average_above_zero_with_positive_values():
	"""
	Function that tests the function average_above_zero 
	with positive values
	"""
	list = [1,2,3,4]
	assert algo.average_above_zero(list) == 2.5


