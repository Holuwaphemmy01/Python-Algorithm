from unittest import TestCase
from task3.task3 import duplicate_count


class Test(TestCase):
    def test_text(self):
        # self.assertEqual(duplicate_count(""), 0)
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("abcdeaa"), 1)
        # self.assertEqual(duplicate_count("abcdeaB"), 2)
        # self.assertEqual(duplicate_count("Indivisibilities"), 2)
