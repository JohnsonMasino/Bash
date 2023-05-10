#!/usr/bin/python3

import unittest as ut

a = 5 * 7
b = 30
l1 = {"Name", "Occupation", "Hobby"}
l2 = {"Occupation", "Hobby", "Name"}

class TestFxn(ut.TestCase):
    def test_fxn(self):
        result = 5 * 6
        self.assertEqual(result, b)

    def test_fxn1(self):
        self.assertSetEqual(l1, l2)

if __name__ == "__main__":
    ut.main()
