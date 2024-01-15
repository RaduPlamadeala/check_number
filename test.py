import unittest

from check_number import comprova_signe

class TestSigne(unittest.TestCase):
    def test_num_positiu(self):
        """Test per a comprovar que el numero donat es positiu"""
        data = 2
        result = comprova_signe(2)
        self.assertEqual(result, 1)
    
    def test_num_negatiu(self):
        """Test per a comprovar que el numero donat es negatiu"""
    
        data = -5
        result = comprova_signe(data)
        self.assertEqual(result, -1)
    
    def test_num_zero(self):
        """Test per a comprovar que el numero es 0"""

        data = 0
        result = comprova_signe(data)
        self.assertEqual(result, 0)
    

if __name__ == '__main__':
    unittest.main()