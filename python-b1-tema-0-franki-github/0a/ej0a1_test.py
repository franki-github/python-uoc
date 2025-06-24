import unittest
from ej0a1 import check_age

class TestCheckAge(unittest.TestCase):
    def test_check_age(self):
        self.assertEqual(check_age(15), False, "Should be False for age 15")
        self.assertEqual(check_age(16), False, "Should be False for age 16")
        self.assertEqual(check_age(17), False, "Should be False for age 17")
        self.assertEqual(check_age(18), True, "Should be True for age 18")
        self.assertEqual(check_age(20), True, "Should be True for age 20")