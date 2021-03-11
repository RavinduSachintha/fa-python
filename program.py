from FA import automatons

from flask import jsonify

def response(status, message):
	return jsonify({'status': 'success' if status == 1 
		else 'error', 'message': message})	
	
def dfa_exec(json_model, string):
	dfa = automatons.DFA()
	dfa.setup_json_model(json_model)
	dfa.setup_by_json_model()
	dfa.set_transitions_by_json_model()
	dfa.verify_transitions_for_alphabet()
	return dfa.check_string(string)

