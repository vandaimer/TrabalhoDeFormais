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

    def minimize(self, live_states=None):
        validation = live_states != None and len(self.final_states) > 0 and len(self.transitions) > 0
        classes = []
        if validation:
            dict_states = {}
            class_f = ClassStates()
            class_k_f = ClassStates()
            for state in live_states:
                if state in self.final_states:
                    class_f.add_state(state)
                else:
                    class_k_f.add_state(state)

            # classes.append(class_f)
            classes.append(class_k_f)

            for item in classes:
                states = item.get_states().copy()
                for state in item.get_states():
                    print( "state ", state )
                    del states[state]
                    for state_b in states:
                        active = item.get_state(state_b)
                        if active:
                            transitions = self.transitions[state]
                            transitions_b = self.transitions[state_b]
                            classBuffer = ClassStates()
                            for simbol in self.alphabet:

                                validation = ( item.has_state(transitions[simbol]) != True and item.has_state(transitions_b[simbol]) == True) or ( item.has_state(transitions[simbol]) == True and item.has_state(transitions_b[simbol]) != True)

                                if validation:
                                    classBuffer.add_state(state_b)
                                    item.inative_state(state_b)

                            if len(classBuffer.get_states()) > 0:
                                classes.append(classBuffer)
            x = [list(x.get_states().keys()) for x in classes]
            print(x)
            return x
        return False

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
                        achievable_states.remove(item)
                        new_life_states = self._live_states(achievable_states, life_states, (item,) )
                        life_states.union(new_life_states)
                        if item in life_states:
                            life_states.add(state)
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

class ClassStates:
    def __init__(self):
        self.states = {}

    def add_state(self, state):
        self.states[state] = True

    def remove_state(self, state):
        del self.states[state]

    def get_states(self):
        return self.states

    def has_state(self, state):
        return state in self.states

    def get_state(self, state):
        has_state = self.has_state(state)
        if has_state:
            return self.states[state]
        return False

    def inative_state(self, state):
        has_state = self.has_state(state)
        if has_state:
            self.states[state] = False
            return True
        return False
