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

    if len(team_names) == 1:
        i = -1

    for i in range(len(team_names) - 2):
        print(team_names[i], end=', ')
    print(team_names[i+1])

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
    temp_team_names = [x for x in team_names]

    non_del_teams = uf.not_intersection(temp_team_names, del_team_names)

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
        for comp_index in comp_name:
            with open('footy_comps.txt', 'r') as ofile:
                comp_content = ofile.readline()
                ## reading the content of the file

            comp_content = comp_content.split(';')
            comp_content = [x.strip() for x in comp_content]
            ## making a list of all competition with the team names
            
            input_comp = comp_index.split(':')[0].strip()
            ## the user input competition name

            count = 0
            ## a counter to find where the competition is in comp_content

            for comp in comp_content:
                if comp.split(':')[0].strip() == input_comp:
                    ## if the competition name has been matched
                    ## breaking the for loop 
                    break
                count += 1

            if count != len(comp_content):
                main_comp = comp_content[count].split(':')
                main_comp = [x.strip() for x in main_comp]
                ## a splitted list containing competiton name, team names and true false value

                team_names = main_comp[1].split(',')
                team_names = [x.strip() for x in team_names]
                ## making a list of all team names

                input_teams = comp_index.split(':')[1].split(',')
                input_teams = [x.strip() for x in input_teams]
                ## making a list of all team names entered by the user

                for team in input_teams:
                    if team not in team_names:
                        team_names.append(team)
                ## checking for whether dupicate team has been entered or not
                print(team_names)
                team_names = ', '.join(elem for elem in team_names)
                ## converting list to string

                team_comp = main_comp[0] + ': ' + team_names
                ## after appending the team name the update competiton

                final_result = ''

                for i in range(len(comp_content) - 1):
                    if i == count:
                        final_result += team_comp
                    else:
                        final_result += comp_content[i]
                    final_result += '; '
                        
                if final_result[0] == ' ':
                    final_result = final_result[1:]

                with open('footy_comps.txt', 'w') as ofile:
                    ofile.write(final_result)
            
            else:
                comp_index = [comp_index.strip()]
                uf.append_team(comp_index)

    else:
        uf.append_team(comp_name)

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
        print(comp.strip())

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
        
        count = uf.find_comp(comp_content, comp_team)
        ## finding the required competition in footy_comps.txt

        if count >= len(comp_content.split(';')):
            ## if wrong team has been input
            print('Team not found')
            continue
        
        selected_teams_del = comp_team.split(';')[0].split(':')[1:]
        selected_teams_del = selected_teams_del[0].split(',')
        selected_teams_del = [x.strip() for x in selected_teams_del]
        
        selected_teams = comp_content.split(';')[count].strip().split(':')[1]
        selected_teams = selected_teams.split(',')
        selected_teams = [x.strip() for x in selected_teams]
        ## picking up the selected teams
        
        del_all_comp = comp_team.split(':')[1].strip()
        
        if del_all_comp == 'del_all':
            count = uf.find_comp(comp_content, comp_team)
            ## finding the required competition in footy_comps.txt

            final_result = comp_content.split(';')
            del final_result[count]
            final_result = [x.strip() for x in final_result]

            final_result = '; '.join(elem for elem in final_result)

            with open('footy_comps.txt', 'w') as ofile:
                ofile.write(final_result)
        
        else:

            del_final = uf.not_intersection(selected_teams, selected_teams_del)

            if del_final == []:
                temp_comp = comp_content.split(';')
                del temp_comp[count]
                final_result = ';'.join(str(elem) for elem in temp_comp)
                print(final_result)

            else:
                temp_comp = comp_content.split(';')[count].split(':')[0].strip()
                temp_comp += ': '
                final_result = ''
            
                print(del_final)
                
                for team in del_final:
                    temp_comp += team + ', '
                temp_comp = temp_comp[:-4] 

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
        