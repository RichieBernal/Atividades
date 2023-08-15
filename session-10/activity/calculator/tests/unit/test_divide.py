# IMPORT the `operations` module
import unittest

class TestFunctions(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide('10/2'), 5)
        pass
   
    def test_divide(self):
        self.assertEqual(divide("-15/4" / "1/2"),-7.5) 
        pass


    def test_divide(self):
        self.assertEqual(divide("8"/"16", 0.5)
    pass
    
    if __name__ == '__main__':
    unittest.main()