import unittest
from Automaton import Automaton


class TestAutomaton(unittest.TestCase):
    def setUp(self):
        self.automaton =  Automaton()

    def test_retorna_false_se_nao_definir_os_estados(self):
        self.automaton.set_alphabet(("a"))
        self.assertFalse(self.automaton.add_transition("A","a","B"))

    def test_retorna_false_se_nao_definir_o_alfabeto(self):
        self.automaton.set_states(("A","B"))
        self.assertFalse(self.automaton.add_transition("A","a","B"))

    def test_adiciona_transicao_nao_deterministica(self):
        self.automaton.set_alphabet(("a"))
        self.automaton.set_states(("A","B"))
        self.assertTrue(self.automaton.add_transition("A","a","B"))

    def test_retorna_as_transicoes_corretamente(self):
        expected = {'A':{'a':['B','C']}}

        self.automaton.set_alphabet(("a"))
        self.automaton.set_states(("A","B","C"))
        self.automaton.add_transition("A","a","B")
        self.automaton.add_transition("A","a","C")

        self.assertEqual(self.automaton.transitions, expected)

    def test_retorna_false_se_nao_tem_transicoes(self):
        self.assertFalse(self.automaton.determinizar())

    def test_retorna_transicoes_deterministicas_submetendo_AFND(self):
        expected = {'A':{'a':['B','C']}, 'BC':{'a':['B','C']}}

        self.automaton.set_alphabet(("a"))
        self.automaton.set_states(("A","B","C"))
        self.automaton.add_transition("A","a","B")
        self.automaton.add_transition("A","a","C")
        self.automaton.add_transition("B","a","B")
        self.automaton.add_transition("C","a","C")
        self.automaton.set_initial_state("A")
        self.automaton.set_final_states(("A"))

        self.assertEqual(self.automaton.determinizar(), expected)

    def test_retorna_transicoes_deterministicas_submetendo_AFD(self):
        expected = {'A':{'a':['B']}, 'B':{'a':['B']}, 'C':{'a':['C']}}

        self.automaton.set_alphabet(("a"))
        self.automaton.set_states(("A","B","C"))
        self.automaton.add_transition("A","a","B")
        self.automaton.add_transition("B","a","B")
        self.automaton.add_transition("C","a","C")
        self.automaton.set_initial_state("A")
        self.automaton.set_final_states(("A"))

        self.assertEqual(self.automaton.determinizar(), expected)
