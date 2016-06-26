from AbstractAutomaton import AbstractAutomaton
import copy


class Automaton(AbstractAutomaton):
    def __init__(self):
        super().__init__()

    def add_transition(self, stateA, terminal, stateB):
        if stateA not in self.states: return False
        if terminal not in self.alphabet: return False
        if stateB not in self.states: return False

        if stateA not in self.transitions:
            self.transitions[stateA] = {}
        if terminal not in self.transitions[stateA]:
            self.transitions[stateA][terminal] = []

        self.transitions[stateA][terminal].append(stateB)

        return True

    def determinizar(self):
        if not self.is_deterministic():
            if len(self.transitions) == 0: return False
            transitions = {}
            transitions[self.initial_state] = self.transitions[self.initial_state]
            transitions_to_modify = transitions.copy()
            for state,list_transitions in transitions.items():
                for simbol in self.alphabet:
                    list_union_states = set()
                    for state in list_transitions[simbol]:
                        if self.transitions.get(state) != None:
                            list_union_states = list_union_states.union(self.transitions.get(state)[simbol])
                    newState = ''.join(list_transitions[simbol])
                    transitions_to_modify[newState] = {}
                    transitions_to_modify[newState][simbol] = sorted(list(list_union_states))
            return transitions_to_modify
        return self.transitions

    def is_deterministic(self):
        if len(self.alphabet) == 0: return False
        if len(self.transitions) == 0: return False
        if len(self.final_states) == 0: return False
        if self.initial_state == None: return False

        for transition in self.transitions.values():
            for simbol in self.alphabet:
                if len(transition[simbol]) > 1:
                    return False
        return True

    def completion(self):
        self.add_state("Z")
        for state in self.states:
            for terminal in self.alphabet:
                if terminal not in self.transitions[state]:
                    self.add_transition(state, terminal, ''.join("Z"))
        return True

    def complement(self):
        copia = copy.deepcopy(self)
        # if not copia.is_deterministic():
            # copia.determinizar()
        copia.completion()

        non_final = list()
        for state in copia.states:
            if state not in copia.final_states:
                non_final.append(state)

        copia.set_final_states(tuple(non_final))
        return copia
        # return True

    def union(self, automaton):
        uniao = Automaton()

        u_alphabet = list()
        for character in self.get_alphabet():
            if character not in u_alphabet:
                u_alphabet.append(character)
        for character in automaton.get_alphabet():
            if character not in u_alphabet:
                u_alphabet.append(character)
        u_alphabet.append("&")
        uniao.set_alphabet(tuple(u_alphabet))

        u_states = list()
        u_final_states = list()
        u_states.append("S")
        uniao.set_states(tuple(u_states))
        uniao.set_initial_state("S")
        sufixo = "1"

        for state in self.states:
            origem = state
            origemRenomeado = origem + sufixo
            if origemRenomeado not in u_states:
                u_states.append(origemRenomeado)
                uniao.set_states(tuple(u_states))
            if self.get_initial_state() == origem:
                uniao.add_transition("S", "&", origemRenomeado)
            if origem in self.get_final_states():
                if origemRenomeado not in u_final_states:
                    u_final_states.append(origemRenomeado)
                    uniao.set_final_states(tuple(u_final_states))

            for terminal in self.transitions[state]:
                for des in self.transitions[state][terminal]:
                    destino = des
                    destinoRenomeado = destino + sufixo
                    if destinoRenomeado not in u_states:
                        u_states.append(destinoRenomeado)
                        uniao.set_states(tuple(u_states))
                    if des in self.get_final_states():
                        if des not in u_final_states:
                            u_final_states.append(des)
                            uniao.set_states(tuple(u_states))
                    uniao.add_transition(origemRenomeado, terminal, destinoRenomeado)

        sufixo = "2"
        for state in automaton.states:
            origem = state
            origemRenomeado = origem + sufixo
            if origemRenomeado not in u_states:
                u_states.append(origemRenomeado)
                uniao.set_states(tuple(u_states))
                if automaton.get_initial_state() == origem:
                    uniao.add_transition("S", "&", origemRenomeado)
                if origem in automaton.get_final_states():
                    if origemRenomeado not in u_final_states:
                        u_final_states.append(origemRenomeado)
                        uniao.set_final_states(tuple(u_final_states))

            for terminal in automaton.transitions[state]:
                for des in automaton.transitions[state][terminal]:
                    destino = des
                    destinoRenomeado = destino + sufixo
                    if destinoRenomeado not in u_states:
                        u_states.append(destinoRenomeado)
                        uniao.set_states(tuple(u_states))
                    if des in self.get_final_states():
                        if des not in u_final_states:
                            u_final_states.append(des)
                            uniao.set_final_states(tuple(u_final_states))

                    uniao.add_transition(origemRenomeado, terminal, destinoRenomeado)
        return uniao
        # return True

    def intersection(self, automaton):
        copia_this = copy.deepcopy(self)
        copia_automato = copy.deepcopy(automaton)
        intersect = Automaton()

        i_alphabet = list()
        for character in self.get_alphabet():
            if character not in i_alphabet:
                i_alphabet.append(character)
        for character in automaton.get_alphabet():
            if character not in i_alphabet:
                i_alphabet.append(character)
        intersect.set_alphabet(tuple(i_alphabet))
        copia_this.set_alphabet(i_alphabet)
        copia_automato.set_alphabet(i_alphabet)

        this_complement = copia_this.complement()
        automato_complement = copia_automato.complement()
        complement_union = this_complement.union(automato_complement)
        intersect = complement_union.complement()

        for state in intersect.states:
            print("Origem: " + state)
            for terminal in intersect.transitions[state]:
                print("Terminal: " + terminal)
                for des in intersect.transitions[state][terminal]:
                    print("Destino: " + des)

        # return intersect
        return True