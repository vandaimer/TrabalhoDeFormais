

class AbstractAutomaton:
    def __init__(self):
        self.states = ()
        self.alphabet = ()
        self.transitions = {}
        self.final_states = ()
        self.initial_state = None

    def set_alphabet(self, alphabet):
        if len(self.states) > 0: return False;
        if len(alphabet) == 0: return False

        self.alphabet = alphabet
        return True

    def get_alphabet(self):
        return self.alphabet

    def add_state(self, state):
        if len(self.states) > 0:
            states = list(self.states)
            states.append(state)
            self.states = tuple(states)
            self.transitions[state] = {}
        else:
            self.states = (state,)
        return True

    def set_states(self, states):
        if not isinstance(states, tuple):
            self.states = (states,)
        else:
            self.states = (states)
        return True

    def add_transition(self, stateA, terminal, stateB ):
        raise NotImplementedError

    def get_transitions(self):
        return self.transitions

    def set_initial_state(self, state):
        if state not in self.states: return False
        self.initial_state = state
        return True

    def set_final_states(self, states):
        if not isinstance(states, tuple):
            states = (states,)

        for state in states:
            if state not in self.states:
                return False
        self.final_states = states
        return True

    def get_final_states(self):
        return self.final_states

    def get_initial_state(self):
        return self.initial_state
