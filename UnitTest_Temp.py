import unittest
from TempConv import (
    C_to_K, K_to_C, F_to_K, K_to_F,
    check_unit, convert_to_K, convert_from_K,
    check_reality
)


class TestTemperatureConversions(unittest.TestCase):
    
    def test_C_to_K(self):
        """Test Celsius to Kelvin conversion"""
        self.assertEqual(C_to_K(0), 273.15)
        self.assertEqual(C_to_K(100), 373.15)
    
    def test_K_to_C(self):
        """Test Kelvin to Celsius conversion"""
        self.assertEqual(K_to_C(273.15), 0.0)
        self.assertEqual(K_to_C(373.15), 100.0)
    
    def test_F_to_K(self):
        """Test Fahrenheit to Kelvin conversion"""
        self.assertEqual(F_to_K(32), 273.15)
        self.assertEqual(F_to_K(212), 373.15)
    
    def test_K_to_F(self):
        """Test Kelvin to Fahrenheit conversion"""
        self.assertEqual(K_to_F(273.15), 32.0)
        self.assertEqual(K_to_F(0), -459.67)
    
    def test_check_unit_valid(self):
        """Test check_unit with valid units"""
        self.assertIsNone(check_unit('C'))
        self.assertIsNone(check_unit('F'))
        self.assertIsNone(check_unit('K'))
    
    def test_check_unit_invalid(self):
        """Test check_unit with invalid unit"""
        self.assertEqual(check_unit('X'), ValueError)
    
    def test_convert_to_K(self):
        """Test convert_to_K function"""
        self.assertEqual(convert_to_K(0, 'C'), 273.15)
        self.assertEqual(convert_to_K(32, 'F'), 273.15)
        self.assertEqual(convert_to_K(300, 'K'), 300)
    
    def test_convert_from_K(self):
        """Test convert_from_K function"""
        self.assertEqual(convert_from_K(273.15, 'C'), 0.0)
        self.assertEqual(convert_from_K(273.15, 'F'), 32.0)
        self.assertEqual(convert_from_K(300, 'K'), 300)
    
    def test_check_reality_valid(self):
        """Test check_reality with valid temperatures"""
        self.assertIsNone(check_reality(0))
        self.assertIsNone(check_reality(273.15))
    
    def test_check_reality_invalid(self):
        """Test check_reality with temperature below absolute zero"""
        self.assertEqual(check_reality(-5), ValueError)


if __name__ == '__main__':
    unittest.main()