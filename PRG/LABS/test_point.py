import unittest
 
from prg13.point import Point
 
class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p = Point(2, 5)
 
    def test_init(self):
        '''
        Test that p.x and p.y are set correctly.
        '''
        self.assertEqual(self.p.x, 2)
        self.assertEqual(self.p.y, 5)
 
    def test_str(self):
        '''
        Test that the __str__() returns a string in a correct format.
        '''
        string_p = str(self.p)
        self.assertEqual(string_p, "x = 2, y = 5")
 
    def test_eq(self):
        '''
        Test that the __eq__() function works as expected.
        '''
        self.assertEqual(self.p, Point(2, 5))
        self.assertNotEqual(self.p, Point(0, 5))
        self.assertNotEqual(self.p, Point(2, 0))
        self.assertNotEqual(self.p, Point(0, 0))
 
    def test_add(self):
        '''
        Test that the + operation return a correct type and answer
        '''
        p2 = Point(-5, 8)
        sum_p = self.p + p2
        self.assertIsInstance(sum_p, Point)
        self.assertEqual(sum_p, Point(-3, 13))
 
    def test_is_unit(self):
        '''
        Test that the test_is_unit() works as expected.
        '''
        p1 = Point(1, 0)
        p2 = Point(0, 1)
        p3 = Point(1, 1)
        p4 = Point(3/5, 4/5)
 
        self.assertTrue(p1.is_unit())
        self.assertTrue(p2.is_unit())
        self.assertFalse(p3.is_unit())
        self.assertTrue(p4.is_unit)

if __name__ == "__main__":
    unittest.main()