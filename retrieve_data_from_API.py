import requests
import json


API_KEY = "c84da2e4454636df32c08657e3c94262"
CITY =    "Melbourne,AU"
URL =    f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
    
    
def get_weather_data(testing_state=False):   
     
    if testing_state:
        with open("weather.json", "r") as file:
            return json.load(file)
        
    else:
        response = requests.get(URL)

        if response.status_code == 200:
            return response.json()  
        else:
            print(f"Error: {response.status_code}, Message: {response.text}")
            return None