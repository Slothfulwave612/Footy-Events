'''
functions.py
------------
This Python module contains all the main functions used for doing 
all the basic tasks in this project namely from adding teams or competition 
to scrapping the content from website, adding and updating events in the calendar.

Modules Imported(7):
--------------------
1. requests: requests is a Python HTTP library, makes HTTP requests simpler and more human-friendly. 
2. BeautifulSoup: for parsing HTML and XML documents.
3. re: to use Python's raw string notation for regular expression patterns.
4. datetime: supplies classes for manipulating dates and times.
5. used for serializing and de-serializing a Python object structure.
6. os: provides functions for interacting with the operating system.
7. utility_funtions: python file which contains all the helper functions.

Functions Defined(8):
--------------------
1. enlist_team: this function will write the team name/s into the text files.
2. preview_teams: this function will display all the added teams.
3. del_teams: this function will delete the team names specified from team name file.
4. enlist_comp: this function will write competition's name and respective teams into footy_comps.txt.
5. preview_comps: this function displays all the competitions that has been saved by the user.
6. del_comps: this function will remove added competitions.
7. scrape_write: this function will add/update the team event in user's calendar.
8. scrape_write_comp: this function adds/update competitons in user's calendar.
'''

## Modules Imported
## ---------------------------------------------------
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
import pickle
import os
import utility_functions as uf
## ----------------------------------------------------

def enlist_team(team_names):
    '''
    This function will write the team name/s into the text files.

    Arguments:
    team_names -- string representing team name/s
    '''
    team_names = ','.join([str(elem) for elem in team_names])

    with open('footy_teams.txt', 'a') as ofile:
        ## opening the file to write/append the content in it
        ofile.write(team_names)
        ofile.write(', ') 

def preview_teams():
    '''
    This function will display all the added teams.
    '''
    with open('footy_teams.txt', 'r') as ofile:
        ## opening the file to read the content in it
        content = ofile.readline()
        
    team_names = content.split(',')
    team_names = [x.strip() for x in team_names]
    if len(team_names) - 1 == 1:
        i = -1

    for i in range(len(team_names) - 2):
        print(team_names[i], end=', ')
    print(team_names[i+1])

