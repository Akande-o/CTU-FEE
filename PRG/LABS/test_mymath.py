import unittest

from prg13.mymath import abs
class TestMyMath(unittest.TestCase):
    def test_abs_positive(self):
        """
        Test that abs() of a positive number is exactly the same number
        """
        data = 8
        result = abs(data)
        self.assertEqual(result, 8)
    
    def test_abs_negative(self):
        """
        Test the abs( of a negative number is an additive inverse of the same number
        """
        data = -8
        result = abs(data)
        self.assertEqual(result, 8)

    def test_abs_string(self):
        """
        Test the abs() raises a ValueError when it is called with a string
        """
        data = "666"
        with self.assertRaises(ValueError):
            abs(data)

if __name__ == "__main__":
    unittest.main()
            