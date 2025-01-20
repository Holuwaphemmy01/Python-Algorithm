from unittest import TestCase
from src.task2 import task2


class Test(TestCase):
    def test_descending(self):
        self.assertEqual(task2.descending(123456789), 987654321)
        self.assertEqual(task2.descending(15), 51)
        self.assertEqual(task2.descending(0), 0)