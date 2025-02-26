import json
import pprint as pp
from datetime import datetime
from zoneinfo import ZoneInfo


with open("weather.json", "r") as file:
    weather_data = json.load(file)
    
    
def get_day_of_week_in_melbourne(timestamp):
    """Returns day of the week in melbourne from Unix timstamp
        e.g. 1740679200 returns Thursday

    Args:
        timestamp (): unix timestamp, 10 hours in seconds is removed from the 
        timestamp to account for the timezone

    Returns:
        str: Day of the week
    """
    return datetime.fromtimestamp(timestamp - (10*60*60)).strftime("%A")
    
    
# print(weather_data["list"])
# pp.pprint(weather_data["list"][0])

# print(weather_data["list"][0]["dt_txt"])

for segment in weather_data["list"]:
    
    day_of_week = get_day_of_week_in_melbourne(segment["dt"])
    print(day_of_week)    
    
    # print(datetime.fromtimestamp(segment["dt"]).strftime("%A"))
    
    
# weather_data = [
#     {
#         "day": "DATA", 
#         "weather": "DATA",
#         "morning_temp": "DATA",
#         "afternoon_temp": "DATA",
#         "evening_temp": "DATA",
#         "overnight_temp": "DATA"
#     },
#     {
#         "day": "DATA", 
#         "weather": "DATA",
#         "morning_temp": "DATA",
#         "afternoon_temp": "DATA",
#         "evening_temp": "DATA",
#         "overnight_temp": "DATA"
#     },
#     {
#         "day": "DATA", 
#         "weather": "DATA",
#         "morning_temp": "DATA",
#         "afternoon_temp": "DATA",
#         "evening_temp": "DATA",
#         "overnight_temp": "DATA"
#     },
    
# ]