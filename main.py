import json
import pprint as pp


from extract_data import create_forecast_data
from weather_display import print_weather_data
from retrieve_data_from_API import get_weather_data


testing_state = False


if testing_state:
    with open("weather.json", "r") as file:
        weather_data = json.load(file)
else:
    weather_data = get_weather_data()
        


forecast = create_forecast_data(weather_data)


print_weather_data(forecast)







# todo
# get the midnight temp onto the correct day




    










