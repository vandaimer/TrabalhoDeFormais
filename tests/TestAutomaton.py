import unittest
from Automaton import Automaton


class TestAutomaton(unittest.TestCase):
    def setUp(self):
        self.automaton =  Automaton()
        self.automaton2 = Automaton()

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
        expected = {'A':{'a':'BC'}, 'BC':{'a':'BC'}}

        self.automaton.set_alphabet(("a"))
        self.automaton.set_states(("A","B","C"))
        self.automaton.add_transition("A","a","B")
        self.automaton.add_transition("A","a","C")
        self.automaton.add_transition("B","a","B")
        self.automaton.add_transition("C","a","C")
        self.automaton.set_initial_state("A")
        self.automaton.set_final_states(("A"))

        self.assertEqual(self.automaton.determinizar().get_transitions(), expected)

    def test_deterministic_retorna_false_se_nao_tem_alfabeto(self):
        self.assertFalse(self.automaton.is_deterministic())

    def test_deterministic_retorna_false_se_nao_tem_transicoes(self):
        self.automaton.set_alphabet(("a"))
        self.assertFalse(self.automaton.is_deterministic())

    def test_deterministic_retorna_false_se_nao_tem_estados_finais(self):
        self.automaton.set_alphabet("a")
        self.automaton.set_states("A")
        self.automaton.add_transition("A","a","A")
        self.assertFalse(self.automaton.is_deterministic())

    def test_deterministic_retorna_false_se_nao_tem_estado_inicial(self):
        self.automaton.set_alphabet("a")
        self.automaton.set_states("A")
        self.automaton.set_final_states(("A"))
        self.automaton.add_transition("A","a","A")
        self.assertFalse(self.automaton.is_deterministic())

    def test_retorna_false_se_AF_eh_nao_deterministico(self):
        self.automaton.set_alphabet("a")
        self.automaton.set_states(("A","B"))
        self.automaton.set_final_states(("A"))
        self.automaton.set_initial_state("A")
        self.automaton.add_transition("A","a","A")
        self.automaton.add_transition("A","a","B")

        self.assertFalse(self.automaton.is_deterministic())

    def test_retorna_true_se_AF_eh_deterministico(self):
        self.automaton.set_alphabet("a")
        self.automaton.set_states(("A","B"))
        self.automaton.set_final_states(("A"))
        self.automaton.set_initial_state("A")
        self.automaton.add_transition("A","a","A")

        self.assertTrue(self.automaton.is_deterministic())

    def test_retorna_transicoes_deterministicas_submetendo_AFD(self):

        from FiniteAutomaton import FiniteAutomaton
        fa = FiniteAutomaton()
        fa.set_alphabet(("a"))
        fa.set_states(("A","B","C"))
        fa.set_initial_state("A")
        fa.set_final_states(("A"))

        fa.add_transition("A","a","B")
        fa.add_transition("B","a","B")
        fa.add_transition("C","a","C")

        self.automaton.set_alphabet(("a"))
        self.automaton.set_states(("A","B","C"))
        self.automaton.add_transition("A","a","B")
        self.automaton.add_transition("B","a","B")
        self.automaton.add_transition("C","a","C")
        self.automaton.set_initial_state("A")
        self.automaton.set_final_states(("A"))

        self.assertEqual(self.automaton.determinizar().get_transitions(), fa.get_transitions())


    def test_completion(self):
        self.automaton.set_alphabet(("a", "b"))
        self.automaton.set_states(("A", "B", "C"))
        self.automaton.add_transition("A", "a", "B")
        self.automaton.add_transition("B", "b", "B")
        self.automaton.add_transition("C", "a", "C")
        self.automaton.set_initial_state("A")
        self.automaton.set_final_states(("C"))
        self.assertTrue(self.automaton.completion())

    def test_complement(self):
        self.automaton.set_alphabet(("a", "b"))
        self.automaton.set_states(("A", "B", "C"))
        self.automaton.add_transition("A", "a", "B")
        self.automaton.add_transition("B", "b", "C")
        self.automaton.add_transition("C", "a", "C")
        self.automaton.set_initial_state("A")
        self.automaton.set_final_states(("C"))
        # self.assertTrue(self.automaton.complement())

    def test_union(self):
        self.automaton.set_alphabet(("a", "b"))
        self.automaton.set_states(("A", "B", "C"))
        self.automaton.add_transition("A", "a", "B")
        self.automaton.add_transition("B", "b", "C")
        self.automaton.add_transition("C", "a", "C")
        self.automaton.set_initial_state("A")
        self.automaton.set_final_states(("C"))

        self.automaton2.set_alphabet(("a", "b"))
        self.automaton2.set_states(("A", "B", "C"))
        self.automaton2.add_transition("A", "a", "B")
        self.automaton2.add_transition("B", "b", "C")
        self.automaton2.add_transition("C", "a", "C")
        self.automaton2.set_initial_state("A")
        self.automaton2.set_final_states(("C"))

        # self.assertTrue(self.automaton.union(self.automaton2))

    def test_intersection(self):
        self.automaton.set_alphabet(("a", "b"))
        self.automaton.set_states(("A", "B", "C"))
        self.automaton.add_transition("A", "a", "B")
        self.automaton.add_transition("B", "b", "C")
        self.automaton.add_transition("C", "a", "C")
        self.automaton.set_initial_state("A")
        self.automaton.set_final_states(("C"))

        self.automaton2.set_alphabet(("a", "b", "c"))
        self.automaton2.set_states(("A", "B", "C"))
        self.automaton2.add_transition("A", "a", "A")
        self.automaton2.add_transition("A", "a", "B")
        self.automaton2.add_transition("B", "b", "C")
        self.automaton2.add_transition("C", "c", "C")
        self.automaton2.set_initial_state("A")
        self.automaton2.set_final_states(("C"))

        self.assertTrue(self.automaton.intersection(self.automaton2))

    def test_retorna_transicoes_deterministicas_submetendo_AFD_alfabeto_ab(self):
        from FiniteAutomaton import FiniteAutomaton

        fa = FiniteAutomaton()
        fa.set_alphabet(("a","b"))
        fa.set_states(("S","BDF","ACF"))
        fa.set_initial_state("S")
        fa.set_final_states(("BDF","ACF"))

        fa.add_transition("S","a","BDF")
        fa.add_transition("BDF","a","ACF")
        fa.add_transition("ACF","a","BDF")

        fa.add_transition("S","b","ACF")
        fa.add_transition("BDF","b","BDF")
        fa.add_transition("ACF","b","ACF")

        #mock
        self.automaton.set_alphabet(("a","b"))
        self.automaton.set_states(("S","A","B","C","D","F"))

        self.automaton.add_transition("S","a","B")
        self.automaton.add_transition("S","a","D")
        self.automaton.add_transition("S","a","F")
        self.automaton.add_transition("S","b","A")
        self.automaton.add_transition("S","b","C")
        self.automaton.add_transition("S","b","F")


        self.automaton.add_transition("A","a","B")
        self.automaton.add_transition("A","a","F")
        self.automaton.add_transition("A","b","A")


        self.automaton.add_transition("B","a","A")
        self.automaton.add_transition("B","b","B")
        self.automaton.add_transition("B","b","F")


        self.automaton.add_transition("C","a","D")
        self.automaton.add_transition("C","b","C")
        self.automaton.add_transition("C","b","F")


        self.automaton.add_transition("D","a","C")
        self.automaton.add_transition("D","a","F")
        self.automaton.add_transition("D","b","D")

        self.automaton.set_initial_state("S")
        self.automaton.set_final_states(("F"))

        #assert
        self.assertEqual(self.automaton.determinizar().get_transitions(), fa.get_transitions())
