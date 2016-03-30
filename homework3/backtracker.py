from abc import ABCMeta, abstractmethod

class Backtracker():
	__metaclass__  = ABCMeta

	@abstractmethod
	def isValidPartialSolution(self, slotIndex):
		"""Returns if valid partial solution"""

	def findSolution(self):
		triedValue = [[False for x in range(len(values))] for x in range(len(slots))]
		slot = 0
		while slot < len(slots):
			foundValue = False
			for value in values:
				if not foundValue:
					slots[slot] = value
					print "slot:", slot, "value:", value, slots, "valid solution:", self.isValidPartialSolution(slot + 1), "tried value:", triedValue[slot][value]
					if not triedValue[slot][value] and self.isValidPartialSolution(slot + 1):
						foundValue = True
						triedValue[slot][value] = True
			if not foundValue:
				slots[slot] = None
				slot -= 1
				if slot < 0:
					return False
			else:
				slot += 1
		return slots
