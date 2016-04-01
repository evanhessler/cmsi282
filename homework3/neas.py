from backtracker import Backtracker

class Neas(Backtracker):
	def __init__(self, slots, values):
		self.slots = slots
		self.values = values

	def is_valid_partial_solution(self, slot_index):
		new_slots = slots[:slot_index]
		for x in range(1, slot_index):
			slots_divided = [new_slots[i:i+x] for i in range(0, len(new_slots), x)]
			for a, b in zip(slots_divided, slots_divided[1:]):
				if a == b:
					return False
		return True
