import unittest
from fizzbuzz import Fizzbuzz


class fizzbuzzTest(unittest.TestCase):

    def test_non_list_inputs(self):
        self.assertEqual(Fizzbuzz(5, 8), "Invalid input")

    def test_non_list_input(self):
        self.assertEqual(Fizzbuzz([2, 3, 4], 7), "Invalid input")

    def test_fizz(self):
        self.assertEqual(Fizzbuzz([1, 3, 4], ['a', 'b', 'c']), "fizz")

    def test_buzz(self):
        self.assertEqual(Fizzbuzz([4, 5, 4], [3, 4]), "buzz")

    def test_fizz_buzz(self):
        self.assertEqual(Fizzbuzz([1, 2, 3, 3, 4, 5, 5, 5, 5, 6],
                                  [7, 7, 4, 5, 9]), "Fizzbuzz")

    def test_other_total(self):
        self.assertEqual(Fizzbuzz([4, 5, 6], [3]), 4)

    def test_both_empty(self):
        self.assertEqual(Fizzbuzz([1, 3, 5], []), "fizz")

if __name__ == '__main__':
    unittest().run()