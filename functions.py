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

    with open('footy_teams_comps.txt', 'a') as ofile:
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
    with open('footy_teams_comps.txt', 'r') as ofile:
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

    with open('footy_teams_comps.txt', 'r') as ofile:
        content_team = ofile.readline()
        content_comp = ofile.readline()

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

    if end_result == '' and content_comp == '':
        os.remove('footy_teams_comps.txt')

    else:
        with open('footy_teams_comps.txt', 'w') as ofile:
            if end_result == '':
                end_result = '\n'
            ofile.write(end_result)
            ofile.write(content_comp)