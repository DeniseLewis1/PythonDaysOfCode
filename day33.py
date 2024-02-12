# Write a test case for a function that checks if a number is prime

import unittest

def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
        return True
    return False

class TestIsPrime(unittest.TestCase):

    def test_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for num in primes:
            self.assertTrue(is_prime(num), f'{num} is not a prime number')
    
    def test_not_prime(self):
        not_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
        for num in not_primes:
            self.assertFalse(is_prime(num), f'{num} is a prime number')


if __name__ == '__main__':
    unittest.main()