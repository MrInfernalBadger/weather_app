import requests
import json
import pprint as pp

testing_state = True

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
    

print(len(weather_data["list"]))


    










