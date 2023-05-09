#!/usr/bin/python3

import unittest
from mul_fxn import mul

set0 = {"John", "Kings", "Odd_Name", "Marcell"}
set1 = {"Kings", "Marcell", "Odd_Name", "John"}
class testmul(unittest.TestCase):
    def test_mul(self):
        result = mul(5, 10)
        self.assertEqual(result, 50)

    def test_check0(self):
        self.assertTrue(3 > 0)

    def test_check1(self):
        self.assertSetEqual(set0, set1)

    def test_check2(self):
        self.assertTrue(30 >= 29)

    def test_check3(self):
        number = self.countTestCases()
        print(f"The number of test cases are: {number}.")

class testmul1(unittest.TestResult):
    def test_check0(self):
        self.wasSuccessful()

if __name__ == "__main__":
    unittest.main()
