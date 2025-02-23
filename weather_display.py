##################################################################################
#     {day_of_the_week}    #     {day_of_the_week}    #     {day_of_the_week}    #
#    Weather - {weather}   #    Weather - {weather}   #    Weather - {weather}   #
#    High - {high_temp}    #    High - {high_temp}    #    High - {high_temp}    #
#    Low  - {low_temp}     #    Low  - {low_temp}     #    Low  - {low_temp}     #
#                          #                          #                          #
##################################################################################


weather_data = {"list": [
    {"day": "Monday", "weather": "Sunny", "high_temp": 30, "low_temp": 20},
    {"day": "Tuesday", "weather": "Cloudy", "high_temp": 25, "low_temp": 15},
    {"day": "Wednesday", "weather": "Rainy", "high_temp": 28, "low_temp": 18}
]}

result_lines = ["#", "#", "#", "#", "#"]


for value in weather_data["list"]:
    result = ''
    
    print(value["day"])
    print(result)