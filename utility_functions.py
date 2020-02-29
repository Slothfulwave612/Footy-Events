'''
utility_functions.py
--------------------

'''

def not_intersection(lst1, lst2): 
    '''
    This function compares two lists and gives the intersection of the two.

    Arguments:
    lst1 -- list data-type
    lst2 -- list date-type

    Returns:
    lst3 -- intersection of lst1 and lst2
    '''
    lst3 = [value for value in lst1 if value not in lst2] 
    return lst3 
