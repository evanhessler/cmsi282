from backtracker import Backtracker

class Neas(Backtracker):
	def __init__(self, slots, values):
		self.slots = slots
		self.values = values

	def isValidPartialSolution(self, slotIndex):
		newSlots = slots[:slotIndex]
		for x in range(1, slotIndex):
			slotsDivided = [newSlots[i:i+x] for i in range(0, len(newSlots), x)]
			for a, b in zip(slotsDivided, slotsDivided[1:]):
				if a == b:
					return False
		return True
