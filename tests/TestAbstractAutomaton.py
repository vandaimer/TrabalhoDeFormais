import unittest
from AbstractAutomaton import AbstractAutomaton


class TestAbstractAutomaton(unittest.TestCase):
    def setUp(self):
        self.finite_automaton =  AbstractAutomaton()

    def test_adiciona_um_novo_estado(self):
        self.assertTrue(self.finite_automaton.add_state("A"))

    def test_adiciona_varios_e_depois_um(self):
        expected = ("q0","q1","q2")
        self.finite_automaton.set_states(("q0","q1"))
        self.finite_automaton.add_state("q2")

        self.assertEqual(self.finite_automaton.states, expected)

    def test_se_retorna_o_estado_adicionado(self):
        expected = ("q0",)
        self.finite_automaton.add_state("q0")

        self.assertEqual(self.finite_automaton.states, expected)

    def test_adiciona_um_depois_varios(self):
        expected = ("q0","q1","q2")
        self.finite_automaton.add_state("q2")
        self.finite_automaton.set_states(("q0","q1"))

        self.assertEqual(self.finite_automaton.states, expected)
    def test_define_conjunto_de_estados(self):
        self.assertTrue(self.finite_automaton.set_states({'S','E','T'}))

    def test_tipo_estrutura_da_estrutura_estados_eh_tupla_se_passar_lista(self):
        self.finite_automaton.set_states(['S','T'])
        self.assertIsInstance(self.finite_automaton.states, tuple)

    def test_tipo_estrutura_da_estrutura_estados_eh_tuple_se_passar_dict(self):
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

    def test_get_transitions(self):
        try:
            self.finite_automaton.add_transition('R', 'a', 'S')
        except NotImplementedError as e:
            self.assertEqual(self.finite_automaton.get_transitions(), {})

    def test_define_estado_inicial(self):
        self.finite_automaton.set_states(('S'))
        self.assertTrue(self.finite_automaton.set_initial_state('S'))

    def test_define_estado_inicial_se_o_estad_jah_foi_definido(self):
        self.finite_automaton.set_states(('R','S','T'))
        self.assertFalse(self.finite_automaton.set_initial_state('H'))

    def test_verifica_se_estado_inicial_foi_definido(self):
        self.finite_automaton.set_states(('Q0'))
        self.assertTrue(self.finite_automaton.set_initial_state('Q0'))

    def test_nao_define_estado_inicial_foi_definido(self):
        self.assertFalse(self.finite_automaton.set_initial_state('q0'))

    def test_nao_define_estado_inicial_se_o_estado_nao_foi_definido(self):
        self.assertFalse(self.finite_automaton.set_initial_state('J'))

    def test_obtem_estado_inicial(self):
        self.finite_automaton.set_states(('S'))
        self.finite_automaton.set_initial_state(('S'))
        self.assertEqual(self.finite_automaton.get_initial_state(), ('S'))

    def test_define_estados_finais(self):
        self.finite_automaton.set_states(('S', 'T'))
        self.assertTrue(self.finite_automaton.set_final_states(('S','T')))

    def test_define_apenas_um_estado_final_com_dois_caracteres(self):
        self.finite_automaton.set_states(('q0'))
        self.assertTrue(self.finite_automaton.set_final_states(('q0')))

    def test_define_apenas_um_estado_final_com_um_caractere(self):
        self.finite_automaton.set_states(('S'))
        self.assertTrue(self.finite_automaton.set_final_states(('S')))

    def test_nao_define_estado_final_se_ele_nao_foi_definido_antes(self):
        self.assertFalse(self.finite_automaton.set_final_states(('S','B')))

    def test_verifica_se_foi_adicionado_os_estados_finais(self):
        self.finite_automaton.set_states(('S','H'))
        self.finite_automaton.set_final_states(('S','H'))
        self.assertEqual(self.finite_automaton.get_final_states(), ('S','H'))

    def test_verifica_se_foi_sobreescrito_os_estados_finais(self):
        self.finite_automaton.set_states(('X','T'))
        self.finite_automaton.set_states(('XX','TT'))
        self.finite_automaton.set_final_states(('X','T'))
        self.finite_automaton.set_final_states(('XX','TT'))
        self.assertEqual(self.finite_automaton.get_final_states(), ('XX','TT'))
