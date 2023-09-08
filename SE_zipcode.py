#!/usr/bin/env python
# coding: utf-8

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import pandas as pd
import requests
from datetime import datetime, timedelta, date


# Initialize the OWM API
owm = OWM('ba4862987ea3f2079ee881d001cc4a84')
mgr = owm.weather_manager()

# Dictionary containing latitude and longitude data for the zip codes of solar plants and wind farms
Geodata = {
    "28":  {"lat": 62.7896573,  "lon":  16.5519702},
    "57":  {"lat": 57.2851714,"lon": 15.2759766},
    "68":  {"lat": 59.1589394, "lon":  14.190986},
    "70":  {"lat": 59.2201,"lon":  14.6687},
    "82":  {"lat": 65.3307612,  "lon":  20.8422425},
    "83":  {"lat": 62.5331229,  "lon":  14.2669109},
    "84":  {"lat": 50.9014721,  "lon":  11.0377839},
    "92":  {"lat": 46.7650646, "lon":  14.833006},
    "95":  {"lat": 64.6057959,  "lon":  13.7773811},

   
}

def getGeo(zipcode):
    """Get the latitude and the longitude of the zip code list
    
    Parameters:
    - zipcode (str): The zip code for which latitude and longitude are neede

    Returns
    - float, float: Latitude and longitude coordinates for the given zip code.

    """
    return Geodata[zipcode]["lat"], Geodata[zipcode]["lon"]

def weatherforecast(zipcode):
    """
    Get weather forecast data for the next 48 hours for a given zip code.

    Parameters:
    - zipcode (str): The zip code for which weather forecast data is needed.

    Returns:
    - pd.DataFrame: A DataFrame containing weather forecast data.
    """
    
     # Fetch latitude and longitude for the given zip code
    lat,lon=getGeo(zipcode)
    # Retrieve weather data for the next 48 hours
    one_call = mgr.one_call(lat, lon)
    
     # Create an empty DataFrame to store weather data
    dict = {'timestamp': [], 'wind': [], 'cloud': [], 'temp': []}
    df = pd.DataFrame(dict)
    
    # Extract and store weather data for each hour in the DataFrame
    for i in range(len(one_call.forecast_hourly)):    
        timestamp = one_call.forecast_hourly[i].reference_time('iso')
        w=one_call.forecast_hourly[i].wind().get('speed', 0)
        c=one_call.forecast_hourly[i].clouds
        t=one_call.forecast_hourly[i].temperature('celsius').get('feels_like', None)
        df.loc[len(df.index)] = [timestamp,w,c,t] 
    
    # Set the timestamp column as the DataFrame's index
    df.set_index('timestamp', inplace=True)



    return df


def historical(zipcode):
    """
    Get historical weather data for a given zip code.

    Parameters:
    - zipcode (str): The zip code for which historical weather data is needed.

    Returns:
    - pd.DataFrame: A DataFrame containing historical weather data.
  
    """
        
     # Fetch latitude and longitude for the given zip code  
    lat,lon=getGeo(zipcode)
    # Send a request to the Open Meteo API to fetch historical weather data        
    response = requests.get("https://archive-api.open-meteo.com/v1/archive?latitude="+str(lat)+"&longitude="+str(lon)+"&start_date=2021-06-01&end_date=2023-06-01&hourly=apparent_temperature,cloudcover,windspeed_100m&timezone=Europe%2FBerlin&windspeed_unit=ms&min=2022-06-01&max=2023-06-01")

    # Parse the JSON response   
    wdata = response.json()
    
    # Create an empty DataFrame to store historical weather data    
    dic ={"timestamp": [],"wind":[],"clouds":[],"tem":[]}
    
    # Extract and store historical weather data in the DataFrame
    t = wdata.get("hourly").get("time")
    tem=wdata.get("hourly").get("apparent_temperature")
    c=wdata.get("hourly").get("cloudcover")
    wind = wdata.get("hourly").get("windspeed_100m")
    
    for i in t:
        date_format = "%Y-%m-%dT%H:%M"
        dt_start = datetime.strptime(i,date_format)
        dic["timestamp"].append(dt_start)
    for i in wind:
        dic["wind"].append(i)
    for i in c:
        dic["clouds"].append(i)
    for i in tem:
        dic["tem"].append(i)
   
    # Create a DataFrame from the parsed data                
    df = pd.DataFrame(dic)



    return df

