class Backtracker(object):
	def find_solution(self):
		backtracked = False
		slot = 0
		while slot < len(self.slots):
			found_working_value = False
			if backtracked:
				starting_value = self.values.index(self.slots[slot]) + 1
			else:
				starting_value = 0
			if starting_value < len(self.values):
				for value in range(starting_value, len(self.values)):
					if not found_working_value:
						self.slots[slot] = self.values[value]
						if self.is_valid_partial_solution(slot + 1):
							found_working_value = True
			if not found_working_value:
				self.slots[slot] = None
				slot -= 1
				backtracked = True
				if slot < 0:
					return False
			else:
				slot += 1
				backtracked = False
		return self.slots
