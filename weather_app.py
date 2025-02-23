import requests
import json
import pprint as pp

with open("response.json", "r") as f:
    data = json.load(f)
pp.pprint(data)


# API_KEY = "c84da2e4454636df32c08657e3c94262"
# CITY = "Melbourne"
# # URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
# # URL = f"http://api.openweathermap.org/geo/1.0/direct?q={CITY}&limit={2}&appid={API_KEY}"

# URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"



# response = requests.get(URL)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
#     # weather = data["weather"][0]["description"]
#     # temp = data["main"]["temp"]
#     # print(f"Weather in {CITY}: {weather}, {temp}°C")
# else:
#     print(f"Error: {response.status_code}, Message: {response.text}")









