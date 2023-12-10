import unittest
import os
import sys

sys.path.append(os.getcwd())
from main import refine_price


class TestNormalizer(unittest.TestCase):

    def test_normalizer(self):
        self.assertEqual(refine_price("$123,456,789"), "123456789")
        self.assertEqual(refine_price("$4"), "4")
        self.assertEqual(refine_price("4"), "4")
        self.assertEqual(refine_price("44.45"), "44.45")
        self.assertEqual(refine_price("$44"), "44")
        self.assertEqual(refine_price("4,567.66"), "4567.66")
        self.assertEqual(refine_price("$15.3"), "15.3")
        self.assertEqual(refine_price("$0.587"), "0.587")
        self.assertEqual(refine_price("0.5"), "0.5")


if __name__ == '__main__':
    unittest.main()
