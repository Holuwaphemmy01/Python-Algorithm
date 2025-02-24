from unittest import TestCase

import expense_tracker


class Test(TestCase):
    def test_add_expense(self):
        result = expense_tracker.add_expense(2020, 12, 31, "I buy suliyah", 20, 000000)
        self.assertEqual(result, "Expenses added successfully")
