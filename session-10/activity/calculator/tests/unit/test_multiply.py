# IMPORT the `operations` module
import unittest

class TestFunctions(unittest.TestCase):

    def test_multiply(self):
    # Negative numbers
    # "-2" * "3" = -6
    self.assertEqual(multiply("-2" * "3"), -6)
    pass


def test_multiply(self):
    # Fractions
    # "1/2" * "8/4" = 1
    self.assertEqual(multiply("1/2" * "8/4"), 1)
    pass


def test_multiply(self):
    # Positive numbers
    # "10" * "5" = 50
    self.assertEqual(multiply("10" * "5"), 50) 
    pass

if __name__ == '__main__':
    unittest.main()

