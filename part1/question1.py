################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/
#
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

from enum import Enum

# Define an enumeration for city data keys
class CityKeys(Enum):
    TEMPERATURE = 'temperature'  # Key for temperature
    SKY_CONDITION = 'sky_condition'  # Key for sky condition

# Error message when the city is not found
ERROR_OPTION = "Error, the city you're trying to look up is not registered"

# Dictionary that stores city data
cities = {
    "Quito":      {CityKeys.TEMPERATURE: 22, CityKeys.SKY_CONDITION: 'sunny'},
    "Sao Paulo":  {CityKeys.TEMPERATURE: 17, CityKeys.SKY_CONDITION: 'cloudy'},
    "New York":   {CityKeys.TEMPERATURE: 14, CityKeys.SKY_CONDITION: 'rainy'}
}

# Function to get the weather of a city
def get_city_weather(city):
    """
    This function takes the name of a city as input and returns the weather information.

    Args:
        city (str): The name of the city for which you want to retrieve the weather.

    Returns:
        str: A string describing the temperature and sky condition of the city.
             In case the city is not registered, an error message is returned.
    """
    if city in cities:
        city_data = cities[city]
        temperature = city_data[CityKeys.TEMPERATURE]
        sky_condition = city_data[CityKeys.SKY_CONDITION]
        return f"{temperature} degrees and {sky_condition}"
    else:
        return ERROR_OPTION
