

class AutomatoFinito:
    def __init__(self):
        self.estados = ()
        self.alfabeto = ()
        self.transicoes = {}

    def define_alfabeto(self, alfabeto):
        if len(self.estados) > 0: return False;
        if len(alfabeto) == 0: return False

        self.alfabeto = alfabeto
        return True

    def obtem_alfabeto(self):
        return self.alfabeto

    def define_estados(self, estados):
        self.estados = tuple(estados)
        return True

    def adiciona_transicao(self, estadoA, terminal, estadoB ):
        if estadoA not in self.estados: return False
        if terminal not in self.alfabeto: return False
        if estadoB not in self.estados: return False

        if estadoA not in self.transicoes:
            self.transicoes[estadoA] = {}
        if terminal in self.transicoes[estadoA]:
            return False
        self.transicoes[estadoA][terminal] = estadoB
        return True

    def obtem_transicoes(self):
        return self.transicoes
