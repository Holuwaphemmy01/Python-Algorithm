from unittest import TestCase
from Task1.Task1 import task1

class Test(TestCase):
    def test_task1(self):
        self.assertEqual(task1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(task1([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        self.assertEqual(task1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(task1([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        self.assertEqual(task1([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")




