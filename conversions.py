
_ZERO_C_IN_KELVIN = 273.15


def convertCelsiusToKelvin(celsius):
    """
    Takes in a float representing a Celsius measurement
    returns that temperature converted into Kelvin
    """
    kelvin = celsius + 273.15

    return kelvin


def convertCelsiusToFahrenheit(celsius):
    """
    Takes in a float representing a Celsius measurement
    returns that temperature converted into Fahrenheit
    """
    fahrenheit = celsius * 9/5 + 32

    return fahrenheit


def convertFahrenheitToCelsius(fahrenheit):
    """
    Takes in a float representing a fahrenheit measurement
    returns that temperature converted into celsius
    """
    celsius = (fahrenheit - 32) * 5/9

    return celsius


def convertFahrenheitToKelvin(fahrenheit):
    """
    Takes in a float representing a Fahrenheit measurement
    returns that temperature converted into Kelvin
    """
    kelvin = (fahrenheit + 459.67) * 5/9

    return kelvin


def convertKelvinToCelsius(kelvin):
    """
    Takes in a float representing a Kelvin measurement
    and returns that temperature converted into Celsius
    """
    celsius = (kelvin + 273.15)

    return celsius


def convertKelvintoFahrenheit(kelvin):
    """
    Takes in a float representing a Kelvin measurement
    returns that temperature converted into Fahrenheit
    """
    fahrenheit = (kelvin * 9/5 - 459.67)

    return fahrenheit


def converMilesToMeters(miles):
    """Convert Miles to Meters"""
    result = 0

    return result
