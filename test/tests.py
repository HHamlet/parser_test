import unittest
import os
import sys

sys.path.append(os.getcwd())
from main import normalizer


class TestNormalizer(unittest.TestCase):

    def test_normalizer(self):
        self.assertEqual(normalizer("$123,456,789"), "123456789")
        self.assertEqual(normalizer("$47,148.66"), "47148.66")



