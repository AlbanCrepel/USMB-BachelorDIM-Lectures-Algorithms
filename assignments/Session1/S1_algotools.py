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
    if n == 0:
        return 0
    average = float(sum) / float(n)
    return float(average)

"""
#testing average_above_zero function
my_table = [-1,-2,-3,-4,-7]
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
    for i in range(int(len(table) / 2)):
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

    if len(list_x) == 0:
        raise ValueError("The list of x is empty")
    if len(list_y) == 0:
        raise ValueError("The list of y is empty")

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
size=6
my_mat = numpy.full([size,size],'',dtype='str')
filled_table = random_fill_sparse(my_mat,6)
print("Here is the filled table : " + str(filled_table))
"""

def remove_whitespace(table):
    """
    Function able to remove all whitespaces from a string
    @param table : the string we remove whitespaces from
    """

    nbOfCharactersDeleted = 0

    for index,character in enumerate(table):
        if character == " ":
            table = table[:index - nbOfCharactersDeleted] + table[index-nbOfCharactersDeleted+1 :]
            nbOfCharactersDeleted += 1

    return table

"""
#testing the remove_whitespace function  
myString = "here is a string"
print("Here is the string with whitespaces : " + myString)
myString = remove_whitespace(myString)
print("Here is the string without whitespaces : " + myString)
"""

def shuffle(list_in):
    """
    Function able to randomly select items of a list
    @param list_in : the list to be shuffled
    """
    for n in reversed(range(len(list_in))):
        randomIndex = random.randint(0, n)
        indexValue = list_in[randomIndex]

        list_in[randomIndex] = list_in[n]
        list_in[n] = indexValue


    return list_in

"""
#testing the shuffle function
myList = range(10)
print("list before shuffling : " + str(myList))
myList = shuffle(myList)
print("list after shuffling : " + str(myList))
"""

"""
1. Selective Sort
1.a)
10 15 7 1 3 3 9
We start going through our vector
1 is our minimum, we exchange 10 and 1 and restart from the index 1
we now have 1 15 7 10 3 3 9
the second 3 is our minimum, we exchange 15 and 3 and restart from index 2
we now have 1 3 7 10 15 3 9
the other 3 is our minimum, we exchange 7 and 3 and restart from index 3
we now have 1 3 3 10 15 7 9
7 is our minimum, we exchange 10 and 7 and restart from index 4
we now have 1 3 3 7 15 10 9
9 is our minimum, we exchange 15 and 9 and restart from index 5
we now have 1 3 3 7 9 10 15
there are no permutation, so the the vector is sorted
1.b) No the number of iterations doesn't depend on the vector content
1.c) 6 iterations are required to sort the vector (in 2 last items are already sorted in the last iteration)
1.d) 5 permutations are applied
1.e) 7(7-1)/2 = 21 So 21 comparisons are applied
1.f) The complexity of this algorithm is O(n^2)
1.g) In the worst case of vector, we have
n = 50 : 49 permutation, 50(50-1)/2 = 1225 comparisons
n = 100 : 99 permutations, 100(100-1)/2 = 4950 comparisons
n = 500 : 499 permutations, 500(500-1)/2 = 124750 comparisons
"""

def sort_selective(list_in):
    """
    Function able to sort a list
    @param list_in : the list to be sorted
    """
    for i in range(len(list_in) -1):
        minIndex = i
        for j in range(i, len(list_in)):
            if list_in[j] < list_in[minIndex]:
                minIndex = j

        if minIndex != i:
            tempValue = list_in[i]
            list_in[i] = list_in[minIndex]
            list_in[minIndex] = tempValue

    return list_in

"""
#testing the sort_selective function
myList = [10, 15, 7, 1, 3, 3, 9]
print("list before sorting : " + str(myList))
myList = sort_selective(myList)
print("list after sorting : " + str(myList))
"""

"""
2. Bubble Sort
2.a) 
10 15 7 1 3 3 9
We start going through our vector
We exchange 15 and 7
we now have 10 7 15 1 3 3 9
We exchange 15 and 1
we now have 10 7 1 15 3 3 9
We exchange 3 and 15
we now have 10 7 1 3 15 3 9
We exchange 3 and 15
we now have 10 7 1 3 3 15 9
We exchange 9 and 15
we now have 10 7 1 3 3 9 15
***We restart going through our vector from the beginning
we exchange 10 and 7
we now have 7 10 1 3 3 9 15
we exchange 10 and 1
we now have 7 1 10 3 3 9 15
we exchange 10 and 3
we now have 7 1 3 10 3 9 15
we exchange 10 and 3
we now have 7 1 3 3 10 9 15
we exchange 10 and 9
we now have 7 1 3 3 9 10 15
***We restart going through our vector from the beginning
we exchange 7 and 1
we now have 1 7 3 3 9 10 15
we exchange 7 and 3
we now have 1 3 7 3 9 10 15
we exchange 7 and 3
we now have 1 3 3 7 9 10 15
***We restart going through our vector from the beginning
there are no permutation, so the the vector is sorted
2.b) Yes the number of iterations depend on the vector content
2.c) 4 iterations are needed to sort the vector
2.d) 13 permutations are applied
2.e) 24 comparisons are applied
2.f) The complexity of this algorithm is O(n^2)
1.g) In the worst case of vector, we have
n = 50 : 1225-50 = 1175 permutation, 50(50-1)/2 = 1225 comparisons
n = 100 : 4950 - 100 = 4850 permutations, 100(100-1)/2 = 4950 comparisons
n = 500 : 124750 - 500 = 124250 permutations, 500(500-1)/2 = 124750 comparisons
"""

def sort_bubble(list_in):
    """
    Function able to sort a list
    @param list_in : the list to be sorted
    """
    permutations = True
    while permutations == True:
        permutations = False
        for i in range(1, len(list_in)):
            if list_in[i-1] > list_in[i]:
                tempValue = list_in[i]
                list_in[i] = list_in[i-1]
                list_in[i-1] = tempValue
                permutations = True

    return list_in

"""
#testing the sort_bubble function
myList = [10, 15, 7, 1, 3, 3, 9]
print("list before sorting : " + str(myList))
myList = sort_bubble(myList)
print("list after sorting : " + str(myList))
"""