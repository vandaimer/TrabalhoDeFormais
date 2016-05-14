import unittest
from AutomatoFinito import AutomatoFinito


class TestAutomatoFinito(unittest.TestCase):
    def setUp(self):
        self.automato_finito = AutomatoFinito()

    def test_define_conjunto_de_estados(self):
        self.assertTrue(self.automato_finito.define_estados({'S','E','T'}))

    def test_tipo_estrutura_do_conjunto_de_estados_eh_tupla_se_passar_lista(self):
        self.automato_finito.define_estados(['S','T'])
        self.assertIsInstance(self.automato_finito.estados, tuple)

    def test_tipo_estrutura_do_conjunto_de_estados_eh_tupla_se_passar_dict(self):
        self.automato_finito.define_estados({'S','T'})
        self.assertIsInstance(self.automato_finito.estados, tuple)

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
        self.automato_finito.define_estados(('R'))
        self.assertFalse(self.automato_finito.define_alfabeto((1,2,3)))

    def test_adiciona_transicao(self):
        self.automato_finito.define_alfabeto(('a'))
        self.automato_finito.define_estados(('R','S'))
        self.assertTrue(self.automato_finito.adiciona_transicao('R', 'a', 'S'))

    def test_obtem_transicoes(self):
        transicao = {'R':{'a':'S'}}
        self.automato_finito.define_alfabeto(('a'))
        self.automato_finito.define_estados(('R', 'S'))
        self.automato_finito.adiciona_transicao('R', 'a', 'S')
        self.assertEqual(self.automato_finito.obtem_transicoes(), transicao)

    def test_adiciona_duas_transicoes(self):
        transicoes = {'R':{'a':'S'}, 'S':{'b':'T'}}
        self.automato_finito.define_alfabeto(('a','b'))
        self.automato_finito.define_estados(('R', 'S', 'T'))
        self.automato_finito.adiciona_transicao('R', 'a', 'S')
        self.automato_finito.adiciona_transicao('S', 'b', 'T')
        self.assertEqual(self.automato_finito.obtem_transicoes(), transicoes)

    def test_adiciona_duas_transicoes_que_tem_origem_no_mesmo_estado(self):
        transicoes = {'S':{'b':'T','c':'Y'}}
        self.automato_finito.define_alfabeto(('c','b'))
        self.automato_finito.define_estados(('S', 'Y', 'T'))
        self.automato_finito.adiciona_transicao('S', 'b', 'T')
        self.automato_finito.adiciona_transicao('S', 'c', 'Y')
        self.assertEqual(self.automato_finito.obtem_transicoes(), transicoes)

    def test_nao_adiciona_transicao_se_o_terminal_existe_no_alfabeto(self):
        self.assertFalse(self.automato_finito.adiciona_transicao('R','b','S'))

    def test_nao_adiciona_transicao_se_o_primeiro_estado_nao_foi_adicionado(self):
        self.automato_finito.define_alfabeto(('a'))
        self.assertFalse(self.automato_finito.adiciona_transicao('R','a','S'))

    def test_nao_adiciona_transicao_se_o_segundo_estado_nao_foi_adicionado(self):
        self.automato_finito.define_alfabeto(('a'))
        self.automato_finito.define_estados('R')
        self.assertFalse(self.automato_finito.adiciona_transicao('R','a','S'))
