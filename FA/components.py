# State class definition
class state:

	# initialize state class
	def __init__(self, id):
		self.state_id = id
		self.next = dict() # transition function
