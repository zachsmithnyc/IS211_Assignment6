from conversions import *


def convert(from_units, to_units, value):

    from_lcase = from_units.lower()
    to_lcase = to_units.lower()

    # from Celsius to Kelvin
    if from_lcase == 'celsius' and to_lcase == "kelvin":
        return convertCelsiusToKelvin(value)
    elif from_lcase == 'celsius' and to_lcase == "fahrenheit":
        return convertCelsiusToFahrenheit(value)
    elif from_lcase == 'kelvin' and to_lcase == "fahrenheit":
        return convertKelvintoFahrenheit(value)
    elif from_lcase == 'kelvin' and to_lcase == "celsius":
        return convertKelvinToCelsius(value)
    elif from_lcase == 'fahrenheit' and to_lcase == "celsius":
        return convertFahrenheitToCelsius(value)
    elif from_lcase == 'fahrenheit' and to_lcase == "kelvin":
        return convertFahrenheitToKelvin(value)
    
    # from Miles to Meters
    if from_lcase == "miles" and to_lcase == "meters":
        return convertMilesToMeters(value)
    elif from_lcase == "miles" and to_lcase == "yards":
        return convertMilesToYards(value)
    elif from_lcase == "meters" and to_lcase == "yards":
        return convertMetersToYards(value)
    elif from_lcase == "meters" and to_lcase == "miles":
        return convertMetersToMiles(value)
    elif from_lcase == "yards" and to_lcase == "miles":
        return convertYardsToMiles(value)
    elif from_lcase == "yards" and to_lcase == "meters":
        return convertYardsToMeters(value)
