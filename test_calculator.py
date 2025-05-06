import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        from calculator import Calculator
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.evaluate("2+3"), 5.0)

    def test_subtraction(self):
        self.assertEqual(self.calc.evaluate("10-4"), 6.0)

    def test_multiplication(self):
        self.assertEqual(self.calc.evaluate("3*7"), 21.0)

    def test_precedence(self):
        self.assertEqual(self.calc.evaluate("2+3*4"), 14.0)

    def test_floating_point(self):
        self.assertAlmostEqual(self.calc.evaluate("2.5*4"), 10.0)

    def test_complex(self):
        self.assertEqual(self.calc.evaluate("2+3*4-5"), 9.0)

if __name__ == "__main__":
    unittest.main()
