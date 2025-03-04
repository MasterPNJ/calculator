from unittest import TestCase
from src.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.mysum(1, 2), 3)
        
    def test_average(self):
        self.assertEqual(self.calc.myaverage(2, 4), 3)
        self.assertEqual(self.calc.myaverage(10, 20), 15)
        self.assertAlmostEqual(self.calc.myaverage(1, 2), 1.5)

    
    
if __name__ == '__main__':
    unittest.main()