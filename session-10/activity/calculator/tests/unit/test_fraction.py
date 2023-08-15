# IMPORT the `operations` module
import unittest

class TestFunctions(unittest.TestCase):

    def test_get_fractions(self):
    self.assertEqual(get_fractions("10"), 10)
    pass


def test_get_fractions_2(self):
    self.assertEqual(get_fractions("7/4"),1.75)
    
    pass

def test_get_fractions_3(self):
    self.assertEqual(get_fractions("-1"), -1)
    pass

if __name__ == '__main__':
    unittest.main()
