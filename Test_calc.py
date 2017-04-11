import unittest
from calculator import *

def setUpModule():
    print('set up module')

def tearDownModule():
    print('tear down module')

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        # Create an instance of the calculator that can be used in all tests
        self.calc = Calculator()

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9)

  # Write test methods for subtract, multiply, and divide

    def test_subract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_mulitply(self):
        self.assertEqual(self.calc.multiply(5, 4), 20)

    def test_divide(self):
        self.assertEqual(self.calc.divide(30, 6), 5)



if __name__ == '__main__':
    unittest.main()
