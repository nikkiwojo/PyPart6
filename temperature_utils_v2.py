import math

def fahrenheit_to_kelvin(original_temp: float) -> float:
    kelvin = round(((5 / 9) * (original_temp - 32) + 273.15), 2)
    return kelvin

def celsius_to_kelvin(original_temp: float) -> float:
    kelvin = round((original_temp + 273.15), 2)
    return kelvin