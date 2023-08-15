import get_fractions
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_integration(self):
        self.assertEqual(multiply(sum(5, 5), substract(1.25, 0.75)), 5)
        self.assertEqual(multiply(sum(8, 7/5), substract(15, 3/8)), 137.475)
        pass

if __name__ == '__main__':
    unittest.main()