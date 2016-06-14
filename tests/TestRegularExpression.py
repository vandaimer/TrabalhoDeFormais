import unittest
from RegularExpression import RegularExpression


class TestRegularExpression(unittest.TestCase):
    def setUp(self):
        self.regular_expression = RegularExpression()

    def test_save_and_load_expression(self):
        self.regular_expression.set_expression("a*(b?c|d)*")
        self.regular_expression.save_expression("expressao_teste.p")
        self.regular_expression.load_expression("expressao_teste.p")
        self.assertEqual(self.regular_expression.expression, "a*(b?c|d)*")
