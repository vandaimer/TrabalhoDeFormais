import unittest
from FiniteAutomaton import FiniteAutomaton


class TestFiniteAutomaton(unittest.TestCase):
    def setUp(self):
        self.finite_automaton =  FiniteAutomaton()

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

    def test_est_alcancaveis_retorna_false_se_nao_tem_transicoes(self):
        self.assertFalse(self.finite_automaton._achievable_states())

    def test_est_alcancaveis_retorna_false_se_tem_transicoes_mas_nao_tem_sem_estado_inicial(self):
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states(('q0'))
        self.finite_automaton.set_final_states(('q0'))
        self.finite_automaton.add_transition('q0','a','q0')
        self.assertFalse(self.finite_automaton._achievable_states())

    def test_est_alcancaveis_retorna_false_se_tem_transicoes_mas_nao_tem_estados_finais(self):
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states(('q0'))
        self.finite_automaton.set_initial_state('q0')
        self.finite_automaton.add_transition('q0','a','q0')
        self.assertFalse(self.finite_automaton._achievable_states())

    def test_est_alcacaveis_retorna_est_alcacaveis_tento_uma_transicao(self):
        expected = {'q0'}
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states(('q0'))
        self.finite_automaton.set_initial_state('q0')
        self.finite_automaton.set_final_states(('q0'))
        self.finite_automaton.add_transition('q0','a','q0')
        self.assertEqual(self.finite_automaton._achievable_states(), expected)

    def test_est_alcacaveis_retorna_est_alcancaveis_tento_duas_transicao(self):
        expected = {'q0','q1'}
        self.finite_automaton.set_alphabet(('a','b'))
        self.finite_automaton.set_states(('q0','q1'))
        self.finite_automaton.set_initial_state('q0')
        self.finite_automaton.set_final_states(('q0'))
        self.finite_automaton.add_transition('q0','a','q1')
        self.finite_automaton.add_transition('q0','b','q0')
        self.finite_automaton.add_transition('q1','a','q1')
        self.finite_automaton.add_transition('q1','b','q0')
        self.assertEqual(self.finite_automaton._achievable_states(), expected)

    def test_est_vivos_retorna_false_se_nao_tem_trasicoes(self):
        self.assertFalse(self.finite_automaton._live_states())

    def test_est_vivos_retorna_true_se_tem_uma_transicao_ao_menos(self):
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states(('q0'))
        self.finite_automaton.set_initial_state('q0')
        self.finite_automaton.set_final_states(('q0'))
        self.finite_automaton.add_transition('q0','a','q0')
        self.assertTrue(self.finite_automaton._live_states(achievable_states=('q0',)))

    def test_est_vivos_retorna_false_se_tem_transicoes_mas_nao_tem_estados_finais(self):
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states(('q0'))
        self.finite_automaton.set_initial_state('q0')
        self.finite_automaton.add_transition('q0','a','q0')
        self.assertFalse(self.finite_automaton._live_states(achievable_states=('q0',)))

    def test_est_vivos_retorna_false_se_tem_transicoes_mas_nao_tem_sem_estado_inicial(self):
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states(('q0'))
        self.finite_automaton.set_final_states(('q0'))
        self.finite_automaton.add_transition('q0','a','q0')
        self.assertFalse(self.finite_automaton._live_states(achievable_states=('q0',)))

    def test_est_vivos_retorna_um_estado_vivo_corretamente(self):
        expected = {'q0'}
        self.finite_automaton.set_alphabet(('a'))
        self.finite_automaton.set_states(('q0'))
        self.finite_automaton.set_initial_state('q0')
        self.finite_automaton.set_final_states(('q0'))
        self.finite_automaton.add_transition('q0','a','q0')
        self.assertEqual(self.finite_automaton._live_states(achievable_states=('q0',)), expected)

    def test_est_vivos_retorna_tre_estados_vivos_corretamente(self):
        expected = {'q0', 'q1', 'q2'}
        achievable_states = ('q0','q1','q2','q3')

        self.finite_automaton.set_alphabet(('a','b'))
        self.finite_automaton.set_states(('q0','q1','q2','q3','q4','q5'))
        self.finite_automaton.set_initial_state('q0')
        self.finite_automaton.set_final_states(('q1','q4'))

        self.finite_automaton.add_transition('q0','a','q2')
        self.finite_automaton.add_transition('q0','b','q3')
        self.finite_automaton.add_transition('q1','a','q1')
        self.finite_automaton.add_transition('q1','b','q2')
        self.finite_automaton.add_transition('q2','a','q1')
        self.finite_automaton.add_transition('q2','b','q1')
        self.finite_automaton.add_transition('q3','a','q4')
        self.finite_automaton.add_transition('q3','b','q3')

        self.assertEqual(self.finite_automaton._live_states(achievable_states=achievable_states), expected)

    def test_est_alcancaveis_retorna_seis_estados_vivos_corretamente(self):
        expected = {'A', 'B', 'C', 'E', 'F', 'G'}

        self.finite_automaton.set_alphabet(('a','b'))
        self.finite_automaton.set_states(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'))
        self.finite_automaton.set_initial_state('A')
        self.finite_automaton.set_final_states(('A','D','G'))

        self.finite_automaton.add_transition('A', 'a', 'G')
        self.finite_automaton.add_transition('A', 'b', 'B')
        self.finite_automaton.add_transition('B', 'a', 'F')
        self.finite_automaton.add_transition('B', 'b', 'E')
        self.finite_automaton.add_transition('C', 'a', 'C')
        self.finite_automaton.add_transition('C', 'b', 'G')
        self.finite_automaton.add_transition('D', 'a', 'A')
        self.finite_automaton.add_transition('D', 'b', 'H')
        self.finite_automaton.add_transition('E', 'a', 'E')
        self.finite_automaton.add_transition('E', 'b', 'A')
        self.finite_automaton.add_transition('F', 'a', 'B')
        self.finite_automaton.add_transition('F', 'b', 'C')
        self.finite_automaton.add_transition('G', 'a', 'G')
        self.finite_automaton.add_transition('G', 'b', 'F')
        self.finite_automaton.add_transition('H', 'a', 'H')
        self.finite_automaton.add_transition('H', 'b', 'D')

        self.assertEqual(self.finite_automaton._achievable_states(), expected)

    def test_est_vivos_retorna_seis_estados_vivos_corretamente(self):
        expected = {'A', 'B', 'C', 'E', 'F', 'G'}

        self.finite_automaton.set_alphabet(('a','b'))
        self.finite_automaton.set_states(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'))
        self.finite_automaton.set_initial_state('A')
        self.finite_automaton.set_final_states(('A','D','G'))

        self.finite_automaton.add_transition('A', 'a', 'G')
        self.finite_automaton.add_transition('A', 'b', 'B')
        self.finite_automaton.add_transition('B', 'a', 'F')
        self.finite_automaton.add_transition('B', 'b', 'E')
        self.finite_automaton.add_transition('C', 'a', 'C')
        self.finite_automaton.add_transition('C', 'b', 'G')
        self.finite_automaton.add_transition('D', 'a', 'A')
        self.finite_automaton.add_transition('D', 'b', 'H')
        self.finite_automaton.add_transition('E', 'a', 'E')
        self.finite_automaton.add_transition('E', 'b', 'A')
        self.finite_automaton.add_transition('F', 'a', 'B')
        self.finite_automaton.add_transition('F', 'b', 'C')
        self.finite_automaton.add_transition('G', 'a', 'G')
        self.finite_automaton.add_transition('G', 'b', 'F')
        self.finite_automaton.add_transition('H', 'a', 'H')
        self.finite_automaton.add_transition('H', 'b', 'D')

        achievable = self.finite_automaton._achievable_states()
        self.assertEqual(self.finite_automaton._live_states(achievable), expected)

    def test_minimiza_retorna_false_se_nao_passar_estados_vivos(self):
        self.assertFalse(self.finite_automaton.minimize())

    def test_minimiza_retorna_false_se_passar_estados_vivos_igual_none(self):
        self.assertFalse(self.finite_automaton.minimize(None))

    def test_minimiza_retorna_false_se_nao_tem_estados_finais_definido(self):
        live_states = {'A'}
        self.assertFalse(self.finite_automaton.minimize(live_states))

    def test_minimiza_retorna_false_se_nao_tem_transicoes(self):
        self.finite_automaton.set_states(('A'))
        self.finite_automaton.set_final_states(('A'))
        live_states = {'A'}
        self.assertFalse(self.finite_automaton.minimize(live_states))

    def test_minimiza_retorna_live_state(self):
        self.finite_automaton.set_alphabet(('a','b'))
        self.finite_automaton.set_states(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'))
        self.finite_automaton.set_initial_state('A')
        self.finite_automaton.set_final_states(('A','D','G'))

        self.finite_automaton.add_transition('A', 'a', 'G')
        self.finite_automaton.add_transition('A', 'b', 'B')

        self.finite_automaton.add_transition('B', 'a', 'F')
        self.finite_automaton.add_transition('B', 'b', 'E')
        self.finite_automaton.add_transition('C', 'a', 'C')
        self.finite_automaton.add_transition('C', 'b', 'G')
        self.finite_automaton.add_transition('D', 'a', 'A')
        self.finite_automaton.add_transition('D', 'b', 'H')
        self.finite_automaton.add_transition('E', 'a', 'E')
        self.finite_automaton.add_transition('E', 'b', 'A')
        self.finite_automaton.add_transition('F', 'a', 'B')
        self.finite_automaton.add_transition('F', 'b', 'C')

        self.finite_automaton.add_transition('G', 'a', 'G')
        self.finite_automaton.add_transition('G', 'b', 'F')

        self.finite_automaton.add_transition('H', 'a', 'H')
        self.finite_automaton.add_transition('H', 'b', 'D')

        achievable = self.finite_automaton._achievable_states()
        live_states = self.finite_automaton._live_states(achievable)

        self.assertEqual(self.finite_automaton.minimize(live_states), [['A', 'G'], ['B', 'F'], ['C', 'E']] )

    # def test_minimiza_retorna_classe_correta_se_1_estado_vivo(self):
    #     expected = {'A':1}
    #     live_states = {'A'}
    #     self.assertEqual(self.finite_automaton.minimize(live_states), expected)
