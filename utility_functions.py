'''
utility_functions.py
--------------------
This Python module contains functions used by the function.py and main_menu.py files.
It contains helper function which helps the main functions in functions.py or
options in main_menu.py .

Modules Imported(8):
-----------------
1. requests: requests is a Python HTTP library, makes HTTP requests simpler and more human-friendly. 
2. BeautifulSoup: for parsing HTML and XML documents.
3. re: to use Python's raw string notation for regular expression patterns.
4. datetime: supplies classes for manipulating dates and times.
5. apiclient: Python client library for Google's discovery based APIs.
6. google_auth_oauthlib: this library provides oauthlib integration with google-auth.
7. pickle: used for serializing and de-serializing a Python object structure.
8. os: provides functions for interacting with the operating system.

Class Defined(1):
-----------------
1. Google: used for searching a particular query on google's webpage.

Functions Defined(9):
--------------------
1. not_intersection: this function compares two lists and gives the difference of the two.
2. append_team: this function will add competitions to footy_comps.txt.
3. find_comp: this function will find the competition if present in foot_comps.txt.
4. load_calendar: this function will load the user's google calendar.
5. even_struct: this function is for defining the structure of the required footy-event.
6. update_event: this function will find the index where the updation have to take place.
7. up_event_struct: this function will prepare the event structure for updating the event.
8. team_names: this function will list out all the team names.
9. comp_names: this function will list out all the competitions.
'''

## Modules Imported
## ----------------------------------------------------
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os
## -----------------------------------------------------

class Google:
    '''
    this class contaings the function for searching a particular query on google's webpage.
    '''
    @classmethod
    def search(self, search):
        page = requests.get("http://www.google.de/search?q="+search)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
        urls = [re.split(":(?=http)",link["href"].replace("/url?q=",""))[0] for link in links]
        return [url for url in urls if 'webcache' not in url]

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
    '''
    This function will add competitions to footy_comps.txt.

    Argument:
    comp_name -- list data-type, containing competition name
    '''
    comp_name = ';'.join([str(elem) for elem in comp_name])
    ## turning back to string

    with open('footy_comps.txt', 'a') as ofile:
        ## opening footy_comps file for appending the results
        ofile.write(comp_name)
        ofile.write('; ')

def find_comp(comp_content, comp_team):
    '''
    This function will find the competition if present in foot_comps.txt.

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

def load_calendar(user_name, scopes):
    '''
    This function will load the user's google calendar.

    Arguments:
    user_name -- str, the username of the user.
    scopes -- list, containing the scope for google calendar api to function accordingly.

    Returns:
    service -- for running various functions.
    calendar_id -- the id of user's google calendar.
    '''
    if f'{user_name}.pkl' in os.listdir():
        ## if the pickle file is already there, no need to ask permission again 
        with open(f'{user_name}.pkl', 'rb') as f:
            ## loading the pickle file
            credentials = pickle.load(f)
    else:
        ## asking for permission
        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=scopes)
        credentials = flow.run_console()
        pickle.dump(credentials, open(f'{user_name}.pkl', 'wb'))
        ## saving the user permission in a pickle file

    service = build('calendar', 'v3', credentials=credentials)

    result = service.calendarList().list().execute()
    calendar_id = result['items'][0]['id']
    ## accessing the calendar id 

    return service, calendar_id

def even_struct(summary, desc, start_time, timezone):
    '''
    This function is for defining the structure of the required footy-event.

    Arguments:
    summary -- str, containing home_team vs away team.
    desc -- str, containing the competition name.
    start_time -- str, containing the starting time of the match.
    timezone -- str, containing the timezone of user's area.

    Returns:
    event -- footy-event structure.
    '''
    start_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
    ## converting string to datetime object
    end_time = start_time + timedelta(hours=3)
    ## creating the end time for the event
    
    event = {
      'summary': summary,
      'description': desc,
      'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': timezone,
      },
      'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': timezone,
      },
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'popup', 'minutes': 30},
        ],
      },
    }
    ## creating the required event structure
    
    return event

def update_event(result, summary):
    '''
    This function will find the index where the updation have to take place.

    Arguments:
    result -- contains all the information about user's google calendar.
    summary -- the competition name.

    Returns:
    i -- index of that summary.
    '''
    for i in range(0, len(result['items'])):
        if result['items'][i]['summary'] == summary:
            return i

def up_event_struct(start_time, timezone):
    '''
    This function will prepare the event structure for updating the event.

    Arguments:
    start_time -- str, containing the new start time for the event.
    timezone -- str, containing the timezone of user's area.

    Return:
    event -- event structure containing new start time and end time.
    '''
    start_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
    end_time = start_time + timedelta(hours=3)
    
    event = {
         'start': {'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"), 'timeZone': timezone},
         'end': {'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"), 'timeZone': timezone}
            }
    
    return event

def team_names():
    '''
    This function will list out all the team names.

    Returns:
    team_content -- list, containing team names.
    '''
    with open('footy_teams.txt', 'r') as ofile:
        team_content = ofile.readline()
        ## reading the content from the file

    team_content = team_content.split(',')
    team_content = [x.strip() for x in team_content]
    team_content = team_content[:-1]
    ## splitting every team content into the list format
    
    return team_content

def comp_names():
    '''
    This function will list out all the competitions.

    Returns:
    comp_content -- list, contaning all competitions.
    '''
    with open('footy_comps.txt', 'r') as ofile:
        comp_content = ofile.readline()
        ## reading the content from the file
    
    comp_content = comp_content.split(';')
    comp_content = [elem.strip() for elem in comp_content]
    ## splitting every competition content into list format
    
    return comp_content

## slothfulwave612