"""
@author : Alban CREPEL
@brief : a set of generic functions for data management
"""

def average_above_zero(list):
    """
    
    """
    sum = 0
    n = 0
    for i in list:
        #select only positive values
        if i > 0:
            sum += i
            n += 1
    average = float(sum) / float(n)
    return float(average)

my_list = [1,2,3,4,-7]
result = average_above_zero(my_list)
message = "The average of positive elements of {list_values} is : {res}".format(list_values=my_list,res=result)
print(message)