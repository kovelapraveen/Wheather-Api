'''
Utility functions for Weather CLI App
'''

def kelvin_to_celsius(k: float) -> float:
    return k - 273.15

def kelvin_to_fahrenheit(k: float) -> float:
    return (k - 273.15) * 9/5 + 32

def celsius_to_fahrenheit(c: float) -> float:
    return c * 9/5 + 32

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5/9