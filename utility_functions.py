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
    comp_name = ';'.join([str(elem) for elem in comp_name])
    ## turning back to string

    with open('footy_comps.txt', 'a') as ofile:
        ## opening footy_comps file for appending the results
        ofile.write(comp_name)
        ofile.write('; ')

def find_comp(comp_content, comp_team):
    '''
    This function will find the competition if present in foot_comps.txt

    Arguments:
    comp_content -- the content from footy_comps.txt
    comp_team -- the inputed teams

    Returns:
    count -- index value where that particular competition has been found
    '''
    count = 0
        
    for comp in comp_content.split(';'):
        if comp.split(':')[0].strip() == comp_team.split(':')[0].strip():
            ## if competition matches breaking 
            break
        count += 1
    
    return count