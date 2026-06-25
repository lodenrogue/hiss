import unittest
from evaluate import evaluate, variables

class TestLogicalOperators(unittest.TestCase):

    def tearDown(self):
        variables.clear()

    def test_greater_than(self):
        self.assertEqual(evaluate("(> 2 1)"), True)
        self.assertEqual(evaluate("(> 1 2)"), False)
        self.assertEqual(evaluate("(> 2 2)"), False)

    def test_greater_than_one_variable(self):
        evaluate("(defvar x 10)")
        self.assertEqual(evaluate("(> x 1)"), True)
        self.assertEqual(evaluate("(> 1 x)"), False)

    def test_greater_than_two_variables(self):
        evaluate("(defvar x 10)") 
        evaluate("(defvar y 20)")
        self.assertEqual(evaluate("(> x y)"), False)
        self.assertEqual(evaluate("(> y x)"), True)

    def test_less_than(self):
        self.assertEqual(evaluate("(< 1 2)"), True)
        self.assertEqual(evaluate("(< 2 1)"), False)
        self.assertEqual(evaluate("(< 2 2)"), False)

    def test_less_than_variables(self):
        evaluate("(defvar x -5)")
        evaluate("(defvar y 0)")
        evaluate("(defvar z 5)")
        self.assertEqual(evaluate("(< x y)"), True)
        self.assertEqual(evaluate("(< z y)"), False)
        self.assertEqual(evaluate("(< x x)"), False)

    def test_greater_than_or_equal(self):
        self.assertEqual(evaluate("(>= 2 1)"), True)
        self.assertEqual(evaluate("(>= 2 2)"), True)
        self.assertEqual(evaluate("(>= 1 2)"), False)
        self.assertEqual(evaluate("(>= 0 -1)"), True)
        self.assertEqual(evaluate("(>= -1 0)"), False)
        self.assertEqual(evaluate("(>= -1 -1)"), True)

    def test_greater_than_or_equal_variables(self):
        evaluate("(defvar x 10)")
        evaluate("(defvar y 10)")
        evaluate("(defvar z 5)")
        self.assertEqual(evaluate("(>= x y)"), True)
        self.assertEqual(evaluate("(>= x z)"), True)
        self.assertEqual(evaluate("(>= z x)"), False)

    def test_less_than_or_equal(self):
        self.assertEqual(evaluate("(<= 1 2)"), True)
        self.assertEqual(evaluate("(<= 2 2)"), True)
        self.assertEqual(evaluate("(<= 2 1)"), False)
        self.assertEqual(evaluate("(<= -2 -1)"), True)
        self.assertEqual(evaluate("(<= -1 -2)"), False)
        self.assertEqual(evaluate("(<= 0 0)"), True)

    def test_less_than_or_equal_variables(self):
        evaluate("(defvar x 20)")
        evaluate("(defvar y 20)")
        evaluate("(defvar z 30)")
        self.assertEqual(evaluate("(<= x y)"), True)
        self.assertEqual(evaluate("(<= x z)"), True)
        self.assertEqual(evaluate("(<= z x)"), False)

    def test_equal(self):
        self.assertEqual(evaluate("(eq 1 1)"), True)
        self.assertEqual(evaluate("(eq 1 2)"), False)
        self.assertEqual(evaluate("(eq -1 -1)"), True)
        self.assertEqual(evaluate("(eq 0 0)"), True)
        self.assertEqual(evaluate("(eq 0 1)"), False)

    def test_equal_variables(self):
        evaluate("(defvar x 100)")
        evaluate("(defvar y 100)")
        evaluate("(defvar z 200)")
        self.assertEqual(evaluate("(eq x y)"), True)
        self.assertEqual(evaluate("(eq x z)"), False)
        self.assertEqual(evaluate("(eq z z)"), True)

    def test_nested_expressions(self):
        evaluate("(defvar x 5)")
        evaluate("(defvar y 10)")
        self.assertEqual(evaluate("(eq (< x y) (> y x))"), True)
        self.assertEqual(evaluate("(eq (<= x y) (>= x y))"), False)
        
if __name__ == "__main__":
    unittest.main()