def del_teams(del_team_names):
    '''
    This function will delete the team names specified from team name file.

    Arguments:
    del_team_names -- string containing team names
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
                ## making the final required result

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
            
                
                for team in del_final:
                    temp_comp += team + ', '
                temp_comp = temp_comp[:-2] 
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

def scrape_write(user_name, team_content, month_name, timezone, service, calendar_id):
    '''
    This function will add/update the team event in user's calendar.

    Arguments:
    user_name -- string, user name of the user.
    team_content -- list, containing team names.
    month_name -- dict, containing corresponding month values.
    timezone -- str, timezone of user's area.
    service -- for running google calendar api functions.
    calendar_id -- calendar id of the user's calendar.
    '''
    for team in team_content:
        print(f'For Team {team}')

        search_term = f'{team} sky sports fixtures'

        print('\nGetting The Link of the website...\n')

        ## accessing the link of the website
        website_link = uf.Google.search(search_term)[0].split('&')[0]

        print(f'\nScrapping data for {team} from the website...\n')
        print(website_link)

        ## scraping the content from the website
        try:
            scrape_data = requests.get(website_link)
        except Exception:
            print('Taking Some Time\n')
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)

            scrape_data = session.get(website_link)
            
        soup = BeautifulSoup(scrape_data.text, 'html.parser')

        ## finding the div tag which contains all fixture's information
        results = soup.find('div', attrs={'class': 'fixres__body'})
        
        ## scrapping fixuture's date, competition name, team names and timing of the fixtures
        years = results.find_all('h3')
        fix_date = results.find_all('h4')
        comp_name = results.find_all('h5')
        teams = results.find_all('span', attrs={'class': 'swap-text__target'})
        timings = results.find_all('span', attrs={'class': 'matches__date'})

        ## making a dict of all years
        year_dict = {}

        for year in years:
            year_temp = year.text.split(' ')
            year_dict[year_temp[0]] = year_temp[1]

        ## making a list of all dates
        date_text = []

        for date in fix_date:
            temp = date.text.split(' ')

            date_final =''

            for i in temp[1]:
                if i.isdigit():
                    date_final += i
                else:
                    break

            year = year_dict[temp[2]]
            month = month_name[temp[2]]

            date_text.append(f'{date_final} {str(month)} {year}')

        ## making a list of all competition names
        comp_text = []

        for comp in comp_name:
            comp_text.append(comp.text.lower())

        ## making a list of match times
        match_time = []

        for time in timings:
            match_time.append(time.text.strip())

        final_time = []

        for date_x, time_y in zip(date_text, match_time):
            date_split = date_x.split(' ')
            date_split = [int(elem) for elem in date_split]
            time_split = time_y.split(':')
            time_split = [int(elem) for elem in time_split]
            temp_time = datetime(date_split[2], date_split[1], date_split[0], time_split[0], time_split[1], 0)
            temp_time = temp_time + timedelta(hours=4)
            final_time.append(temp_time)

        ## making a dictionary that will contain all information

        final_record = dict()
        home_team = []
        away_team = []

        count = 1

        for x_temp in teams:
            if x_temp.text == '\n\n\n\n':
                continue

            elif count % 2 != 0:
                home_team.append(x_temp.text.lower())
            else:
                away_team.append(x_temp.text.lower())
            count += 1

        for i in range(len(match_time)):
            final_record['Date/Time'] = final_time
            final_record['Competition'] = comp_text

        final_record['Home_Team'] = home_team
        final_record['Away_Team'] = away_team

        print('\nScrapped Successfully')

        result = service.events().list(calendarId=calendar_id, timeZone=timezone, maxResults=9999).execute()
        summary = []
        desc = []
        start_time = []
        result_dict = {}

        for item in range(len(result['items'])):
            temp = result['items'][item]['summary'].split(' ')[-1]
            if temp == '(Football)':
                summary.append(result['items'][item]['summary'])
                desc.append(result['items'][item]['description'])
                date_temp = result['items'][item]['start']['dateTime']
                start_time.append(date_temp)

        result_dict['Summary'] = summary
        result_dict['Description'] = desc
        result_dict['start_time'] = start_time

        for i in range(len(final_record['Home_Team'])):
            temp_list = []

            for index in final_record:
                temp_list.append(final_record[index][i])

            start_time = temp_list[0]
            start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S")
            desc = temp_list[1]
            summary = f'{temp_list[2]} vs {temp_list[3]} (Football)'
            count = False
            for j in range(len(result_dict['Summary'])):
                if summary == result_dict['Summary'][j] and desc == result_dict['Description'][j]:
                    if start_time != result_dict['start_time'][j][:-6]:
                        print(f'Updating Event: {summary}')
                        count = True
                        index = uf.update_event(result, summary)
                        event_id = result['items'][index]['id']
                        event = uf.up_event_struct(start_time, timezone)
                        up_e = service.events().patch(calendarId=calendar_id, eventId=event_id, body=event).execute()
                        print('Event Updated Successfully')
                        print()
                        break
                    else:
                        count = True
                        break
            if count == False:
                print(f'Adding Event: {summary}')
                event = uf.even_struct(summary, desc, start_time, timezone)
                service.events().insert(calendarId=calendar_id, body=event).execute()
        print()

def scrape_write_comp(user_name, comp_name, team_name, month_name, timezone, service, calendar_id, count_c=0):
    '''
    This function adds/update competitons in user's calendar.

    Arguments:
    user_name -- str, user name of the user.
    comp_name -- list, containing competition name.
    team_name -- list, containing teams for corresponding competitions.
    month_name -- dict, corresponding value of each month.
    timezone -- str, timezone of user's area.
    service -- for running google calendar api functions.
    calendar_id -- calendar id of the user's calendar.
    count_c -- for accessing each competiton's content(teams).
    '''
    for comp in comp_name:
        print(f'For Competition {comp}')

        search_term = f'{comp} sky sports fixtures'

        print('\nGetting The Link of the website...\n')

        ## accessing the link of the website
        website_link = uf.Google.search(search_term)[0].split('&')[0]
        temp_team = team_name[count_c]
        
        print(f'\nScrapping data for {comp}: {temp_team} from the website...\n')
        print(website_link)

        ## scraping the content from the website
        try:
            scrape_data = requests.get(website_link)
        except Exception:
            print('Taking Some Time\n')
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)

            scrape_data = session.get(website_link)
            
        soup = BeautifulSoup(scrape_data.text, 'html.parser')

        ## finding the div tag which contains all fixture's information
        results = soup.find('div', attrs={'class': 'fixres__body'})
        
        ## scrapping fixuture's date, competition name, team names and timing of the fixtures
        years = results.find_all('h3')
        fix_date = results.find_all('h4')
        teams = results.find_all('span', attrs={'class': 'swap-text__target'})
        timings = results.find_all('span', attrs={'class': 'matches__date'})
        
        results = str(results)
        real_dates = []
        
        for i in range(len(fix_date)-1):
            start = results.find(str(fix_date[i]))
            end = results.find(str(fix_date[i+1]))
            temp = results[start:end].count('<div class="fixres__item">')
            for j in range(temp):
                real_dates.append(fix_date[i])
        
        start = results.find(fix_date[i+1].text)
        temp = results[start:].count('<div class="fixres__item">')
        for j in range(temp):
                real_dates.append(fix_date[i+1])
        
        ## making a dict of all years
        year_dict = {}

        for year in years:
            year_temp = year.text.split(' ')
            year_dict[year_temp[0]] = year_temp[1]

        ## making a list of all dates
        date_text = []

        for date in real_dates:
            temp = date.text.split(' ')

            date_final =''

            for i in temp[1]:
                if i.isdigit():
                    date_final += i
                else:
                    break

            year = year_dict[temp[2]]
            month = month_name[temp[2]]

            date_text.append(f'{date_final} {str(month)} {year}')

        ## making a list of match times
        match_time = []

        for time in timings:
            match_time.append(time.text.strip())

        temp_time_2 = []

        for date_x, time_y in zip(date_text, match_time):
            date_split = date_x.split(' ')
            date_split = [int(elem) for elem in date_split]
            time_split = time_y.split(':')
            time_split = [int(elem) for elem in time_split]
            temp_time = datetime(date_split[2], date_split[1], date_split[0], time_split[0], time_split[1], 0)
            temp_time = temp_time + timedelta(hours=4)
            temp_time_2.append(temp_time)

        ## making a dictionary that will contain all information

        final_record = dict()
        home_team = []
        away_team = []

        count = 1

        for x_temp in teams:
            if x_temp.text == '\n\n\n\n':
                continue

            elif count % 2 != 0:
                home_team.append(x_temp.text)
            elif count % 2 == 0:
                away_team.append(x_temp.text)
            count += 1
        
        final_home = []
        final_away = []
        final_time = []

        if temp_team != 'all':
            for x, y, z in zip(home_team, away_team, temp_time_2):
                if x.lower() in temp_team or y.lower() in temp_team:
                    final_home.append(x.lower())
                    final_away.append(y.lower())
                    final_time.append(z)

            for i in range(len(match_time)):
                final_record['Date/Time'] = final_time

            final_record['Home_Team'] = final_home
            final_record['Away_Team'] = final_away

        else:
            for i in range(len(match_time)):
                final_record['Date/Time'] = temp_time_2

            final_record['Home_Team'] = home_team
            final_record['Away_Team'] = away_team

        print('\nScrapped Successfully')
        count_c += 1

        result = service.events().list(calendarId=calendar_id, timeZone=timezone, maxResults=9999).execute()
        summary = []
        desc = []
        start_time = []
        result_dict = {}

        for item in range(len(result['items'])):
            temp = result['items'][item]['summary'].split(' ')[-1]
            if temp == '(Football)':
                summary.append(result['items'][item]['summary'])
                desc.append(result['items'][item]['description'])
                date_temp = result['items'][item]['start']['dateTime']
                start_time.append(date_temp)

        result_dict['Summary'] = summary
        result_dict['Description'] = desc
        result_dict['start_time'] = start_time
        
        t_count = 0

        for i in range(len(final_record['Home_Team'])):
            temp_list = []

            for index in final_record:
                temp_list.append(final_record[index])
        
            start_time = temp_list[0][t_count]
            
            start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S")
            desc = comp
            summary = f'{temp_list[1][t_count]} vs {temp_list[2][t_count]} (Football)'
            count = False
            
            for j in range(len(result_dict['Summary'])):
                if summary == result_dict['Summary'][j] and desc == result_dict['Description'][j]:
                    if start_time != result_dict['start_time'][j][:-6]:
                        print(f'Updating Event: {summary}')
                        count = True
                        index = uf.update_event(result, summary)
                        event_id = result['items'][index]['id']
                        event = uf.up_event_struct(start_time, timezone)
                        up_e = service.events().patch(calendarId=calendar_id, eventId=event_id, body=event).execute()
                        print('Event Updated Successfully')
                        print()
                        break
                    else:
                        count = True
                        break
            if count == False:
                print(f'Adding Event: {summary}')
                event = uf.even_struct(summary, desc, start_time, timezone)
                service.events().insert(calendarId=calendar_id, body=event).execute()
            t_count += 1
        print()

## slothfulwave612