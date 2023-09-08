#!/usr/bin/env python
# coding: utf-8

import importlib
import pandas as pd
from requests.sessions import DEFAULT_REDIRECT_LIMIT
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date
import json
import numpy as np
import DE_zipcode
importlib.reload(DE_zipcode)
import SE_zipcode
importlib.reload(SE_zipcode)


def Germany_zip():
    """
    Collect historical weather data in Germany combining with the zip code
    save it as a csv file
    """
    dfs = []  # List to store the dataframes for each zip code
    zip_codes = ["01", "04", "06", "15", "16", "17", "21", "23", "24", "25", "39", "49", "50", "66", "74", "84", "94"]

    # Loop through each zip code
    for zip_code in zip_codes:
        # Get historical weather data for the current zip code
        df = DE_zipcode.historical(zip_code)

        # Rename the columns to include the zip code in the column names
        df.rename(columns={'wind': f'{zip_code}windspeed_100m (m/s)', 'clouds': f'{zip_code}cloudcover (%)', 'tem': f'{zip_code}apparent_temperature (°C)'}, inplace=True)
        # Set timestamp as the index
        df.set_index('timestamp', inplace=True)
        # Add the dataframe to the list
        dfs.append(df)

    data = pd.concat(dfs, axis=1)
    #data.to_csv('DE_weather_zip_code.csv', index_label='timestamp')
    print(data)


def Sweden_zip():
    """
    Collect historical weather data in Sweden combining with the zip code
    save it as a csv file
    """
    dfs = []  # List to store the dataframes for each zip code
    zip_codes = ["28","57", "68", "70","82", "83","84","92","95"]
    # Loop through each zip code
    for zip_code in zip_codes:
        # Get historical weather data for the current zip code
        df = SE_zipcode.historical(zip_code)

        # Rename the columns to include the zip code in the column names
        df.rename(columns={'wind': f'{zip_code}windspeed_100m (m/s)', 'clouds': f'{zip_code}cloudcover (%)', 'tem': f'{zip_code}apparent_temperature (°C)'}, inplace=True)
        # Set timestamp as the index
        df.set_index('timestamp', inplace=True)
        # Add the dataframe to the list
        dfs.append(df)

    data = pd.concat(dfs, axis=1)
    #data.to_csv('SE_weather_zip_code.csv', index_label='timestamp')
    print(data)

def Germany_lat_lon():
    """
    Collect historical weather data in Germany combining the latitude and the longitude
    save it as a csv file
    """
      
    dfs = []  # List to store the dataframes for each latitude and longitude

    for lat in np.arange(55, 47.5, -0.5):  # Start from 55 and decrement by 0.5 until 47.5 
        for lon in np.arange(6, 15, 0.5):   # Start from 6 and increment by 1 until 15 
            key = f"({lat:.1f},{lon:.1f})"
            df = DE_zipcode.historical2(lat,lon)

        # Rename the columns to include the zip code in the column names
            df.rename(columns={'wind': f'{key}windspeed_100m (m/s)', 'clouds': f'{key}cloudcover (%)', 'tem': f'{key}apparent_temperature (°C)'}, inplace=True)
        # Set timestamp as the index
            df.set_index('timestamp', inplace=True)
        # Add the dataframe to the list
            dfs.append(df)

    data = pd.concat(dfs, axis=1)
    #data.to_csv('DE_weather_lat_lon.csv', index_label='timestamp')
    print(data)
        

#call the function
Germany_zip()
Sweden_zip()
Germany_lat_lon()

