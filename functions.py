'''
functions.py
------------

'''

import os
import utility_functions as uf

def enlist_team(team_names):
    '''
    The function will write the team name/s into the text files.

    Arguments:
    team_names -- string representing team name/s

    Returns:
    None
    '''
    for i in range(len(team_names)):
        team_names[i] += '--F'
    
    team_names = ','.join([str(elem) for elem in team_names])

    with open('footy_teams.txt', 'a') as ofile:
        ## opening the file to write/append the content in it
        ofile.write(team_names)
        ofile.write(', ') 

def preview_teams():
    '''
    The function will display all the added teams.

    Arguments:
    None

    Returns:
    None
    '''
    with open('footy_teams.txt', 'r') as ofile:
        ## opening the file to read the content in it
        content = ofile.readline()
        
    team_names = content.split(',')
    team_names = [x.strip() for x in team_names]

    if len(team_names) == 2:
        i = -1

    for i in range(len(team_names) - 2):
        print(team_names[i][:-3], end=', ')
    print(team_names[i+1][:-3])

def del_teams(del_team_names):
    '''
    The function will delete the team names specified from team name file.

    Arguments:
    del_team_names -- string containing team names

    Return:
    None
    '''

    del_team_names = [x.strip() for x in del_team_names]

    with open('footy_teams.txt', 'r') as ofile:
        content_team = ofile.readline()

    team_names = content_team.split(',')
    team_names = [x.strip() for x in team_names]
    temp_team_names = [x[:-3] for x in team_names]

    non_del_teams = uf.not_intersection(temp_team_names, del_team_names)

    tf_value = ''

    for final_names in non_del_teams:
        for real_names in team_names:
            if final_names == real_names[:-3] and (final_names != '' or real_names != ''):
                tf_value += real_names[-1]
    
    for i in range(len(non_del_teams) - 1):
        non_del_teams[i] += f'--{tf_value[i]}'

    end_result = ', '.join([str(elem) for elem in non_del_teams])

    if end_result == '':
        os.remove('footy_teams.txt')

    else:
        with open('footy_teams.txt', 'w') as ofile:
            ofile.write(end_result)
    
def enlist_comp(comp_name):
    '''
    This function will write competition's name and respective 
    teams into footy_comps.txt

    Arguments:
    comp_name: list of competition names

    Returns:
    None
    '''

    if 'footy_comps.txt' in  os.listdir():
        with open('footy_comps.txt'):
            pass
    
    ## HERE

    for i in range(len(comp_name)):
        comp_name[i] += ': F'
        ## adding F to show that processing has not been done yet
    
    comp_name = ';'.join([str(elem) for elem in comp_name])
    ## turning back to string

    with open('footy_comps.txt', 'a') as ofile:
        ## opening footy_comps file for appending the results
        ofile.write(comp_name)
        ofile.write('; ')

def preview_comps():
    '''
    This function displays all the competitions that
    has been saved by the user.

    Arguments:
    None

    Returns:
    None
    '''
    with open('footy_comps.txt', 'r') as ofile:
        ## opening text file for reading
        comp_content = ofile.readline()
        ## reading the content on the first line
    
    comp_content = comp_content.split(';')

    for comp in comp_content:
        print(comp[:-3].strip())

def del_comps(del_comp_names):
    '''
    This function will remove added competitions.

    Arguments:
    del_comp_names -- string, competition names in required order.

    Returns:
    None
    '''

    iterate_del_names = del_comp_names.split(';')
    iterate_del_names = [x.strip() for x in iterate_del_names]

    for comp_team in iterate_del_names:
        
        with open('footy_comps.txt', 'r') as ofile:
            comp_content = ofile.readline()
            ## reading the content from the first line
        
        count = 0
        
        for comp in comp_content.split(';'):
            if comp.split(':')[0].strip() == comp_team.split(':')[0].strip():
                break
            count += 1
        ## finding out matching teams

        selected_teams_del = comp_team.split(';')[0].split(':')[1:]
        selected_teams_del = selected_teams_del[0].split(',')
        selected_teams_del = [x.strip() for x in selected_teams_del]

        selected_teams = comp_content.split(';')[count].strip().split(':')[1]
        selected_teams = selected_teams.split(',')
        selected_teams = [x.strip() for x in selected_teams]
        ## picking up the selected teams

        del_final = uf.not_intersection(selected_teams, selected_teams_del)

        if del_final == []:
            temp_comp = comp_content.split(';')
            del temp_comp[count]
            final_result = ';'.join(str(elem) for elem in temp_comp)
            
        else:
            temp_comp = comp_content.split(';')[count].split(':')[0].strip()
            tf_value = comp_content.split(';')[count].split(':')[2].strip()
            temp_comp += ': '
            final_result = ''

            for team in del_final:
                temp_comp += team + ', '
            temp_comp = temp_comp[:-2] + f': {tf_value}'

            comp_temp = comp_content.split(';')
            for i in range(len(comp_temp) - 1):
                if i == count:
                    final_result += ' ' + temp_comp
                else:
                    final_result += comp_temp[i]
                final_result += ';'
                
            if final_result[0] == ' ':
                final_result = final_result[1:]
        
        if final_result == '':
            os.remove('footy_comps.txt')
        else:
            with open('footy_comps.txt', 'w') as ofile:
                ofile.write(final_result)
        