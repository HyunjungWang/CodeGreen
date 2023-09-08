# Codegreen
## Predicting the renewable energy % based on historical weather data

Project Codegreen estimates the optimal time point, which fulfills the renewable energy requirements. 
For example, when a user asks for the start time for 2-hour computation in Germany with 30% renewable energy, Codegreen provides the optimal time of day for the computation. 
The most important factor to predict the renewable energy percentage is the weather.
The sub-task here is predicting the renewable energy percentage of total energy production with the help of historical weather data.


## Prerequisites
### PIP
-Install Entose python to call the location of power plants
pip install entsoe-py

-Install geopandas to visualize the Germany map



## Usage

-DE_zipcode.py: Collecting Germany historical weather data and forecast weather data using Api

-SE_zipcode.py: Collecting Sweden historical weather data and forecast weather data using Api

-SE_geolocation.py: Finding the location of solar plants and wind farms

-historical_weatehr_api.py: Combining historical weather data with the location information

-Germany_regressor.ipynb: 
Training a decision tree regressor and random forest regressor to predict the renewable energy percentage in Germany
Using a historical weather dataset contatining the zip code
Ploting the prediction comparing with the acutal renewable energy percentage and the forecast of reneable energy percentage
Ploting the top 5 important locations that affect the renewable energy percentage

-Sweden_regressor.ipynb
Training a decision tree regressor and random forest regressor to predict the renewable energy percentage in Sweden
Using a historical weather dataset contatining the zip code
Ploting the prediction comparing with the acutal renewable energy percentage and the forecast of reneable energy percentage
Ploting the top 5 important locations that affect the renewable energy percentage

-Germany_lat_lon_regressor.ipynb
Training a decision tree regressor and random forest regressor to predict the renewable energy percentage
Using a historical weather dataset contatining the latitude and the longitude.
Ploting the prediction comparing with the acutal renewable energy percentage and the forecast of reneable energy percentage
Ploting the top 5 important locations that affect the renewable energy percentage


## Acknowledgments

entsoeAPI.py is provdie by team member, Shubh Vardhan Jain.

