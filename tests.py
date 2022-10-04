# Let's import everything from conversion
from conversions import *
from conversions_refactored import convert

import unittest


class ConversionTest(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        celsius = 0
        result = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertEqual(result, expected)

        result = convertCelsiusToKelvin(300)
        expected = 573.15
        self.assertEqual(result, expected)

        result = convertCelsiusToKelvin(500)
        expected = 773.15
        self.assertEqual(result, expected)

        result = convertCelsiusToKelvin(30)
        expected = 303.15
        self.assertEqual(result, expected)

        result = convertCelsiusToKelvin(20)
        expected = 293.15
        self.assertEqual(result, expected)


    def test_convertCelsiusToFahrenheit(self):

        result = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertEqual(result, expected)

        result = convertCelsiusToFahrenheit(21)
        expected = 69.8
        self.assertEqual(result, expected)

        result = convertCelsiusToFahrenheit(30)
        expected = 86
        self.assertEqual(result, expected)

        result = convertCelsiusToFahrenheit(40)
        expected = 104
        self.assertEqual(result, expected)

        result = convertCelsiusToFahrenheit(500)
        expected = 932
        self.assertEqual(result, expected)

    def test_convertFahrenheitToCelsius(self):

        result = convertFahrenheitToCelsius(32)
        expected = 0
        self.assertEqual(result, expected)

        result = convertFahrenheitToCelsius(40)
        expected = 4.444444
        self.assertAlmostEqual(result, expected, places=6)

        result = convertFahrenheitToCelsius(50)
        expected = 10
        self.assertEqual(result, expected)

        result = convertFahrenheitToCelsius(68)
        expected = 20
        self.assertEqual(result, expected)

        result = convertFahrenheitToCelsius(932)
        expected = 500
        self.assertEqual(result, expected)

    def test_convertFahrenheittoKelvin(self):
        
        result = convertFahrenheitToKelvin(14)
        expected = 263.15
        self.assertEqual(result, expected)

        result = convertFahrenheitToKelvin(32)
        expected = 273.15
        self.assertEqual(result, expected)

        result = convertFahrenheitToKelvin(50)
        expected = 283.15
        self.assertEqual(result, expected)

        result = convertFahrenheitToKelvin(68)
        expected = 293.15
        self.assertAlmostEqual(result, expected, places=5)

        result = convertFahrenheitToKelvin(500)
        expected = 533.15
        self.assertAlmostEqual(result, expected, places=5)

    def test_convertKelvinToCelsius(self):
        
        result = convertKelvinToCelsius(0)
        expected = -273.15
        self.assertEqual(result, expected)

        result = convertKelvinToCelsius(43.15)
        expected = -230
        self.assertAlmostEqual(result, expected, places=5)

        result = convertKelvinToCelsius(283.15)
        expected = 10
        self.assertEqual(result, expected)

        result = convertKelvinToCelsius(300)
        expected = 26.85
        self.assertAlmostEqual(result, expected, places=4)

        result = convertKelvinToCelsius(500)
        expected = 226.85
        self.assertAlmostEqual(result, expected, places=5)

    def test_convertKelvintoFahrenheit(self):
        
        result = convertKelvintoFahrenheit(0)
        expected = -459.67
        self.assertEqual(result, expected)

        result = convertKelvintoFahrenheit(100)
        expected = -279.67
        self.assertEqual(result, expected)

        result = convertKelvintoFahrenheit(33.15)
        expected = -400
        self.assertEqual(result, expected)

        result = convertKelvintoFahrenheit(333.15)
        expected = 140
        self.assertAlmostEqual(result, expected)

        result = convertKelvintoFahrenheit(500)
        expected = 440.33
        self.assertEqual(result, expected)

    def test_convertMilesToMeters(self):
        
        result = convertMilesToMeters(1)
        expected = 1609.34
        self.assertEqual(result, expected)

        result = convertMilesToMeters(15)
        expected = 24140.1
        self.assertEqual(result, expected)

        result = convertMilesToMeters(30)
        expected = 48280.2
        self.assertEqual(result, expected)

        result = convertMilesToMeters(2)
        expected = 3218.68
        self.assertEqual(result, expected)

        result = convertMilesToMeters(500)
        expected = 804670.0
        self.assertEqual(result, expected)

    def test_convertMilestoYards(self):

        result = convertMilesToYards(1)
        expected = 1760
        self.assertEqual(result, expected)

        result = convertMilesToYards(2)
        expected = 3520
        self.assertEqual(result, expected)

        result = convertMilesToYards(50)
        expected = 88000
        self.assertEqual(result, expected)

        result = convertMilesToYards(100)
        expected = 176000
        self.assertEqual(result, expected)

        result = convertMilesToYards(500)
        expected = 880000
        self.assertEqual(result, expected)

    def test_convertMeterstoMiles(self):

        result = convertMetersToMiles(1)
        expected = 0.000621371
        self.assertAlmostEqual(result, expected, places=6)

        result = convertMetersToMiles(10)
        expected = 0.00621371
        self.assertAlmostEqual(result, expected, places=6)

        result = convertMetersToMiles(500)
        expected = 0.310686
        self.assertAlmostEqual(result, expected, places=6)

        result = convertMetersToMiles(700)
        expected = 0.43496
        self.assertAlmostEqual(result, expected, places=5)

        result = convertMetersToMiles(2000)
        expected = 1.242742
        self.assertAlmostEqual(result, expected, places=5)

    def test_convertMeterstoYards(self):

        result = convertMetersToYards(1)
        expected = 1.09361
        self.assertAlmostEqual(result, expected, places=6)

        result = convertMetersToYards(15)
        expected = 16.4042
        self.assertAlmostEqual(result, expected, places=4)

        result = convertMetersToYards(50)
        expected = 54.6805
        self.assertAlmostEqual(result, expected, places=5)

        result = convertMetersToYards(100)
        expected = 109.361
        self.assertAlmostEqual(result, expected, places=6)

        result = convertMetersToYards(500)
        expected = 546.805
        self.assertAlmostEqual(result, expected, places=6)

    def test_convertYardstoMiles(self):

        result = convertYardsToMiles(1)
        expected = 0.000568182
        self.assertAlmostEqual(result, expected, places=6)

        result = convertYardsToMiles(200)
        expected = 0.113636
        self.assertAlmostEqual(result, expected, places=6)

        result = convertYardsToMiles(500)
        expected = 0.284091
        self.assertAlmostEqual(result, expected, places=6)

        result = convertYardsToMiles(1000)
        expected = 0.568182
        self.assertAlmostEqual(result, expected, places=6)

        result = convertYardsToMiles(5000)
        expected = 2.840909
        self.assertAlmostEqual(result, expected, places=6)

    def test_convertYardstoMeters(self):

        result = convertYardsToMeters(1)
        expected = 0.91407
        self.assertAlmostEqual(result, expected, places=4)

        result = convertYardsToMeters(15)
        expected = 13.7111517
        self.assertAlmostEqual(result, expected, places=4)

        result = convertYardsToMeters(30)
        expected = 27.4223
        self.assertAlmostEqual(result, expected, places=3)

        result = convertYardsToMeters(100)
        expected = 91.4076
        self.assertAlmostEqual(result, expected, places=3)

        result = convertYardsToMeters(500)
        expected = 457.038391
        self.assertAlmostEqual(result, expected, places=4)


    def testconvert(self):
        celsius = 0
        result = convert("Celsius", "Kelvin", celsius)
        expected = 273.15
        self.assertEqual(result, expected)

        celsius = 0
        result = convert("Celsius", "Fahrenheit", celsius)
        expected = 32
        self.assertEqual(result, expected)

        fahrenheit = 32
        result = convert("Fahrenheit", "Celsius", fahrenheit)
        expected = 0
        self.assertEqual(result, expected)

        fahrenheit = 32
        result = convert("Fahrenheit", "Kelvin", fahrenheit)
        expected = 273.15
        self.assertEqual(result, expected)

        kelvin = 273.15
        result = convert("Kelvin", "Fahrenheit", kelvin)
        expected = 32
        self.assertEqual(result, expected)

        kelvin = 273.15
        result = convert("Kelvin", "Celsius", kelvin)
        expected = 0
        self.assertEqual(result, expected)

        miles = 1
        result = convert("Miles", "Meters", miles)
        expected = 1609.34
        self.assertEqual(result, expected)

        miles = 1
        result = convert("Miles", "Yards", miles)
        expected = 1760
        self.assertEqual(result, expected)

        meters = 1609.34
        result = convert("Meters", "Miles", meters)
        expected = 1
        self.assertEqual(result, expected)

        meters = 1609.34
        result = convert("Meters", "Yards", meters)
        expected = 1759.9903173999
        self.assertAlmostEqual(result, expected, places=5)

        yards = 5000
        result = convert("Yards", "Miles", yards)
        expected = 2.840909
        self.assertAlmostEqual(result, expected, places=6)

        yards = 500
        result = convert("Yards", "Meters", yards)
        expected = 457.038391
        self.assertAlmostEqual(result, expected, places=6)








if __name__ == "__main__":
    unittest.main()
