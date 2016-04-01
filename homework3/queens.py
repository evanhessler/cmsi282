from math import floor, sqrt
from backtracker import Backtracker

#Queens placement out goes from left to right. I.e. for 8x8 board, 0 is top left, 7 is top right, 63 is bottom right.
class Queens(Backtracker):
	def __init__(self, slots, values):
		self.slots = slots
		self.values = values

	def isValidPartialSolution(self, slotIndex):
		newSlots = slots[:slotIndex]
		queens = [None]*len(newSlots)

		for x in range(len(queens)):
			if newSlots[x] > len(values) - 1:
				return False
			else:
				queens[x] = 7 - int(floor((len(values) - 1 - newSlots[x])/sqrt(len(values)))) , newSlots[x] % sqrt(len(values))

		for i in range(len(queens)):
		    for j in range(i + 1, len(queens)):
				if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
					return False

		return True
