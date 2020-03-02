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

def append_team(comp_name):
    for i in range(len(comp_name)):
        comp_name[i] += ': F'
        ## adding F to show that processing has not been done yet
    
    comp_name = ';'.join([str(elem) for elem in comp_name])
    ## turning back to string

    with open('footy_comps.txt', 'a') as ofile:
        ## opening footy_comps file for appending the results
        ofile.write(comp_name)
        ofile.write('; ')
