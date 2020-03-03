'''
main_menu.py
------------

This Python module contains the main menu for our program, the
module will be run by the user in order to perform their required
task.

'''

import os
import functions 

choice = 0

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
                team_comp = input('\nEnter Team:- ').strip().split(',')

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

                comp_name = input('\nEnter competition\'s name:- ').split(';')
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

                    del_comp_names = input('\nEnter competition to be deleted:- ')
                    ## format(to remove teams) -- compitition name: team name1, team name2...
                    ## format(to remove comp)  -- compitition name: all
                    ## to remove all competition write del_all

                    if del_comp_names == 'del_all':
                        os.remove('footy_comps.txt')
                    else:
                        functions.del_comps(del_comp_names)
                else:
                    print('Please Add A Competition First')


    elif choice == 3:
        ## Run The Process
        pass
    
    elif choice < 1 or choice > 4:
        print('Invalid Input')
    
## slothfulwave612    