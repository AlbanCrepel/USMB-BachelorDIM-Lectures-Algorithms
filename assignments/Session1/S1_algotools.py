"""
@author : Alban CREPEL
@brief : a set of generic functions for data management
"""

def average_above_zero(table):
    """
    Basic function able to return the average of a list's values
    @param list : the list to be scanned
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
my_list = [1,2,3,4,-7]
result = average_above_zero(my_list)
message = "The average of positive elements of {list_values} is : {res}".format(list_values=my_list,res=result)
print(message)
"""

def max_value(table):
    """
    Basic function able to return the max value of a list
    @param list : the list to be scanned
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
           
  
"""        
#testing max_value function
my_list = [1,2,3,4,-7]
result = max_value(my_list)
message = "The max value of {list_values} is : {value} at index {index}".format(list_values=my_list,value=result[0],index=result[1])
print(message)
"""

