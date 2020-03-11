'''
utility_functions.py
--------------------
'''

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os

class Google:
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

def load_calendar(user_name, scopes):
    if f'{user_name}.pkl' in os.listdir():
        with open(f'{user_name}.pkl', 'rb') as f:
            credentials = pickle.load(f)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=scopes)
        credentials = flow.run_console()
        pickle.dump(credentials, open(f'{user_name}.pkl', 'wb'))

    service = build('calendar', 'v3', credentials=credentials)

    result = service.calendarList().list().execute()
    calendar_id = result['items'][0]['id']
    return service, calendar_id

def even_struct(summary, desc, start_time, timezone):
    start_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
    end_time = start_time + timedelta(hours=3)
    
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
    
    return event

def update_event(result, summary):
    for i in range(0, len(result['items'])):
        if result['items'][i]['summary'] == summary:
            return i

def up_event_struct(start_time, timezone):
    start_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
    end_time = start_time + timedelta(hours=3)
    
    event = {
         'start': {'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"), 'timeZone': timezone},
         'end': {'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"), 'timeZone': timezone}
            }
    
    return event

def team_names():
    with open('footy_teams.txt', 'r') as ofile:
        team_content = ofile.readline()
        ## reading the content from the file

    team_content = team_content.split(',')
    team_content = [x.strip() for x in team_content]
    team_content = team_content[:-1]
    ## splitting every team content into the list format
    
    return team_content

def comp_names():
    with open('footy_comps.txt', 'r') as ofile:
        comp_content = ofile.readline()
    
    comp_content = comp_content.split(';')
    comp_content = [elem.strip() for elem in comp_content]
    
    return comp_content

