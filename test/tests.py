import unittest
import os
import sys

sys.path.append(os.getcwd())
from main import normalizer


class TestNormalizer(unittest.TestCase):

    def test_normalizer(self):
        self.assertEqual(normalizer("$123,456,789"), "123456789")
        self.assertEqual(normalizer("$4"), "4")
        self.assertEqual(normalizer("4"), "4")
        self.assertEqual(normalizer("44.45"), "44.45")
        self.assertEqual(normalizer("$44"), "44")
        self.assertEqual(normalizer("4,567.66"), "4567.66")
        self.assertEqual(normalizer("$15.3"), "15.3")
        self.assertEqual(normalizer("$0.587"), "0.587")
        self.assertEqual(normalizer("0.5"), "0.5")



