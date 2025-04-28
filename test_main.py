import unittest
from main import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(9), "fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(10), "buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")

    def test_invalid_negative(self):
        with self.assertRaises(ValueError):
            fizzbuzz(-5)

    def test_invalid_zero(self):
        with self.assertRaises(ValueError):
            fizzbuzz(0)

    def test_invalid_not_multiple(self):
        with self.assertRaises(ValueError):
            fizzbuzz(1)

    def test_invalid_float(self):
        with self.assertRaises(ValueError):
            fizzbuzz(1.5)

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            fizzbuzz("abc")

if __name__ == "__main__":
    unittest.main()
