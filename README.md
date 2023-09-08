# Codegreen
Computing emits carbon.
One of the ways to reduce carbon emissions due to computing is to shift the timing of performing
computations to periods when more energy is sourced from renewable sources.

Project Codegreen estimates the optimal time point, which fulfills the renewable energy requirements. 
For example, when a user asks for the start time for a 2-hour computation in Germany with 30% renewable energy, Codegreen provides the optimal time of day for the computation. 

## Predicting the renewable energy percentage based on historical weather data

The most important factor to predict the renewable energy percentage is the weather.
The sub-task of the project Codegreen is predicting the renewable energy percentage of total energy production with the help of historical weather data. 

## Identifying key locations that affect renewable energy percentage 
Identifying key locations that have the most significant impact on renewable energy generation is crucial for optimizing server placement and reducing the carbon footprint of data centers. By strategically placing our client's servers in areas with abundant renewable energy sources, we can contribute to a more sustainable and environmentally friendly operation.

## Prerequisites
### PIP
-Install Entose python to call the location of power plants
    ```
    pip install entsoe-py
    ```
-Install geopandas to visualize the Germany map
    ```
    pip install geopandas
    ```




## Usage

- DE_zipcode.py: Collecting Germany's historical weather data and forecast weather data using API from Open-Meteo

- SE_zipcode.py: Collecting Sweden's historical weather data and forecast weather data using API from Open-Meteo

- SE_geolocation.py: Finding the location of solar plants and wind farms

- historical_weatehr_api.py: Combining historical weather data with the location information

- Germany_regressor.ipynb
  
Training a decision tree regressor and random forest regressor to predict the renewable energy percentage in Germany
Using a historical weather dataset containing the zip code

Plotting the prediction compared with the actual renewable energy percentage and the forecast of renewable energy percentage

Plotting the top 5 important locations that affect the renewable energy percentage

- Sweden_regressor.ipynb
  
Training a decision tree regressor and random forest regressor to predict the renewable energy percentage in Sweden

Using a historical weather dataset containing the zip code

Plotting the prediction compared with the actual renewable energy percentage and the forecast of renewable energy percentage

Plotting the top 5 important locations that affect the renewable energy percentage

- Germany_lat_lon_regressor.ipynb
Training a decision tree regressor and random forest regressor to predict the renewable energy percentage

Using a historical weather dataset containing the latitude and the longitude.

Plotting the prediction compared with the actual renewable energy percentage and the forecast of renewable energy percentage

Plotting the top 5 important locations that affect the renewable energy percentage

- entsoeAPI: calculating a country's renewable energy percentage

## Acknowledgments

entsoeAPI.py is provdied by team member, Shubh Vardhan Jain.

