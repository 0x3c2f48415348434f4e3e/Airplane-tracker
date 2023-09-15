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

#check if site is up

def is_up() -> bool:
    try:
        code = requests.get(requests.get(f'http://api.aviationstack.com/v1/flights?access_key={key_token["key"]}'))
        if(code.status_code == 200): #fix logic later
            #status code will be reutned such as 404, 503, 302 etc
            return False
        else:
            return True
    except:
        print("Unable to communicate with server")
        sys.exit(1)
        #improve exception handling later

#make so both HTTPS and HTTP request can run for individuals who's subscription do not suppot https

if(is_up):
    global data
    data = httpx.get(f'http://api.aviationstack.com/v1/flights?access_key={key_token["key"]}')
else:
    print("Error requesting data")

#let read the the data we
'''
According to the API the properties we get (Whihc should be important are):
4.) live - An object, gives us information like altitude, etc
'''

storedata = json.loads(data.content)

lengthofdataobject = len(storedata)
#loop over length of object to get necessary stuff to get the 
flightimportantinfo = []

#print(storedata.pagination)
print(storedata)
for i in range(lengthofdataobject):
    listofdata = []
    listofdata.append(storedata.airline.name)
    listofdata.append(storedata.flight.number)
    listofdata.append(storedata.aircraft.registration)
    listofdata.append(storedata.live.latitude)
    listofdata.append(storedata.live.longitude)
    listofdata.append(storedata.live.altitude)
    listofdata.append(storedata.live.direction)
    listofdata.append(storedata.live.speed_horizontal)
    listofdata.append(storedata.live.sped_vertical)
    listofdata.append(storedata.live.is_ground)

    flightimportantinfo.extend(listofdata)

print(flightimportantinfo)

#Fix several errors
