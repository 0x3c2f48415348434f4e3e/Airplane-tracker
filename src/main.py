import requests
import subprocess
try:
    import httpx
except:
    print("http is not within system")
    subprocess.run('pip install httpx')
try:
    import cartopy 
except:
    print("cartopy is not within system")
    subprocess.run('pip install cartopy')
'''
try:
    import pygame
except:
    print("pygame is not within system")
    subprocess.run('pip install pygame')
'''
try:
    import pandas as pd
except:
    print("pandas is not within system")
    subprocess.run('pip install pandas')

try:
    import geopandas
except:
    print('geopandas is not within system')
    subprocess.run('pip install geopandas')

#will have to go into the requirements.txx file to add the modules needed

import matplotlib

from key import key_token
import logging #log stuff, leave for later
import json
import sys
import sqlite3 #just going to store the data we get in a database (since ploting them within the suitable information is unfeasible)
#check if site is up

def is_up() -> bool:
    try:
        code = requests.get(requests.get(f'http://api.aviationstack.com/v1/flights?access_key={key_token["key"]}'))
        if(code.status_code == 200): #fix logic later
            #status code will be reutned such as 404, 503, 302 etc
            print("True")
            return True
        else:
            print("False")
            return False
    except requests.exceptions.ConnectionError as e:
        print(e)
        sys.exit(1)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
        sys.exit(1)
        #improve exception handling later

#make so both HTTPS and HTTP request can run for individuals who's subscription do not suppot https

if(is_up):
    global data
    data = httpx.get(f'http://api.aviationstack.com/v1/flights?access_key={key_token["key"]}')
    #create SQLite database here
    DatabaseConnection = sqlite3.connect('SQL.db')
else:
    print("Error requesting data")

#let read the the data we
'''
According to the API the properties we get (Whihc should be important are):
4.) live - An object, gives us information like altitude, etc
'''

storedata = json.loads(data.content)


#loop over length of object to get necessary stuff to get the 
flightimportantinfo = []

second = storedata["data"]
#print(second)#storedata)
#print(storedata)

lengthofdataobject = len(second)
listofdata = []
for i in range(lengthofdataobject):
    listofdata = [second[i]["airline"]["name"], listofdata.append(second[i]["flight"]["number"]),listofdata.append(second[i]["live"])]

    flightimportantinfo.extend(listofdata)

print(flightimportantinfo)

#Fix several errors
