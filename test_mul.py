#!/usr/bin/python3

import unittest
from mul_fxn import mul
class testmul(unittest.TestCase):
    def test_mul(self):
        result = mul(5, 10)
        self.assertEqual(result, 50)

if __name__ == "__main__":
    unittest.main()
