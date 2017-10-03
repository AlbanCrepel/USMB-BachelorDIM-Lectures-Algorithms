"""
@author : Alban CREPEL
@brief : a set of generic functions for data management
"""

import numpy
import random

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

    if len(list_x) == 0 or len(list_y) == 0:
        raise ValueError("The lists are empty")

    a = min_value(list_x)[0]
    b = min_value(list_y)[0]
    c = max_value(list_x)[0]
    d = max_value(list_y)[0]
    return numpy.array([[a,b],[a,d],[c,b],[c,d]])



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


def remove_whitespace(table):
    """
    Function able to remove all whitespaces from a string
    @param table : the string we remove whitespaces from
    """

    nb_of_characters_deleted = 0

    for index,character in enumerate(table):
        if character == " ":
            table = table[:index - nb_of_characters_deleted] + table[index-nb_of_characters_deleted+1 :]
            nb_of_characters_deleted += 1

    return table


def shuffle(list_in):
    """
    Function able to randomly select items of a list
    @param list_in : the list to be shuffled
    """
    for n in reversed(range(len(list_in))):
        random_index = random.randint(0, n)
        index_value = list_in[random_index]

        list_in[random_index] = list_in[n]
        list_in[n] = index_value


    return list_in


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
        min_index = i
        for j in range(i, len(list_in)):
            if list_in[j] < list_in[min_index]:
                min_index = j

        if min_index != i:
            temp_value = list_in[i]
            list_in[i] = list_in[min_index]
            list_in[min_index] = temp_value

    return list_in


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
                temp_value = list_in[i]
                list_in[i] = list_in[i-1]
                list_in[i-1] = temp_value
                permutations = True

    return list_in
