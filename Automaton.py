from AbstractAutomaton import AbstractAutomaton

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
