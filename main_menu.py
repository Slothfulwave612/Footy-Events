'''
main_menu.py
------------
This Python module contains the main menu for our Footy-Events projecy, the
module will be run by the user in order to perform their required task.

Module Imported(3):
-------------------
1. os: provides functions for interacting with the operating system.
2. functions: python module containing all the main functions.
3. utility_functions: python module containing the helper functions.
'''

## Module Imported
## ----------------------------
import os
import functions 
import utility_functions as uf
## ----------------------------

choice = 0

month_name = {
       'January': 1, 
       'February': 2, 
       'March': 3,
       'April': 4,
       'May': 5,
       'June': 6,
       'July': 7,
       'August': 8,
       'September': 9,
       'October': 10,
       'November': 11, 
       'December': 12
      }
## month name and their corresponding value

timezone = 'Asia/Kolkata'
## time zone set to India

scopes = ['https://www.googleapis.com/auth/calendar']
## scope for running api functions

while choice != 4:

    ## here are all the options available
    print('\n***Footy Events***')
    print('1. Enlist Your Team')
    print('2. Enlist Your Competition')
    print('3. Run The Process')
    print('4. Exit\n')

    while True:
        ## Error checking
        try:
            choice = int(input('Enter Your Choice:- '))
            ## for entering the choice
            break
        except ValueError:
            print('Invalid Input\n')
    
    if choice == 1:
        ## Enlist Your Team
        en_choice = 0

        while en_choice != 4:
            print('\nEnlist Your Team')
            print('1. Add a Team')
            print('2. Preview Added Teams')
            print('3. Delete Added Teams')
            print('4. Back')

            while True:
                try:
                    en_choice = int(input('Enter Your Choice:- '))
                    ## for entering the choice for enlisting menu
                    break
                except ValueError:
                    print('Invalid Input\n')
                
            if en_choice == 1:
                ## Add a Team
                team_comp = input('\nEnter Team:- ').lower().strip().split(',')

                functions.enlist_team(team_comp)
                ## calling enlist_team function

                print('\nYour teams has been saved.')

            elif en_choice == 2:
                ## Preview Added Teams
                if 'footy_teams.txt' in os.listdir():
                    print('\nHere are your added teams:- ')

                    functions.preview_teams()
                    ## calling preview_teams function
                else:
                    print('Please Add A Team First')

            elif en_choice == 3:
                ## Delete Added Teams
                if 'footy_teams.txt' in os.listdir():
                    print('\nYour Teams:- ')

                    functions.preview_teams()
                    ## calling preview_teams function

                    del_team_names = input('\nEnter teams to be deleted:- ').strip().split(',')

                    if del_team_names[0] == 'del_all':
                        os.remove('footy_teams.txt')
                    else:
                        functions.del_teams(del_team_names)
                else:
                    print('Please Add A Team First')

            elif en_choice < 1 or en_choice > 4:
                print('Invalid Input')
            
    elif choice == 2:
        ## Enlist Your Competition
        comp_choice = 0
        ## for accessing the competition sub-menu

        while comp_choice != 4:
            ## sub-menu choices
            print('\nEnlist Your Competition')
            print('1. Add a Competition')
            print('2. Preview Added Competitions')
            print('3. Delete Added Competitions')
            print('4. Back')

            while True:
                try:
                    comp_choice = int(input('Enter Your Choice:- '))
                    ## for entering the choice for enlisting menu
                    break
                except ValueError:
                    ## for any value errors
                    print('Invalid Input\n')
                
            if comp_choice == 1:
                ## Add a Competition

                comp_name = input('\nEnter competition\'s name:- ').lower().split(';')
                ## format(for selected teams) -- competition name: team_name1, team_name2, ....
                ## format(for all teams) -- competition name: all
                ## multiple competition separated by ;

                functions.enlist_comp(comp_name)

                print('\nYour competitions has been saved.')
                ## displaying the message
            
            elif comp_choice == 2:
                ## Preview Added Competitions
                if 'footy_comps.txt' in os.listdir():
                    print('\nHere are your added Competitions:- ')

                    functions.preview_comps()
                    ## calling preview_comps function
                else:
                    ## if file not found
                    print('Please Add A Competition First')
            
            elif comp_choice == 3:
                ## Delete Added Competitions
                if 'footy_comps.txt' in os.listdir():
                    print('\nYour Competitions:- ')

                    functions.preview_comps()
                    ## calling preview_comps function

                    del_comp_names = input('\nEnter competition to be deleted:- ').lower()
                    ## format(to remove teams) -- compitition name: team name1, team name2...
                    ## format(to remove comp)  -- compitition name: del_all
                    ## to remove all competition write del_all

                    if del_comp_names == 'del_all':
                        os.remove('footy_comps.txt')
                    else:
                        functions.del_comps(del_comp_names)
                else:
                    print('Please Add A Competition First')
            
            elif comp_choice < 1 or choice > 4:
                print('Invalid Input')


    elif choice == 3:
        ## Run The Process
        user_name = input('\nEnter your username:- ').lower()

        service, calendar_id = uf.load_calendar(user_name, scopes)

        print('\n---Instructions For Running or Updating Selected Teams or Competitions---')
        print('1. Enter TR if you want to Run Process for teams.')
        print('2. Enter CR if you want to Run Process for competitions.')
        print('3. Enter TCR if you want to Run Process for both teams and competitions.')
        print('4. Enter TU if you want to update selected teams.')
        print('5. Enter CU if you want to update selected competitions.')
        print('6. Enter TCU if you want to update selected teams as well as competitions.')
        print('7. Enter exit if you want to exit out.')
        print('-------------------------------------------------------------------------')

        sel_choice = None

        while(sel_choice != 'exit'):
            print()
            sel_choice = input('Enter Your Choice:- ').lower()

            if sel_choice == 'tr' or sel_choice == 'tcr':
                ## Run Process for teams
                if 'footy_teams.txt' in os .listdir():
                    team_content = uf.team_names()
                    functions.scrape_write(user_name, team_content, month_name, timezone, service, calendar_id)

                    if sel_choice == 'tr':
                        break
                else:
                    print('footy_teams.txt not found')
                    break
            
            if sel_choice == 'cr' or sel_choice == 'tcr':
                ## Run Process for competitions
                if 'footy_comps.txt' in os.listdir():
                    comp_content = uf.comp_names()
                    comp_name = [elem.split(':')[0] for elem in comp_content][:-1]
                    team_name = []
                    for team in comp_content[:-1]:
                        temp = team.split(':')[1]
                        team_name.append(temp.strip())    
                    functions.scrape_write_comp(user_name, comp_name, team_name, month_name, timezone, service, calendar_id)
                    if sel_choice == 'cr' or sel_choice == 'tcr':
                        break
                else:
                    print('footy_comps.txt not found')
                    break

            if sel_choice == 'tu' or sel_choice == 'tcu':
                ## Update selected teams
                if 'footy_teams.txt' in os.listdir():
                    up_teams = input('Enter Team Names:- ').lower()

                    orig_team = uf.team_names()
                    team_content = up_teams.split(',')
                    team_content = [elem.strip() for elem in team_content]
                    team_content = [elem for elem in team_content if elem in orig_team]
                    functions.scrape_write(user_name, team_content, month_name, timezone, service, calendar_id)
                    if sel_choice == 'tu':
                        break
                else:
                    print('footy_teams.txt not found')
                    break
        
            if sel_choice == 'cu' or sel_choice == 'tcu':
                ## Update selected competitions
                if 'footy_comps.txt' in os.listdir():
                    up_comp = input('Enter Competition\'s Detail:- ').lower()

                    comp_content = up_comp.split(';')
                    comp_content = [elem.strip() for elem in comp_content]
                    comp_name = [elem.split(':')[0] for elem in comp_content]
                    team_name = []
                    for team in comp_content:
                        temp = team.split(':')[1]
                        team_name.append(temp.strip())
                    functions.scrape_write_comp(user_name, comp_name, team_name, month_name, timezone, service, calendar_id)
                    if sel_choice == 'cu' or sel_choice == 'tcu':
                        break
                else:
                    print('footy_comps.txt not found')
                    break

    elif choice < 1 or choice > 4:
        print('Invalid Input')
    
## slothfulwave612    