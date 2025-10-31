import unittest
import math
from circle import area, perimeter

class TestCircle(unittest.TestCase):

    def test_area_positive(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(2), math.pi * 4)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            perimeter(-3)


if __name__ == '__main__':
    unittest.main()
