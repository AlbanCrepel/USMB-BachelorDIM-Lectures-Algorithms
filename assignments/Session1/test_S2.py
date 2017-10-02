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


def test_max_value_with_empty_list():
	"""
	Function that tests the function max_value 
	with an empty list
	"""
	list = []
	with pytest.raises(ValueError):
		res = algo.max_value(list)

def test_max_value_with_positive_values():
	"""
	Function that tests the function max_value 
	with a list of positive values
	"""
	list = [1,2,3,4,7]
	assert algo.max_value(list) == (7,4)

def test_max_value_with_negative_values():
	"""
	Function that tests the function max_value 
	with a list of negative values
	"""
	list = [-1,-2,-3,-4,-7]
	assert algo.max_value(list) == (-1,0)

def test_max_value_with_negative_and_positive_values():
	"""
	Function that tests the function max_value 
	with a list of both negative and positive values
	"""
	list = [1,-2,-3,-4,-7]
	assert algo.max_value(list) == (1,0)