import unittest
from unittest import TestCase

import self

import expense


class Test(unittest.TestCase):
    def test_to_throw_exception_when_date_is_not_correct(self):
        with self.assertRaises(ValueError):  # Correct use of assertRaises
            expense.add_expense("2022-34-22", "adelakun", "1234")


    def test_to_throw_exception_when_date_is_empty(self):
        with self.assertRaises(ValueError): expense.add_expense("", "adelakun", "1234")


    def test_to_throw_exception_when_description_is_empty(self):
        with self.assertRaises(ValueError): expense.add_expense("2022-12-14", " ", "1234")

    def test_to_throw_exception_when_amount_is_alphabet(self):
        with self.assertRaises(ValueError): expense.add_expense("2022-12-14", "AAdelal", "adbsbs")

    def test_to_throw_exception_when_amount_is_negative(self):
        with self.assertRaises(ValueError): expense.add_expense("2022-12-14", "tatat", "-1234")

