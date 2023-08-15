# IMPORT the `operations` module
import unittest

class TestFunctions(unittest.TestCase):
    
    def test_sum(self):
    # Floats
    # "0.5" + "0.5" = 1
    self.assertEqual(sum("0.5" + "0.5"), 1)
    pass

def test_sum_2(self):
    # Negative numbers
    # "-3" + "-3" = -6
    self.assertEqual(sum("-3" + "-3"), -6)
    pass

def test_sum_3(self):
    # Positive numbers
    # "4" + "6" = 10
    self.assertEqual(sum("4" + "6"), 10)
    pass

if __name__ == '__main__':
    unittest.main()