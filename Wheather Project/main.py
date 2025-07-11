#!/usr/bin/env python3
'''
Weather CLI App
'''

import sys
import argparse
import requests
from typing import Dict, Any

import config
import utils

def fetch_weather(city: str, units: str = config.DEFAULT_UNITS, lang: str = config.DEFAULT_LANG) -> Dict[str, Any]:
    params = {
        'q': city,
        'appid': config.API_KEY,
        'units': units,
        'lang': lang
    }
    resp = requests.get(config.BASE_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def print_weather(data: Dict[str, Any], units: str) -> None:
    name = data.get('name')
    weather_desc = data['weather'][0]['description'].title()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    unit_symbol = '°C' if units == 'metric' else '°F' if units == 'imperial' else 'K'

    print(f'\nWeather in {name}:')
    print(f'  🌡  Temperature: {temp}{unit_symbol}')
    print(f'  💧  Humidity:    {humidity}%')
    print(f'  ☁️   Condition:   {weather_desc}')
    print(f'  💨  Wind Speed:  {wind_speed} m/s\n')

def main() -> None:
    parser = argparse.ArgumentParser(description='Get current weather for a city.')
    parser.add_argument('city', nargs='?', help='City name (e.g., London)')
    parser.add_argument('-u', '--units', choices=['standard', 'metric', 'imperial'],
                        default=config.DEFAULT_UNITS, help='Units: standard (Kelvin), metric (Celsius), imperial (Fahrenheit)')
    parser.add_argument('-l', '--lang', default=config.DEFAULT_LANG, help='Language code for description (default: en)')
    args = parser.parse_args()

    city = args.city or input('Enter city name: ').strip()
    if not city:
        sys.exit('City name cannot be empty.')

    try:
        data = fetch_weather(city, units=args.units, lang=args.lang)
        print_weather(data, units=args.units)
    except KeyboardInterrupt:
        print('\nCancelled by user.')
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            print('City not found. Please check the spelling.')
        else:
            print('Error while fetching weather data:', e)
    except requests.RequestException as e:
        print('Network error:', e)

if __name__ == '__main__':
    main()