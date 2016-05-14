import unittest
from AutomatoFinito import AutomatoFinito


class TestAutomatoFinito(unittest.TestCase):
    def setUp(self):
        self.automato_finito = AutomatoFinito()

    def test_adiciona_novo_estado(self):
        self.assertTrue(self.automato_finito.adiciona_estado('H'))

    def test_nao_adiciona_estado_ja_adicionado_antes(self):
        self.automato_finito.adiciona_estado('E')
        self.assertFalse(self.automato_finito.adiciona_estado('E'))

    def test_adiciona_dois_estados_diferentes(self):
        self.automato_finito.adiciona_estado('F')
        self.assertTrue(self.automato_finito.adiciona_estado('R'))

    def test_obtem_o_estado_S_do_automato(self):
        self.assertEqual(self.automato_finito.obtem_estado('S'), {'S'})

    def test_obtem_estado_X_do_automato(self):
        self.assertEqual(self.automato_finito.obtem_estado('X'), {'X'})

    def test_define_alfabeto(self):
        self.assertTrue(self.automato_finito.define_alfabeto(('t','b')))

    def test_nao_define_alfabeto_vazio(self):
        self.assertFalse(self.automato_finito.define_alfabeto(()))

    def test_sobreescreve_alfabeto(self):
        self.automato_finito.define_alfabeto(('a', 'b', 'c'))
        self.automato_finito.define_alfabeto(('q', 'w', 'e'))
        self.assertEqual(self.automato_finito.obtem_alfabeto(), ('q', 'w', 'e'))

    def test_obtem_alfabeto(self):
        self.automato_finito.define_alfabeto(('a', 'b', 'c'))
        self.assertEqual(self.automato_finito.obtem_alfabeto(), ('a', 'b', 'c'))

    def test_nao_define_alfabeto_se_tive_pelo_menos_um_estado_adicionado(self):
        self.automato_finito.adiciona_estado('R')
        self.assertFalse(self.automato_finito.define_alfabeto((1,2,3)))

    def test_adiciona_transicao(self):
        self.automato_finito.define_alfabeto(('a'))
        self.automato_finito.adiciona_estado('R')
        self.automato_finito.adiciona_estado('S')
        self.assertTrue(self.automato_finito.adiciona_transicao('R', 'a', 'S'))

    def test_obtem_transicoes(self):
        self.automato_finito.define_alfabeto(('a'))
        self.automato_finito.adiciona_estado('R')
        self.automato_finito.adiciona_estado('S')
        self.automato_finito.adiciona_transicao('R', 'a', 'S')
        self.assertEqual(self.automato_finito.obtem_transicoes(),{'R':{'a':'S'}})

    def test_adiciona_duas_transicoes(self):
        transicoes = {'R':{'a':'S'}, 'S':{'b':'T'}}
        self.automato_finito.define_alfabeto(('a','b'))
        self.automato_finito.adiciona_estado('R')
        self.automato_finito.adiciona_estado('S')
        self.automato_finito.adiciona_estado('T')
        self.automato_finito.adiciona_transicao('R', 'a', 'S')
        self.automato_finito.adiciona_transicao('S', 'b', 'T')
        self.assertEqual(self.automato_finito.obtem_transicoes(), transicoes)

    def test_nao_adiciona_transicao_se_o_terminal_existe_no_alfabeto(self):
        self.assertFalse(self.automato_finito.adiciona_transicao('R','b','S'))

    def test_nao_adiciona_transicao_se_o_primeiro_estado_nao_foi_adicionado(self):
        self.automato_finito.define_alfabeto(('a'))
        self.assertFalse(self.automato_finito.adiciona_transicao('R','a','S'))

    def test_nao_adiciona_transicao_se_o_segundo_estado_nao_foi_adicionado(self):
        self.automato_finito.define_alfabeto(('a'))
        self.automato_finito.adiciona_estado('R')
        self.assertFalse(self.automato_finito.adiciona_transicao('R','a','S'))
