from collections import OrderedDict

class AutomatoFinito:
    def __init__(self):
        self.estados = OrderedDict()
        self.alfabeto = ()
        self.transicoes = OrderedDict()

    def obtem_estado(self, estado):
        return {estado}

    def define_alfabeto(self, alfabeto):
        if len(self.estados) > 0: return False;
        if len(alfabeto) == 0: return False

        self.alfabeto = alfabeto
        return True

    def obtem_alfabeto(self):
        return self.alfabeto

    def adiciona_estado(self, estado):
        if estado in self.estados and len(self.estados) > 0:
            return False
        self.estados[estado] = None
        return True

    def adiciona_transicao(self, estadoA, terminal, estadoB ):
        if estadoA not in self.estados: return False
        if terminal not in self.alfabeto: return False
        if estadoB not in self.estados: return False

        self.transicoes[estadoA] = {terminal:estadoB}
        return True

    def obtem_transicoes(self):
        return self.transicoes
