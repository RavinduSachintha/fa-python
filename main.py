from FA import components
from FA import automatons

def main():
	dfa = automatons.DFA()
	
	q0 = components.state("q0")
	q1 = components.state("q1")
	#q2 = components.state("q2")
	
	states = [q0, q1]
	alphabet = ["a", "b"]
	init_state = q0
	final_states = [q0]
	
	dfa.setup(states, alphabet, init_state, final_states)
	
	dfa.set_transition(q0,q1,["a"])
	dfa.set_transition(q0,q0,["b"])
	dfa.set_transition(q1,q0,["a"])
	dfa.set_transition(q1,q1,["b"])
	#dfa.set_transition(q2,q2,["a", "b"])
	
	dfa.verify_transitions_for_alphabet()
	
	dfa.check_string("aabba")
	
main()

