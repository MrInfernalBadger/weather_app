from pprint import pprint

from extract_data import create_forecast_data
from weather_display import print_weather_data
from retrieve_data_from_API import get_weather_data


testing_state = False
weather_data = get_weather_data(testing_state)

if weather_data:
    forecast = create_forecast_data(weather_data)

    print_weather_data(forecast) 
    
             
else:
    print("\nFailed to retrieve weather data.")
    

# todo
# makes times of day dynamically change depending on timezone, could could retrieve all values and pick the first, third, sixth and ninth