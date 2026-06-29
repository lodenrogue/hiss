import unittest
from evaluate import Evaluator

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.evaluate = Evaluator().evaluate

    def test_simple_function(self):
        self.evaluate("(defun add10 (a) (+ a 10))")
        self.assertEqual(self.evaluate("(add10 5)"), 15)

    def test_global_vars_function(self):
        self.evaluate("(defun add20 (a) (+ a 20))")
        self.evaluate("(defvar x 10)")
        self.assertEqual(self.evaluate("(add20 x)"), 30)

if __name__ == "__main__":
    unittest.main()
