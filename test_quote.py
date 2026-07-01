import unittest
from evaluate import Evaluator

class TestQuote(unittest.TestCase):

    def setUp(self):
        self.evaluate = Evaluator().evaluate

    def test_symbol(self):
        self.assertEqual(self.evaluate("(quote test)"), "test")

    def test_list(self):
        self.assertEqual(self.evaluate("(quote (test 123))"), ["test", 123])


if __name__ == "__main__":
    unittest.main()
