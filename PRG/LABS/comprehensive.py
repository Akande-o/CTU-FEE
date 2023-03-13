def abs_2(x):
    """Return an absolute value of x-2, i.e., y=|x-2|.
 
    :param x: int, float. 
    :return: int, float. The absolute value of x-2.
    >>> abs_2(0)
    2
    """
    y = x-2
    if y < 0:
        return -y
    else:
        return y

def abs_2_list(lst):
    """Return a list of absolute values of x-2, where x's are elements of lst.
 
    :param lst: list of ints/floats. 
    :return: list of ints/floats.
    >>> abs_2_list([0, 2, 4])
    [2, 0, 2]
    """
    abs_list = []
    for num in lst:
        y = abs(num - 2)
        abs_list.append(y)
    return abs_list

def sum_file(file_name):
    """Return a list of row sums.
 
    :param file_name: Path to a text file. 
    :return: list of ints/floats.
    >>> sum_file("number_file.txt")
    [10, 237, 43, -8, 12]
    """
    sum_list = []
    with open(file_name, "r", encoding = 'utf-8') as f:
        for line in f:
            number = 0
            line = line.strip()
            digits = line.split(",")
            for char in digits:
                number += int(char)
            sum_list.append(number)
    return sum_list

import unittest
 
class ColorRGB:
    """Represents a color in the R (red), G (green), B (blue) format."""
    def __init__(self, red, green, blue):
        self.red = red
        self.blue = blue
        self.green = green
    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __add__(self, other):
        sum_red = min(self.red + other.red, 255)
        sum_green = min(self.green + other.green, 255)
        sum_blue = min(self.blue + other.blue, 255)
        return ColorRGB(sum_red, sum_green, sum_blue)

        
    def __str__(self):
        return "ColorRGB({},{},{})".format(self.red, self.green, self.blue)
 
class TestColorRGB(unittest.TestCase):
    """Test ColorRGB methods"""
 
    def test_init(self):
        """Test that the initializer method __init__ takes 3 parameters"""
        ColorRGB(255, 0, 255)
 
    def test_str(self):
        """Test string conversion"""
        self.assertEqual("ColorRGB(0,127,127)", str(ColorRGB(0, 127, 127)))
 
    def test_eq(self):
        """Test deep equality for two ColorRGB instances"""
        self.assertEqual(ColorRGB(0,30,255), ColorRGB(0,30,255))
 
    def test_add(self):
        """Test the plus operator between two instances of the ColorRGB class"""
        color1 = ColorRGB(30, 100, 255)
        color2 = ColorRGB(0, 255, 30)
        self.assertEqual(ColorRGB(30, 255, 255), color1 + color2)
        self.assertEqual(ColorRGB(30, 100, 255), color1)
        self.assertEqual(ColorRGB(0, 255, 30), color2)
import random
def random_integers(length, lower_bound, upper_bound):
    """Build a list of randomly chosen integers.
 
    :param length: Length of the resulting list
    :param lower_bound: Lower bound of each random integer (INCLUDED)
    :param upper_bound: Upper bound of each random integer (INCLUDED)
    :return: List of random integers
    """
    rng = random.Random()
    rand_list = []
    for i in range(length):
        integer = rng.randrange(lower_bound, upper_bound + 1)
        rand_list.append(integer)
    return rand_list

fruits = ["apple", "banana", "pear", "kiwi", "strawberry", "lime", "lemon", "orange"]
upper_even = [fruit.upper() for fruit in fruits if len(fruit)%2 == 0 ]
print(upper_even)

abs_value = [abs(x-2) for x in range(-10, 11)]
print(abs_value)


 
if __name__ == "__main__":
    # Execute all unit tests
    unittest.main()
if __name__ == "__main__":
    import doctest
    doctest.testmod()

