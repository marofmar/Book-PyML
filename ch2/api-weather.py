import requests
import json
import numpy as np
# API personal key of yours 
apikey = "<YOUR API KEY HERE>"

# select cities to check the weather
cities = ['Seoul', 'San Francisco']

# set API 
# api.openweathermap.org/data/2.5/weather?q=London,uk
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# Kelvin to Celcius
k2c = lambda k: np.float(k)-273.15

# Extract info of cities 
for name in cities:
    url = api.format(city = name, key = apikey)
    # send request to API to extract data
    r = requests.get(url) 
    # transform the received result into JSON format
    data = json.loads(r.text) 
    #print(data)

    # print the result
    print(" CITY: ", data['name'])
    print(" | weather: ", data['weather'][0]['description'])
    print(" | the low: ", k2c(data['main']['temp_min']))
    print(" | the high: ", k2c(data['main']['temp_max']))
    print(" | wind speed: ", data['wind']['speed'])
    print(" | feels like: ", k2c(data['main']['feels_like']))
    print()
from datetime import datetime
print(datetime.now(), "Seoul NOW")