import json
import pprint as pp
import numpy as np

from datetime import datetime
from collections import Counter



def load_weather_data_from_file():
    with open("weather.json", "r") as file:
        return json.load(file)
    
    
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
    
    
def get_day_of_week_from_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%A")
    
    
def simplify_weather_description(description):    

    # if len(description) != 8:
    #     print(f"List contained ({len(description)}) items, expected 8")
    #     return "ERROR"

    # # Approximate bell curve weights for an 8-item list
    # weights = [0.1, 0.2, 0.4, 0.8, 0.8, 0.4, 0.2, 0.1]

    # # Create a weighted frequency counter
    # word_weights = Counter()
    # for word, weight in zip(description, weights):
    #     word_weights[word] += weight

    # # Return the word with the highest weight
    # return word_weights.most_common(1)[0][0]



  # For generating weights

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




def create_forecast_data(weather_data):
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
        else:
            if segment_hour == "06":
                result[segment_date]["temperatures"]["morning"] = segment["main"]["temp"]
            elif segment_hour == "12":
                result[segment_date]["temperatures"]["afternoon"] = segment["main"]["temp"]
            elif segment_hour == "18":
                result[segment_date]["temperatures"]["evening"] = segment["main"]["temp"]
            elif segment_hour == "21": #NOT TAKING TEMPERATURE FROM MIDNIGHT AS INTENDED
                result[segment_date]["temperatures"]["overnight"] = segment["main"]["temp"]
                
                
            result[segment_date]["weather_list"].append(segment["weather"][0]["description"])
            
            
            if segment_hour == "21":
                result[segment_date]["weather"] = simplify_weather_description(result[segment_date]["weather_list"])

    return result


if __name__ == "__main__":
    test_data = load_weather_data_from_file()
    forecast_data = create_forecast_data(test_data)
    pp.pprint(forecast_data)
   




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