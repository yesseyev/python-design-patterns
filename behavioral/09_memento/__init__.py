import pickle


class Originator:

	def __init__(self):
		self._state = None

	def create_memento(self):
		return pickle.dumps(vars(self))

	def set_memento(self, memento):
		previous_state = pickle.loads(memento)
		vars(self).clear()
		vars(self).update(previous_state)


def main():
	# Init
	originator = Originator()
	# Printing default object variables
	print('Initial state', vars(originator))

	# Creating memento (dumping state)
	memento = originator.create_memento()

	# Changing current state
	originator._state = True
	print('Modified state', vars(originator))  # Printing object vars

	# Restoring saved memento state
	originator.set_memento(memento)
	print('Restored state', vars(originator))  # Printing object vars


if __name__ == "__main__":
	main()
