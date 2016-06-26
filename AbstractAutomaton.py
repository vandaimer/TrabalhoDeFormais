

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

        if not isinstance(alphabet, tuple):
            alphabet = (alphabet,)
        else:
            alphabet = (alphabet)

        self.alphabet = alphabet
        return True

    def get_alphabet(self):
        return self.alphabet

    def add_state(self, state):
        if state in self.states: return False
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
            states = (states,)
        else:
            states = (states)

        list_states = list(self.states)
        for state in states:
            list_states.append(state)
        self.states = tuple(sorted(list_states))
        return True

    def add_transition(self, stateA, terminal, stateB ):
        raise NotImplementedError

    def get_transitions(self):
        return self.transitions

    def set_initial_state(self, state):
        if state not in self.states: return False
        self.initial_state = state
        return True

    def add_final_state(self, state):
        if state in self.final_states: return False
        if len(self.final_states) > 0:
            states = list(self.final_states)
            states.append(state)
            self.final_states = tuple(states)
        else:
            self.final_states = (state,)
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
