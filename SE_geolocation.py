#!/usr/bin/env python
# coding: utf-8

#install entsoe python package
pip install entsoe-py

#import libraries
from entsoe import EntsoeRawClient
import pandas as pd
from lxml import etree
from googletrans import Translator
import requests


client = EntsoeRawClient(api_key='be7edc85-62fe-4759-b56c-c4122c275f43')

# Define the parameters for the query
country_code = 'SE'  # Sweden
start = pd.Timestamp('2022-05-01', tz='Europe/Stockholm')
end = pd.Timestamp('2022-06-02', tz='Europe/Stockholm')

# Make the query to get the installed generation capacity per unit
response = client.query_installed_generation_capacity_per_unit(country_code, start, end)


# Remove the encoding declaration from the XML response
response = response.replace("<?xml version='1.0' encoding='UTF-8'?>", "")

# Parse the XML response
root = etree.fromstring(response.encode('utf-8'))

# Find the TimeSeries elements in the XML
timeseries_elements = root.findall('.//{*}TimeSeries')

# Find the registeredResource.name when psrType is B16 or B19
registered_resource_names = []
translator = Translator()
for timeseries_element in timeseries_elements:
    psr_type_element = timeseries_element.find('.//{*}psrType')
    if psr_type_element is not None:
        psr_type = psr_type_element.text
        if psr_type in ['B16', 'B19']: #search the registered_resource_names for wind and solar
            registered_resource_name_element = timeseries_element.find('.//{*}registeredResource.name')
            if registered_resource_name_element is not None:
                registered_resource_name = registered_resource_name_element.text
                translation = translator.translate(registered_resource_name, src='sv', dest='en')
                registered_resource_names.append(translation.text)

print(registered_resource_names)



#location_names = ['Lemnhult', 'Kronoberget', 'The hill sore', 'Höstkullen north', 'Markbygden 2 North', 'Må Larberget', 'Eken', 'Bäckhammar', 'Kråktorpet', 'Windground Björkhöjden', 'Björkvattnet', 'Ä Skålen', 'Ã Mot-Lingbo', 'Blaiken', 'The wind farm winds', 'Markbygdenett', 'Pool', 'Blacknight', 'The gonfish']
location_names=['Högaliden wind farm', 'Ersträsk wind power', 'Lemnhult', 'Kronoberget', 'The hill sore', 'Höstkullen north', 'Björnlandshöjden', 'Ã by-alebo', 'Cold moss', 'Djupdal', 'Markbygden 2 North', 'Shaft', 'Må Larberget', 'Eken', 'Ä ndberg', 'Bäckhammar', 'Kråktorpet', 'Windground Björkhöjden', 'Granliden', 'Blakliden', 'Fäbodberget', 'Björkvattnet', 'Ä Skålen', 'Ã Mot-Lingbo', 'Blaiken', 'The wind farm winds', 'Markbygdenett', 'Pool', 'Blacknight', 'The gonfish', 'Turinge']
latitude_longitude = []

for location_name in location_names:
    # Make a request to the Nominatim API to get the geolocation data
    url = f'https://nominatim.openstreetmap.org/search?q={location_name}&format=json&limit=1'
    response = requests.get(url).json()
    
    if response:
        # Extract the latitude and longitude from the response
        lat = response[0]['lat']
        lon = response[0]['lon']
        
        # Append the latitude and longitude to the result list
        latitude_longitude.append((location_name, lat, lon))
    else:
        # If no geolocation data is found, append None for latitude and longitude
        latitude_longitude.append((location_name, None, None))

# Print the results
for location_data in latitude_longitude:
    print(location_data)

