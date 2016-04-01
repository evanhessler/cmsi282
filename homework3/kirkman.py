from math import floor

class Kirkman():
	day_one = [[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]]
	empty_days = [[[None]*3]*5]*6
	days = day_one + empty_days
	backtracked = False

	def find_slot(self, slot_number):
		return days[floor(slot_number / 15)]

	def place_from(self, slot):
		day = slot / 15
		group = slot % 15 / 3
		person = slot % 15 % 3

		start = self.determine_first_walker_to_test(day, group, person, self.backtracked)
		end = self.determine_last_walker_to_test(day, group, person, self.backtracked)
		foundWalker = False
		
		for walker in range(start, end):
			print self.can_walk(day, group, walker)
			if not foundWalker and self.can_walk(day, group, person, walker):
				self.days[day][group][person] = walker
				foundWalker = True
				backtracked = False
				if slot == 105:
					return self.days
				else:
					self.place_from(slot+1)

		if not foundWalker:
			backtracked = True
			self.place_from(slot-1)
		
	def determine_first_walker_to_test(self, day, group, person, backtracked):
		return 0

	def determine_last_walker_to_test(self, day, group, person, backtracked):
		return 1

	def can_walk(self, day, group, walker):
		total_in_day = 0

		for group in self.days[day]:
			total_in_day += group.count(walker)
			if total_in_day > 1:
				return False

		people_walked_with = group

		for day in self.days:
			for group in day:
				if walker in group:
					for person in group:
						if person != walker:
							people_walked_with.append(person)
							if len(set(people_walked_with)) != len(people_walked_with):
								return False
		print "\n", people_walked_with
		return True

	def to_string(self):
		days_as_string = self.days
		for day in range(len(days_as_string)):
			for group in range(len(days_as_string[day])):
				for person in range(len(days_as_string[day][group])):
					if days_as_string[day][group][person] is not None:
						days_as_string[day][group][person] = chr(days_as_string[day][group][person] + ord('A'))
			print days_as_string[day], "\n"

example = Kirkman().place_from(14)
#print example.to_string()
