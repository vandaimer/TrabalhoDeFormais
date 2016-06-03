from AbstractAutomaton import AbstractAutomaton

class FiniteAutomaton(AbstractAutomaton):
    def __init__(self):
        super().__init__()

    def add_transition(self, stateA, terminal, stateB):
        if stateA not in self.states: return False
        if terminal not in self.alphabet: return False
        if stateB not in self.states: return False

        if stateA not in self.transitions:
            self.transitions[stateA] = {}
        if terminal in self.transitions[stateA]:
            return False
        self.transitions[stateA][terminal] = stateB
        return True

    def _achievable_states(self, state=None, achievable=None):
        transitions = None

        if achievable == None:
            achievable = {}

        if state == None:
            transitions = self.transitions
            state = self.initial_state
        else:
            transitions = self.transitions[state]

        if len(self.final_states) == 0 or self.initial_state == None:
            return False

        if len(transitions) > 0:
            achievable[self.initial_state] = None
            for terminal, state in self.transitions[self.initial_state].items():
                if not state in achievable:
                    self.minimize(state, achievable)
            return True
        return False
