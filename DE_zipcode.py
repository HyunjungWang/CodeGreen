#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#import libraries
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import pandas as pd
import requests
from datetime import datetime, timedelta, date

# Initialize the OWM API
owm = OWM('ba4862987ea3f2079ee881d001cc4a84')
mgr = owm.weather_manager()

# Dictionary containing latitude and longitude data for the zip codes of power plants with large capacity
Geodata = {
    "25": {"lat": 54.2199, "lon": 9.2808},
    "24": {"lat": 54.8257, "lon": 9.1997},
    "17": {"lat": 53.2603, "lon": 13.9753},
    "39": {"lat": 52.0432, "lon": 11.5803},
    "15": {"lat": 51.834, "lon": 13.531},
    "23": {"lat": 52.1561, "lon": 11.3101},
    "01": {"lat": 52.5085, "lon": 11.8088},
    "06": {"lat": 51.5192, "lon": 14.0047},
    "16": {"lat": 54.7178, "lon": 9.3917},
    "21": {"lat": 52.8351, "lon": 13.7997},
    "94": {"lat": 48.8312, "lon": 12.7213},
    "49": {"lat": 52.5693, "lon": 7.0759},
    "04": {"lat": 51.3347, "lon": 12.6089},
    "50": {"lat": 48.7199, "lon": 12.4406},
    "66": {"lat": 49.3169, "lon": 7.334},
    "74": {"lat": 49.319, "lon": 9.4201},
    "84": {"lat": 48.7199, "lon": 12.4406},    
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

def weatherforecast2(lat,lon):
    """
    Get weather forecast data for the next 48 hours based on latitude and longitude.

    Parameters:
    - lat (float): The latitude coordinate of the location.
    - lon (float): The longitude coordinate of the location.

    Returns:
    - pd.DataFrame: A DataFrame containing weather forecast data.
    """

    # Retrieve weather forecast data for the specified latitude and longitude
    one_call = mgr.one_call(lat, lon)
    
    # Create an empty DataFrame to store weather forecast data
    dict = {'timestamp': [], 'wind': [], 'cloud': [], 'temp': []}
    df = pd.DataFrame(dict)
    
     # Extract and store weather forecast data for each hour in the DataFrame
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


def historical2(lat,lon):
    """
    Get historical weather data based on latitude and longitude.

    Parameters:
    - lat (float): The latitude coordinate of the location.
    - lon (float): The longitude coordinate of the location.

    Returns:
    - pd.DataFrame: A DataFrame containing historical weather data.
    """
    # Send a request to the Open Meteo API to fetch historical weather data        
    response = requests.get("https://archive-api.open-meteo.com/v1/archive?latitude="+str(lat)+"&longitude="+str(lon)+"&start_date=2021-06-01&end_date=2023-06-01&hourly=apparent_temperature,cloudcover,windspeed_100m&timezone=Europe%2FBerlin&windspeed_unit=ms&min=2022-06-01&max=2023-06-01")
    
    # Parse the JSON response   
    wdata = response.json()
    
    # Create a dictionary to store the parsed data    
    dic ={"timestamp": [],"wind":[],"clouds":[],"tem":[]}
    
    # Extract data from the JSON response and append it to the dictionary
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