"""
@author : Alban CREPEL
@brief : tests of all the Session1's functions
"""

import S1_algotools as algo
import pytest
import numpy
import copy

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



# -----------------------------------------


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



# -----------------------------------------



def test_min_value_with_empty_list():
	"""
	Function that tests the function min_value 
	with an empty list
	"""
	list = []
	with pytest.raises(ValueError):
		res = algo.min_value(list)


def test_min_value_with_positive_values():
	"""
	Function that tests the function min_value 
	with a list of positive values
	"""
	list = [1,2,3,4,7]
	assert algo.min_value(list) == (1,0)

def test_min_value_with_negative_values():
	"""
	Function that tests the function min_value 
	with a list of negative values
	"""
	list = [-1,-2,-3,-4,-7]
	assert algo.min_value(list) == (-7,4)

def test_min_value_with_negative_and_positive_values():
	"""
	Function that tests the function min_value 
	with a list of both negative and positive values
	"""
	list = [1,-2,-3,-4,-7]
	assert algo.min_value(list) == (-7,4)


# -----------------------------------------

def test_reverse_table_with_empty_list():
	"""
	Function that tests the function reverse_table
	with an empty list
	"""
	list = []
	assert algo.reverse_table(list) == []

def test_reverse_table_with_odd_length():
	"""
	Function that tests the function reverse_table
	with a list of odd length
	"""
	list = [1,2,3,4,-7]
	assert list[::-1] == algo.reverse_table(list)


def test_reverse_table_with_event_length():
	"""
	Function that tests the function reverse_table
	with a list of event length
	"""
	list = [1,2,3,4,5,6]
	assert list[::-1] == algo.reverse_table(list)


# -----------------------------------------


def test_roi_bbox_with_normal_matrix():
	"""
	Function that tests the function roi_bbox
	with a normal matrix
	"""
	size_rows=10
	size_cols=10
	mat = numpy.zeros([size_rows,size_cols], dtype=int)
	  
	#filling the matrix
	mat[2:4,5:9] = 1   
	mat[4:7,7:9] = numpy.ones([3,2])  
	assert algo.roi_bbox(mat).all() == numpy.array([[2,5],[2,8],[6,5],[6,8]]).all()

def test_roi_bbox_with_single_one():
	"""
	Function that tests the function roi_bbox
	with a matrix composed of a single one
	"""
	size_rows=10
	size_cols=10
	mat = numpy.zeros([size_rows,size_cols], dtype=int)
	  
	#filling the matrix
	mat[2][2] = 1    
	assert algo.roi_bbox(mat).all() == numpy.array([[2,2],[2,2],[2,2],[2,2]]).all()	

def test_roi_bbox_with_only_zeros():
	"""
	Function that tests the function roi_bbox
	with a matrix composed of zeros only
	"""
	size_rows=10
	size_cols=10
	mat = numpy.zeros([size_rows,size_cols], dtype=int) 
	with pytest.raises(ValueError):
		res = algo.roi_bbox(mat)



# -----------------------------------------


def test_random_fill_sparse_with_empty_list():
	"""
	Function that tests the function random_fill_sparse
	with an empty list
	"""
	size = 0
	mat = numpy.full([size,size],'',dtype='str')
	with pytest.raises(ValueError):
		res = algo.random_fill_sparse(mat,6)


def test_random_fill_sparse_with_number_of_fills_too_high():
	"""
	Function that tests the function random_fill_sparse
	with a number of items to be filled higher than the length of the list
	"""
	size = 2
	mat = numpy.full([size,size],'',dtype='str')
	with pytest.raises(ValueError):
		res = algo.random_fill_sparse(mat,36)


def test_random_fill_sparse_with_normal_values():
	"""
	Function that tests the function random_fill_sparse
	with normal values
	"""
	count = 0
	size = 6
	mat = numpy.full([size,size],'',dtype='str')

	rows_length = mat.shape[0]
	cols_length = mat.shape[1]

	res = algo.random_fill_sparse(mat,6)
	
	for row in range(rows_length):
		for col in range(cols_length):
			if mat[row][col] == 'X':
				count += 1

	assert count == 6


# -----------------------------------------


def test_remove_whitespace_with_empty_string():
	"""
	Function that tests the function remove_whitespace
	with an empty string
	"""
	myString = ""
	myString = algo.remove_whitespace(myString)
	assert myString == ""


def test_remove_whitespace_with_spaced_string():
	"""
	Function that tests the function remove_whitespace
	with spaced string
	"""
	myString = "here is a string"
	replacedString = copy.deepcopy(myString).replace(" ","")
	myString = algo.remove_whitespace(myString)
	assert myString == replacedString


def test_remove_whitespace_with_unspaced_string():
	"""
	Function that tests the function remove_whitespace
	with an unspaced string
	"""
	myString = "hereisastring"
	myString = algo.remove_whitespace(myString)
	assert myString == "hereisastring"



# -----------------------------------------


def test_shuffle_with_empty_list():
	"""
	Function that tests the function shuffle
	with an empty list
	"""
	list = []
	list = algo.shuffle(list)
	assert list == []


def test_shuffle_with_normal_list():
	"""
	Function that tests the function shuffle
	with a normal list
	"""
	list = range(10)
	listCopy = copy.deepcopy(list)
	list = algo.shuffle(list)
	assert len(set(list).intersection(listCopy)) == len(list)


# -----------------------------------------


def test_sort_selective_with_empty_list():
	"""
	Function that tests the function sort_selective
	with an empty list
	"""
	list = []
	list = algo.sort_selective(list)
	assert list == []


def test_sort_selective_with_positive_values():
	"""
	Function that tests the function sort_selective
	with a list of positive values only
	"""
	list = [10, 15, 7, 1, 3, 3, 9]
	sortedList = sorted(copy.deepcopy(list))
	list = algo.sort_selective(list)
	assert list == sortedList


def test_sort_selective_with_positive_and_negative_values():
	"""
	Function that tests the function sort_selective
	with a list of both negative and positive values
	"""
	list = [10, -15, 7, -1, 3, 3, 9]
	sortedList = sorted(copy.deepcopy(list))
	list = algo.sort_selective(list)
	assert list == sortedList


def test_sort_selective_with_negative_values():
	"""
	Function that tests the function sort_selective
	with a list of negative values only
	"""
	list = [-10, -15, -7, -1, -3, -3, -9]
	sortedList = sorted(copy.deepcopy(list))
	list = algo.sort_selective(list)
	assert list == sortedList


# -----------------------------------------


def test_sort_bubble_with_empty_list():
	"""
	Function that tests the function sort_bubble
	with an empty list
	"""
	list = []
	list = algo.sort_bubble(list)
	assert list == []


def test_sort_bubble_with_positive_values():
	"""
	Function that tests the function sort_bubble
	with a list of positive values only
	"""
	list = [10, 15, 7, 1, 3, 3, 9]
	sortedList = sorted(copy.deepcopy(list))
	list = algo.sort_bubble(list)
	assert list == sortedList


def test_sort_bubble_with_positive_and_negative_values():
	"""
	Function that tests the function sort_bubble
	with a list of both negative and positive values
	"""
	list = [10, -15, -7, 1, 3, 3, 9]
	sortedList = sorted(copy.deepcopy(list))
	list = algo.sort_bubble(list)
	assert list == sortedList


def test_sort_bubble_with_negative_values():
	"""
	Function that tests the function sort_bubble
	with a list of negative values only
	"""
	list = [-10, -15, -7, -1, -3, -3, -9]
	sortedList = sorted(copy.deepcopy(list))
	list = algo.sort_bubble(list)
	assert list == sortedList