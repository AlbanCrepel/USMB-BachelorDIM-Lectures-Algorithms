"""
@author : Alban CREPEL
@brief : a set of generic functions for data management
"""

def average_above_zero(table):
    """
    Basic function able to return the average of a list's values
    @param table : the table to be scanned
    """
    sum = 0
    n = 0
    for i in table:
        #select only positive values
        if i > 0:
            sum += i
            n += 1
    average = float(sum) / float(n)
    return float(average)

"""
#testing average_above_zero function
my_table = [1,2,3,4,-7]
result = average_above_zero(my_table)
message = "The average of positive elements of {list_values} is : {res}".format(list_values=my_table,res=result)
print(message)
"""

def max_value(table):
    """
    Basic function able to return the max value of a table
    @param table : the table to be scanned
    @throws a exception (ValueError) on an empty list
    """
    if len(table) == 0:
        raise ValueError("The list is empty")
        
    max_value = table[0]
    index_of_max_value = 0
    for index,item in enumerate(table):
        if item > max_value:
            max_value = item
            index_of_max_value = index
    return max_value,index_of_max_value
    
def min_value(table):
    """
    Basic function able to return the min value of a table
    @param table : the table to be scanned
    @throws a exception (ValueError) on an empty list
    """
    if len(table) == 0:
        raise ValueError("The list is empty")
        
    min_value = table[0]
    index_of_min_value = 0
    for index,item in enumerate(table):
        if item < min_value:
            min_value = item
            index_of_min_value = index
    return min_value,index_of_min_value
           
  
"""      
#testing max_value function
my_table = [1,2,3,4,-7]
result = max_value(my_table)
message = "The max value of {list_values} is : {value} at index {index}".format(list_values=my_table,value=result[0],index=result[1])
print(message)
"""

def reverse_table(table):
    """
    Basic function able to reverse a table
    @param table : the table to be scanned
    """
    index_of_opposite_element = len(table) - 1
    for i in range(len(table) / 2):
        current_value = table[i]
        table[i] = table[index_of_opposite_element]
        table[index_of_opposite_element] = current_value
        index_of_opposite_element -= 1
        
    return table

"""
#testingreverse_table function  
my_table = [1,2,3,4,-7]
#we store the string of the table because the initial table will change by address
initial_table = str(my_table)
reversed_table = reverse_table(my_table)
message = "The list {initial_table} reversed becomes {reversed_table}".format(initial_table=initial_table,reversed_table=reversed_table)
print(message)
"""

import numpy
def roi_bbox(input_image):
    """
    Function able to compute the corners' coordinates of an 'image'
    @param input_image : the 'image' to be scanned
    """
    a = b = c = d = 0
    list_x = []
    list_y = []
    rows_length = input_image.shape[0]
    cols_length = input_image.shape[1]
    
    for row in range(rows_length):
        for col in range(cols_length):
            if input_image[row][col] == 1:
                list_x.append(row)
                list_y.append(col)
                
    a = min_value(list_x)[0]
    b = min_value(list_y)[0]
    c = max_value(list_x)[0]
    d = max_value(list_y)[0]
    return numpy.array([[a,b],[a,d],[c,b],[c,d]])

"""
#testing the roi_bbox function   
size_rows=10
size_cols=10
my_mat = numpy.zeros([size_rows,size_cols], dtype=int)
  
#filling the matrix
my_mat[2:4,5:9] = 1   
my_mat[4:7,7:9] = numpy.ones([3,2])  
bounding_box = roi_bbox(my_mat)
print("The bounding box of the matrix is : " + str(bounding_box))
"""


import random
def random_fill_sparse(table,vfill):
    """
    Function able to fill a defined number of table cells
    @param table : the table to be filled
    @param vfill : the number of cells to be filled
    """
    fill_char = 'X'
    table_length = table.shape[0]
    nb_of_cells = table_length * table_length
    if vfill > nb_of_cells:
        raise ValueError("The number of cells to be filled is too high")
    
    for i in range(vfill):
        filled = False
        while filled == False:
            random_x = random.randint(0,table_length - 1)
            random_y = random.randint(0,table_length - 1)
            if table[random_x][random_y] != fill_char:
                table[random_x][random_y] = fill_char
                filled = True
        
    return table

"""
#testing the random_fill_sparse function  
size=5
my_mat = numpy.full([size,size],'',dtype='str')
filled_table = random_fill_sparse(my_mat,6)
print("Here is the filled table : " + str(filled_table))
"""

