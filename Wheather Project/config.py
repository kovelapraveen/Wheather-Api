'''
Configuration for Weather CLI App
'''

import os

API_KEY = os.getenv('OPENWEATHER_API_KEY', '2ccc774223a064e049caf921a416f9ed')

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

DEFAULT_UNITS = 'metric'  # metric=Celsius, imperial=Fahrenheit, standard=Kelvin
DEFAULT_LANG = 'en'