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


if __name__ == "__main__":
    unittest.main()
