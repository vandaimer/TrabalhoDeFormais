from AbstractAutomaton import AbstractAutomaton
from FiniteAutomaton import FiniteAutomaton


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
        newAutomaton = FiniteAutomaton()

        if not self.is_deterministic():
            if len(self.transitions) == 0: return False
            newAutomaton.set_alphabet(self.alphabet)
            newAutomaton.add_state(self.initial_state)
            for simbol in self.alphabet:
                dict_union_states = {}
                for another_state in self.transitions[self.initial_state][simbol]:
                    for x in self.alphabet:
                        if dict_union_states.get(x) != None:
                            if self.transitions.get(another_state) != None:
                                dict_union_states[x] = dict_union_states[x].union(set(self.transitions.get(another_state)[x]))
                        else:
                            dict_union_states[x] = set(self.transitions.get(another_state)[x])

                newState = ''.join(sorted(self.transitions[self.initial_state][simbol]))
                newAutomaton.add_state(newState)
                newAutomaton.add_transition(self.initial_state, simbol, newState)

                for index, states in dict_union_states.items():
                    state = ''.join(sorted(list(states)))
                    newAutomaton.add_state(state)
                    newAutomaton.add_transition(newState, index, state)

            for final_state in self.final_states:
                for state in newAutomaton.states:
                    if final_state in state:
                        newAutomaton.add_final_state(state)
            return newAutomaton

        for index, transition in self.transitions.items():
            for simbol,list_states in self.transitions[index].items():
                self.transitions[index][simbol] = ''.join(list_states)

        return self

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
