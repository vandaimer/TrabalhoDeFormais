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

    def _live_states(self, achievable_states=None, life_states=None, other_states=None):
        if len(self.transitions) > 0:
            if len(self.final_states) == 0 or self.initial_state == None:
                return False

            achievable_states = set(achievable_states)
            final_states = set(self.final_states)

            if life_states == None:
                life_states = achievable_states.intersection(final_states)

            if other_states == None:
                other_states = achievable_states.difference(life_states)

            for state in other_states:
                list_state_of_life_state = set(self.transitions[state].values())
                for item in list_state_of_life_state:
                    if item in life_states:
                        life_states.add(state)
                    elif item != state and item in achievable_states:
                        new_life_states = self._live_states(achievable_states, life_states, (item,) )
                        life_states.union(new_life_states)
                        if item in life_states:
                            life_states.add(state)
                achievable_states.remove(state)
            return life_states
        return False

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
            achievable[state] = None
            for terminal, stateB in self.transitions[state].items():
                if not stateB in achievable:
                    self._achievable_states(stateB, achievable)
            return set(achievable)
        return False
