

class Automaton:
    def __init__(self):
        self.states = ()
        self.alphabet = ()
        self.transitions = {}

    def set_alphabet(self, alphabet):
        if len(self.states) > 0: return False;
        if len(alphabet) == 0: return False

        self.alphabet = alphabet
        return True

    def get_alphabet(self):
        return self.alphabet

    def set_states(self, states):
        self.states = tuple(states)
        return True

    def add_transition(self, stateA, terminal, stateB ):
        if stateA not in self.states: return False
        if terminal not in self.alphabet: return False
        if stateB not in self.states: return False

        if stateA not in self.transitions:
            self.transitions[stateA] = {}
        if terminal in self.transitions[stateA]:
            return False
        self.transitions[stateA][terminal] = stateB
        return True

    def get_transitions(self):
        return self.transitions
