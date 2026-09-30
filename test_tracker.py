import unittest

from validator import is_valid_amount, is_valid_name
from category_manager import get_category


class TestStudentExpenseTracker(unittest.TestCase):

    def test_valid_amount(self):
        self.assertTrue(is_valid_amount("100"))

    def test_invalid_amount(self):
        self.assertFalse(is_valid_amount("abc"))

    def test_valid_name(self):
        self.assertTrue(is_valid_name("Lunch"))

    def test_invalid_name(self):
        self.assertFalse(is_valid_name(""))

    def test_food_category(self):
        self.assertEqual(get_category("lunch"), "Food")


if __name__ == "__main__":
    unittest.main()