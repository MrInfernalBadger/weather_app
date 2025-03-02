##################################################################################
#     {day_of_the_week}    #     {day_of_the_week}    #     {day_of_the_week}    #
#    Weather - {weather}   #    Weather - {weather}   #    Weather - {weather}   #
#    High - {high_temp}    #    High - {high_temp}    #    High - {high_temp}    #
#    Low  - {low_temp}     #    Low  - {low_temp}     #    Low  - {low_temp}     #
#                          #                          #                          #
##################################################################################


# Today
## Weather
## Morning - 6am
## Afternoon - 12pm
## Evening - 6pm
## Overnight - 12am


# Tomorrow
## Weather
## Morning - 6am
## Afternoon - 12pm
## Evening - 6pm
## Overnight - 12am


# Next day
## Weather
## Morning - 6am
## Afternoon - 12pm
## Evening - 6pm
## Overnight - 12am

test_data = {'2025-03-02': {'day': 'Sunday',
                'temperatures': {'afternoon': 16.05,
                                 'evening': 14.27,
                                 'morning': 19.41,
                                 'overnight': 14.36},
                'weather': 'scattered clouds',
                'weather_list': ['light rain',
                                 'overcast clouds',
                                 'broken clouds',
                                 'scattered clouds',
                                 'clear sky',
                                 'scattered clouds',
                                 'overcast clouds']},
 '2025-03-03': {'day': 'Monday',
                'temperatures': {'afternoon': 16.66,
                                 'evening': 14.14,
                                 'morning': 20.6,
                                 'overnight': 13.43},
                'weather': 'clear sky',
                'weather_list': ['overcast clouds',
                                 'scattered clouds',
                                 'few clouds',
                                 'clear sky',
                                 'clear sky',
                                 'few clouds',
                                 'few clouds',
                                 'clear sky']},
 '2025-03-04': {'day': 'Tuesday',
                'temperatures': {'afternoon': 21.54,
                                 'evening': 19.64,
                                 'morning': 26.21,
                                 'overnight': 21.11},
                'weather': 'clear sky',
                'weather_list': ['clear sky',
                                 'clear sky',
                                 'clear sky',
                                 'clear sky',
                                 'clear sky',
                                 'clear sky',
                                 'clear sky',
                                 'clear sky']},
 '2025-03-05': {'day': 'Wednesday',
                'temperatures': {'afternoon': 19.66,
                                 'evening': 17.55,
                                 'morning': 24.84,
                                 'overnight': 17.59},
                'weather': 'clear sky',
                'weather_list': ['clear sky',
                                 'clear sky',
                                 'clear sky',
                                 'clear sky',
                                 'few clouds',
                                 'light rain',
                                 'light rain',
                                 'light rain']},
 '2025-03-06': {'day': 'Thursday',
                'temperatures': {'afternoon': 19,
                                 'evening': 17.3,
                                 'morning': 22.37,
                                 'overnight': 17.22},
                'weather': 'overcast clouds',
                'weather_list': ['overcast clouds',
                                 'overcast clouds',
                                 'overcast clouds',
                                 'overcast clouds',
                                 'broken clouds',
                                 'scattered clouds',
                                 'few clouds',
                                 'clear sky']},
 '2025-03-07': {'day': 'Friday',
                'temperatures': {'afternoon': None,
                                 'evening': None,
                                 'morning': None,
                                 'overnight': None},
                'weather': '',
                'weather_list': ['clear sky']}}





def print_weather_data(weather_data):
    for day in weather_data.values():
        if not day["temperatures"]["morning"]:
            continue
        print(f"----{day['day']}----")
        print(day['weather'] + '\n')
        for key, value in day["temperatures"].items():
            if value == None: 
                continue      
            else:
                time_of_day = key.capitalize().ljust(10, ' ')      
                temperature = round(value, 1)
                print(f"{time_of_day} - {temperature}")
        print("\n\n")  
        
        
        
if __name__ == "__main__":
    print_weather_data(test_data)

