def format_weather_data(weather_data):
    # Extracting the list of weather data for each day
    days_data = weather_data.get("list", [])
    
    # Prepare strings for each column in the template
    day_of_the_week_str = []
    weather_str = []
    high_temp_str = []
    low_temp_str = []

    # Loop through each day and fill the columns
    LINE_JUSTIFICATION = 20
    spacer = " " * 4
    dash_row = f"{spacer}---".ljust(LINE_JUSTIFICATION, ' ')
    
    
    for day_info in days_data:
        day_of_the_week_str.append(f"{spacer}{day_info['day']}".ljust(LINE_JUSTIFICATION, ' '))
        weather_str.append(        f"{spacer}Weather - {day_info['weather']}".ljust(LINE_JUSTIFICATION, ' '))
        high_temp_str.append(      f"{spacer}High - {str(day_info['high_temp'])}".ljust(LINE_JUSTIFICATION, ' '))
        low_temp_str.append(       f"{spacer}Low  - {str(day_info['low_temp'])}".ljust(LINE_JUSTIFICATION, ' '))

    # Format the final output by combining all the columns
    row_length = len(f"#{day_of_the_week_str[0]}#{day_of_the_week_str[1]}#{day_of_the_week_str[2]}#")
           
    
    formatted_str = f"""
{'#' * row_length}
#{day_of_the_week_str[0]}#{day_of_the_week_str[1]}#{day_of_the_week_str[2]}#
#{dash_row}#{dash_row}#{dash_row}#
#{weather_str[0]}#{weather_str[1]}#{weather_str[2]}#
#{high_temp_str[0]}#{high_temp_str[1]}#{high_temp_str[2]}#
#{low_temp_str[0]}#{low_temp_str[1]}#{low_temp_str[2]}#
#{' ' * (LINE_JUSTIFICATION)}#{' ' * (LINE_JUSTIFICATION)}#{' ' * (LINE_JUSTIFICATION)}#
{'#' * row_length}
"""


    return formatted_str


# Example weather data
weather_data = {
    "list": [
        {"day": "Monday", "weather": "Sunny", "high_temp": 30, "low_temp": 20},
        {"day": "Tuesday", "weather": "Cloudy", "high_temp": 25, "low_temp": 15},
        {"day": "Wednesday", "weather": "Rainy", "high_temp": 28, "low_temp": 18}
    ]
}

# Call the function and print the result
print(format_weather_data(weather_data))

