from math import floor, ceil, sqrt
from backtracker import Backtracker

class Queens(Backtracker):
	def __init__(self, slots, values):
		self.slots = slots
		self.values = values

	def is_valid_partial_solution(self, slot_index):
		new_slots = slots[:slot_index]
		queens = [None]*len(new_slots)

		for x in range(len(queens)):
			if new_slots[x] > len(values) - 1:
				return False
			else:
				queens[x] = int(ceil(sqrt(len(values)))) - 1 - int(floor((len(values) - 1 - new_slots[x])/sqrt(len(values)))) , new_slots[x] % sqrt(len(values))

		for i in range(len(queens)):
		    for j in range(i + 1, len(queens)):
				if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
					return False

		return True

slots = [None] * 7
values = [x for x in range(0, 64)]
print Queens(slots, values).find_solution()
