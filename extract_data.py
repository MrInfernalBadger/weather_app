import json
import pprint as pp
import numpy as np
import pytz

from datetime import datetime, timedelta
from collections import Counter


def load_weather_data_from_file():
    with open("test_weather_data.json", "r") as file:
        return json.load(file)
    
    
def get_day_of_week_from_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%A")
    
    
def simplify_weather_description(description):  
    if not description:
        return ""

    n = len(description)
    
    # Generate weights using a Gaussian-like curve centered at the middle of the list
    x = np.linspace(-1, 1, n)  # Evenly spaced numbers between -1 and 1
    weights = np.exp(-4 * x**2)  # Gaussian-like distribution

    # Create a weighted frequency counter
    word_weights = Counter()
    for word, weight in zip(description, weights):
        word_weights[word] += weight

    # Return the most weighted word
    return word_weights.most_common(1)[0][0]

 
def get_previous_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")  # Convert string to datetime
    previous_date = date_obj - timedelta(days=1)  # Subtract 1 day
    return previous_date.strftime("%Y-%m-%d")  # Convert back to string


def convert_gmt_to_melbourne(time_str):
    # Define timezones
    gmt = pytz.timezone("GMT")
    melbourne = pytz.timezone("Australia/Melbourne")

    # Convert input string to a datetime object in GMT
    gmt_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    gmt_time = gmt.localize(gmt_time)  # Set timezone to GMT

    # Convert GMT to Melbourne time
    melbourne_time = gmt_time.astimezone(melbourne)

    # Return formatted date-time in Melbourne time
    return melbourne_time.strftime("%Y-%m-%d %H:%M:%S")
   

def create_forecast_data(weather_data):
    times_list = []
    for segment in weather_data["list"]:
        segment["dt_txt"] = convert_gmt_to_melbourne(segment["dt_txt"])
        if segment["dt_txt"][11:13] not in times_list:
            times_list.append(segment["dt_txt"][11:13])
            
    times_list.sort()
    morning =   times_list[2]
    afternoon = times_list[4]
    evening =   times_list[6]
    midnight =  times_list[0]


        
    result = {}
    for segment in weather_data["list"]:
        segment_date = segment["dt_txt"][:10]
        segment_hour = segment["dt_txt"][11:13]
        
        if segment_date not in result:
            result[segment_date] = {              
                "temperatures": {                    
                    "morning": None,
                    "afternoon": None,
                    "evening": None,
                    "overnight": None
                    },
                "weather_list": [segment["weather"][0]["description"]],   
                "weather": "",
                "day": get_day_of_week_from_date(segment_date)
            }
            

        if segment_hour == morning:
            result[segment_date]["temperatures"]["morning"] = segment["main"]["temp"]
        elif segment_hour == afternoon:
            result[segment_date]["temperatures"]["afternoon"] = segment["main"]["temp"]
        elif segment_hour == evening:
            result[segment_date]["temperatures"]["evening"] = segment["main"]["temp"]
        elif segment_hour == midnight and len(result) > 1:                
            result[get_previous_date(segment_date)]["temperatures"]["overnight"] = segment["main"]["temp"]
            
        result[segment_date]["weather_list"].append(segment["weather"][0]["description"])
        
        
        if segment_hour == "11":
            result[segment_date]["weather"] = simplify_weather_description(result[segment_date]["weather_list"])

    return result




if __name__ == "__main__":
    test_data = load_weather_data_from_file()
    forecast_data = create_forecast_data(test_data)

    # pp.pprint(forecast_data)


    
   




# OUTPUT

# {'day': 'Thursday',
#                 'temperatures': {'afternoon': 20.18,
#                                  'evening': 19.31,
#                                  'morning': 23.83,
#                                  'overnight': 19.53},
#                 'weather': 'broken clouds',
#                 'weather_list': ['broken clouds',
#                                  'scattered clouds',
#                                  'broken clouds',
#                                  'scattered clouds',
#                                  'broken clouds',
#                                  'overcast clouds',
#                                  'overcast clouds',
#                                  'overcast clouds']},
#  '2025-02-28': {'day': 'Friday',
#                 'temperatures': {'afternoon': 18.96,
#                                  'evening': 16.63,
#                                  'morning': 23.01,
#                                  'overnight': 16.6},
#                 'weather': 'scattered clouds',
#                 'weather_list': ['broken clouds',
#                                  'broken clouds',
#                                  'broken clouds',
#                                  'scattered clouds',
#                                  'scattered clouds',
#                                  'few clouds',
#                                  'few clouds',
#                                  'clear sky']},
#  '2025-03-01': {'day': 'Saturday',
#                 'temperatures': {'afternoon': 18.36,
#                                  'evening': 16.23,
#                                  'morning': 22.85,
#                                  'overnight': 16.19},
#                 'weather': 'clear sky',
#                 'weather_list': ['clear sky',
#                                  'clear sky',
#                                  'clear sky',
#                                  'clear sky',
#                                  'clear sky',
#                                  'few clouds',
#                                  'scattered clouds',
#                                  'overcast clouds']},
#  '2025-03-02': {'day': 'Sunday',
#                 'temperatures': {'afternoon': 16.59,
#                                  'evening': 16.2,
#                                  'morning': 20.76,
#                                  'overnight': 16.33},
#                 'weather': 'broken clouds',
#                 'weather_list': ['overcast clouds',
#                                  'overcast clouds',
#                                  'broken clouds',
#                                  'scattered clouds',
#                                  'few clouds',
#                                  'broken clouds',
#                                  'overcast clouds',
#                                  'overcast clouds']},
#  '2025-03-03': {'day': 'Monday',
#                 'temperatures': {'afternoon': 19.24,
#                                  'evening': 16.28,
#                                  'morning': 20.92,
#                                  'overnight': 16.25},
#                 'weather': 'clear sky',
#                 'weather_list': ['overcast clouds',
#                                  'overcast clouds',
#                                  'broken clouds',
#                                  'clear sky',
#                                  'clear sky',
#                                  'few clouds',
#                                  'clear sky',
#                                  'clear sky']}}