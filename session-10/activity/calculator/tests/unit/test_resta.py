# IMPORT the `operations` module
import unittest

class TestFunctions(unittest.TestCase):

def test_substract(self):
    # Float numbers
    # "0.5" - "0.5" = 0
    self.assertEqual(substract("0.5" - "0.5"), 0)
    pass
    


def test_substract_2(self):
    # Fraction numbers
    # "1/2" - "1" = -0.5
    self.assertEqual(substract("1/2" - "1"), -0.5)
    pass


def test_substract_3(self):
    # Result negative
    # "10" - "5" = 5
    self.assertEqual(substract("10" - "5" ), 5)
    pass

if __name__ == '__main__':
    unittest.main()
