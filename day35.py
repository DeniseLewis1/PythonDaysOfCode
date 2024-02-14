# Write a simple unit test for a function that adds two numbers

import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):

    def test_add_nums(self):
        self.assertEqual(add_numbers(5, 10), 15)
        self.assertEqual(add_numbers(4.5, 7.25), 11.75)
        self.assertNotEqual(add_numbers(25, 17), 100)

if __name__ == '__main__':
    unittest.main()