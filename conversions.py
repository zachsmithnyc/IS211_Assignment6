
_ZERO_C_IN_KELVIN = 273.15

#convert temperature
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
    celsius = (kelvin - 273.15)

    return celsius


def convertKelvintoFahrenheit(kelvin):
    """
    Takes in a float representing a Kelvin measurement
    returns that temperature converted into Fahrenheit
    """
    fahrenheit = (kelvin * 9/5 - 459.67)

    return fahrenheit

#convert length 
def convertMilesToMeters(miles):
    """Convert Miles to Meters"""
    meters = miles * 1609.34

    return meters 

def convertMilesToYards(miles):
    """Convert Miles to Yards"""
    yards = miles * 1760

    return yards

def convertMetersToMiles(meters):
    """Convert Meters to Miles"""
    miles = meters / 1609.34

    return miles

def convertMetersToYards(meters):
    """Convert Meters to Yardss"""
    yards = meters * 1.09361

    return yards

def convertYardsToMeters(yards):
    """Convert Yardss to Meters"""
    meters = yards / 1.09361

    return meters

def convertYardsToMiles(yards):
    """Convert Yards to Miles"""
    miles = yards / 1760

    return miles
