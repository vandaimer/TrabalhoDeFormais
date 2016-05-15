import unittest
from AutomatoFinito import Automaton


class TestAutomatoFinito(unittest.TestCase):
    def setUp(self):
        self.finite_automaton =  Automaton()

    def test_define_conjunto_de_estados(self):
        self.assertTrue(self.finite_automaton.set_states({'S','E','T'}))

    def test_tipo_estrutura_da_estrutura_estados_eh_tupla_se_passar_lista(self):
        self.finite_automaton.set_states(['S','T'])
        self.assertIsInstance(self.finite_automaton.states, tuple)

    def test_tipo_estrutura_da_estrutura_estados_eh_tupla_se_passar_dict(self):
        self.finite_automaton.set_states({'S','T'})
        self.assertIsInstance(self.finite_automaton.states, tuple)

    def test_set_alphabet(self):
        self.assertTrue(self.finite_automaton.set_alphabet(('t','b')))

    def test_nao_set_alphabet_vazio(self):
        self.assertFalse(self.finite_automaton.set_alphabet(()))

    def test_sobreescreve_alfabeto(self):
        self.finite_automaton.set_alphabet(('a', 'b', 'c'))
        self.finite_automaton.set_alphabet(('q', 'w', 'e'))
        self.assertEqual(self.finite_automaton.get_alphabet(), ('q', 'w', 'e'))

    def test_get_alphabet(self):
        self.finite_automaton.set_alphabet(('a', 'b', 'c'))
        self.assertEqual(self.finite_automaton.get_alphabet(), ('a', 'b', 'c'))

    def test_nao_set_alphabet_se_tive_pelo_menos_um_estado_adicionado(self):
        self.finite_automaton.set_states(('R'))
        self.assertFalse(self.finite_automaton.set_alphabet((1,2,3)))

    def test_add_transition(self):
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states(('R','S'))
        self.assertTrue(self.finite_automaton.add_transition('R', 'a', 'S'))

    def test_get_transitions(self):
        transition = {'R':{'a':'S'}}
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states(('R', 'S'))
        self.finite_automaton.add_transition('R', 'a', 'S')
        self.assertEqual(self.finite_automaton.get_transitions(), transition)

    def test_adiciona_duas_transitions(self):
        transitions = {'R':{'a':'S'}, 'S':{'b':'T'}}
        self.finite_automaton.set_alphabet(('a','b'))
        self.finite_automaton.set_states(('R', 'S', 'T'))
        self.finite_automaton.add_transition('R', 'a', 'S')
        self.finite_automaton.add_transition('S', 'b', 'T')
        self.assertEqual(self.finite_automaton.get_transitions(), transitions)

    def test_adiciona_duas_transitions_que_tem_origem_no_mesmo_estado(self):
        transitions = {'S':{'b':'T','c':'Y'}}
        self.finite_automaton.set_alphabet(('c','b'))
        self.finite_automaton.set_states(('S', 'Y', 'T'))
        self.finite_automaton.add_transition('S', 'b', 'T')
        self.finite_automaton.add_transition('S', 'c', 'Y')
        self.assertEqual(self.finite_automaton.get_transitions(), transitions)

    def test_nao_add_transition_se_o_terminal_existe_no_alfabeto(self):
        self.assertFalse(self.finite_automaton.add_transition('R','b','S'))

    def test_nao_add_transition_se_o_primeiro_estado_nao_foi_adicionado(self):
        self.finite_automaton.set_alphabet(('a'))
        self.assertFalse(self.finite_automaton.add_transition('R','a','S'))

    def test_nao_add_transition_se_o_segundo_estado_nao_foi_adicionado(self):
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states('R')
        self.assertFalse(self.finite_automaton.add_transition('R','a','S'))

    def test_nao_add_transition_nao_deterministica(self):
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states(('R','S','T'))
        self.finite_automaton.add_transition('R','a','S')
        self.assertFalse(self.finite_automaton.add_transition('R','a','T'))
