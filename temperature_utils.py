from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    celsius = round((5 / 9 * (fahrenheit_temp - 32)), 2)
    return celsius


def convert_to_fahrenheit(celsius_temp: float) -> int:
    fahrenheit = round((9 / 5 * celsius_temp + 32), 2)
    return fahrenheit


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    new_list = []
    if input_unit_of_measurement == "c":
        for x in temperatures:
            fahr = round((9 / 5 * x + 32), 2)
            new_list.append((x,fahr))
        return tuple(new_list)
    elif input_unit_of_measurement =="f":
        for x in temperatures:
            cel = round((5 / 9 * (x - 32)), 2)
            new_list.append((x,cel))
        return tuple(new_list)
    else:
        return ()

