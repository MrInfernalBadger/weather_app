import requests
import json
import pprint as pp

from extract_data import create_forecast_data


testing_state = False


if testing_state:
    with open("weather.json", "r") as file:
        weather_data = json.load(file)
else:
    API_KEY = "c84da2e4454636df32c08657e3c94262"
    CITY =    "Melbourne,AU"
    URL =    f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"


    response = requests.get(URL)

    if response.status_code == 200:
        weather_data = response.json()  
        # weather = data["weather"][0]["description"]
        # temp = data["main"]["temp"]
        # print(f"Weather in {CITY}: {weather}, {temp}°C")
    else:
        print(f"Error: {response.status_code}, Message: {response.text}")
        

forecast = create_forecast_data(weather_data)

for day in forecast.values():
    print(f"----{day['day']}----")
    print(day['weather'] + '\n')
    for key, value in day["temperatures"].items():
        if value == None: 
            continue      
        else:
            time_of_day = key.capitalize().ljust(10, ' ')      
            temperature = round(value, 1)
            print(f"{time_of_day} - {temperature}")
    print("\n\n\n")  




# todo
# move diplay function to weather_display.py
# deal with half days and the final blank day
# get the midnight temp onto the correct day




    










