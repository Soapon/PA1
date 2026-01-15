import unittest
from TempConv import (
    C_to_K, K_to_C, F_to_K, K_to_F,
    check_unit, convert_to_K, convert_from_K,
    check_reality
)


class TestTemperatureConversions(unittest.TestCase):
    #C_to_K
    def test_C_to_K(self):
        assert C_to_K(0) == 273.15
        assert C_to_K(100) == 373.15
    #K_to_C
    def test_K_to_C(self):
        assert K_to_C(273.15) == 0.0
        assert K_to_C(373.15) == 100.0
    #F_to_K
    def test_F_to_K(self):
        assert F_to_K(32) == 273.15
        assert F_to_K(212) == 373.15
    #K_to_F
    def test_K_to_F(self):
        assert K_to_F(273.15) == 32.0
        assert K_to_F(0) == -459.67
    
    def test_check_unit_valid(self):
        self.assertIsNone(check_unit('C'))
        self.assertIsNone(check_unit('F'))
        self.assertIsNone(check_unit('K'))
    #check_unit
    def test_check_unit_invalid(self):
        self.assertEqual(check_unit('X'), ValueError)

   #convert_to_K 
    def test_convert_to_K(self):
        self.assertEqual(convert_to_K(0, 'C'), 273.15)
        self.assertEqual(convert_to_K(32, 'F'), 273.15)
        self.assertEqual(convert_to_K(300, 'K'), 300)
    
    def test_convert_from_K(self):
        self.assertEqual(convert_from_K(273.15, 'C'), 0.0)
        self.assertEqual(convert_from_K(273.15, 'F'), 32.0)
        self.assertEqual(convert_from_K(300, 'K'), 300)
    #check_reality
    def test_check_reality_valid(self):
        self.assertIsNone(check_reality(0))
        self.assertIsNone(check_reality(273.15))
    #check_reality
    def test_check_reality_invalid(self):
        self.assertEqual(check_reality(-5), ValueError)

#Run the tests
if __name__ == '__main__':
    unittest.main()