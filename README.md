# Project Codegreen

## 🌱 Overview

**Project Codegreen** is a broader initiative focused on reducing carbon emissions caused by computing activities. It helps schedule computations at times when renewable energy availability is highest — for example, suggesting the best start time for a 2-hour computation in Germany when a user wants at least 30% renewable energy usage.

This repository contributes to Project Codegreen through two critical sub-tasks:

### 🔍 Sub-Tasks in This Project

1. **Predicting Renewable Energy Percentage from Historical Weather Data**  
   Develop machine learning models (Decision Trees and Random Forests) that use weather variables to predict the percentage of renewable energy (solar and wind) in total electricity production.

2. **Identifying Key Locations That Influence Renewable Energy Generation**  
   Analyze spatial weather and production data to identify the geographic regions (zip codes or coordinates) that most strongly impact renewable energy supply. This supports smarter decisions in server placement for sustainability.

These sub-projects provide the predictive and spatial intelligence needed to support Codegreen's decision-making engine.


### 🎯 Goals

- Enable low-carbon computing through data-driven forecasting.
- Improve the accuracy of renewable energy predictions based on local weather patterns.
- Support infrastructure optimization by identifying high-impact renewable energy locations.


## ⚙️ Prerequisites

Make sure to install the following Python packages before starting:
### PIP
- Install Entose python package to search the registered_resource_names for wind and solar
    ```
    pip install entsoe-py
    ```
- Install Python wrapper for the OpenWeatherMap API.
    ```
    pip install pyowm
    ```
- Install geopandas to visualize the Germany map
    ```
    pip install geopandas
    ```


## 🚀 Usage

### 📥 Data Collection

Use the following scripts to collect weather and location data:

- **`DE_zipcode.py`**  
  Collects historical and forecasted weather data for Germany using the Open-Meteo API.

- **`SE_zipcode.py`**  
  Collects historical and forecasted weather data for Sweden using the Open-Meteo API.

- **`SE_geolocation.py`**  
  Retrieves the geographical coordinates of solar and wind energy plants in Sweden.

- **`historical_weather_api.py`**  
  Combines historical weather data with geolocation information for training models.

### 🔌 ENTSO-E API Integration

These modules interact with the [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/) to retrieve energy data:

- **Retrieve Historical Energy Production**  
  Fetch past records of electricity generation categorized by energy sources.

- **Retrieve Day-Ahead Energy Forecasts**  
  Access predictions of energy production for the upcoming day, used to schedule low-carbon computing tasks.

- **Calculate Renewable Energy Percentage**  
  Compute the share of total energy generated from renewable sources like wind and solar.

### 🧠 Training Predictive Models

Use the Jupyter notebooks to train and evaluate machine learning models for forecasting renewable energy percentage:

#### 🇩🇪 Germany

- **`Germany_regressor.ipynb`**  
  - Trains Decision Tree and Random Forest regressors using zip code–based weather data.
  - Compares predicted and actual renewable energy percentages.
  - Plots the top 5 zip code locations influencing renewable output.

- **`Germany_lat_lon_regressor.ipynb`**  
  - Similar to the above, but uses latitude and longitude for training instead of zip codes.

#### 🇸🇪 Sweden

- **`Sweden_regressor.ipynb`**  
  - Trains Decision Tree and Random Forest models on Swedish weather data (by zip code).
  - Visualizes model accuracy and key influencing locations.


## 🔍 Key Results

### 📈 Model Performance

- **Random Forest Regressor** performed best across both datasets.
  - **Germany (Zip Code Features)**: R² ≈ 0.75
  - **Sweden (Zip Code Features)**: R² ≈ 0.92
  - **Germany (Lat/Lon Features)**: R² ≈ 0.75 (no significant improvement over zip code)

- **Decision Tree Regressor** underperformed compared to Random Forest:
  - Germany: R² ≈ 0.47
  - Sweden: R² ≈ 0.79


## 📍 Location Feature Visualization

To understand which geographic regions most influence the renewable energy percentage, we analyzed **feature importances** from the Random Forest model. This helps pinpoint **key locations** where weather variables (like windspeed or temperature) have the strongest impact on renewable energy generation.


### 📊 Observed Trends

- **Sweden consistently achieved higher prediction accuracy**, possibly due to less variability or better data quality.
- Models trained with **latitude/longitude features** performed similarly to zip code–based models.
- **Predictions generally follow the shape** of actual renewable energy percentages, but **underestimate peak values**.

### ⚠️ Limitations

- **Small sample size**: Only 17 locations used for Germany and fewer than 10 for Sweden — out of hundreds of actual power plants.
- **Outdated data**: Rapid increases in renewable capacity (e.g., +71% solar, +77% wind in Germany) reduce the relevance of older data.
- **Static models**: Current models do not account for seasonal or infrastructure growth trends.

> Improving accuracy will require newer data, wider geographic coverage, and potentially more advanced time-series modeling.



## Acknowledgments

entsoeAPI.py and uitl.py is provdied by team member, Shubh Vardhan Jain.

