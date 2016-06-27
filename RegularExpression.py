import pickle
import string


class RegularExpression:
    def __init__(self):
        self.alphabet = ()
        self.expression = ""
        self.allowedSymbols = list(string.ascii_lowercase + string.digits + '&')  # Sao permitidas letras minusculas, digitos e '&'
        self.operators = ['*', '+', '?', '|', '.', '(', ')']  # Operadores validos

    def valid_expression(self, expression):
        parenthesis = 0
        for c in expression:
            if c not in self.allowedSymbols and c not in self.operators: return False
            if c == '(': parenthesis += 1
            if c == ')': parenthesis -= 1
        if parenthesis != 0: return False
        return True

    def set_expression(self, expression):
        if (self.valid_expression(expression)):
            self.expression = expression
            return True
        else:
            return False

    def save_expression(self, filename):
        if filename != '':
            pickle.dump(self.expression, open(filename, 'wb'))

    def load_expression(self, filename):
        if filename != '':
            self.set_expression(pickle.load(open(filename, 'rb')))