# DFA class definition
class DFA:
	
	# Initialize DFA class
	def __init__(self):
		self.cur_state = None
		self.states = []
		self.alphabet = []
		self.init_state = None
		self.final_states = []
		
	# setup initial configurations of the automaton
	def setup(self, states, alphabet, init_state, final_states):
		self.states = states
		self.alphabet = alphabet
		self.init_state = init_state
		self.final_states = final_states
		
	# setup transitions of the automaton
	def set_transition(self, from_, to_, symbols):
		for s in symbols:
			assert s not in  from_.next.keys(), \
			"Symbol '%s' already defined in the state '%s'" % (s, from_.state_id)
			from_.next[s] = to_
		
	# verify all the transitions of the automaton for DFA
	def verify_transitions_for_alphabet(self):
		for state in self.states:
			assert set(state.next.keys()) == set(self.alphabet), \
			"Transition function definition is incorrect for the DFA"
	
	# check whether a given string is accepted or not by the automaton
	def check_string(self, input_string):
		self.cur_state = self.init_state
		i = 0
		
		while(i < len(input_string)):			
			reading_symbol = input_string[i]
			assert reading_symbol in self.alphabet, \
			"Input symbol '%s' is not defined in the alphabet" % reading_symbol
			self.cur_state = self.cur_state.next[reading_symbol]
			i += 1
		
		if self.cur_state in self.final_states:
			print("String '%s' is accepted by the DFA" % input_string)
		else:
			print("String '%s' is not accepted by the DFA" % input_string)

