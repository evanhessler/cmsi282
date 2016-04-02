from math import floor
import copy
import sys
sys.setrecursionlimit(10000)

class Kirkman():
	day_one = [[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]]
	empty_days = [[[None, None, None] for count in range(5)] for count in range(6)]
	days = day_one + empty_days

	def place_from(self, slot):
		if slot < 0:
			return False

		day = slot / 15
		group = slot % 15 / 3
		person = slot % 15 % 3

		print group

		value_before_backtrack = copy.deepcopy(self.days[day][group][person])
		self.days[day][group][person] = None
		#print "\n", self.to_string()

		start = self.determine_first_walker_to_test(day, group, person, value_before_backtrack)
		end = self.determine_last_walker_to_test(day, group, person)
		#print slot, chr(start + ord('A')), chr(end + ord('A'))
		for walker in range(start, end):
			if self.can_walk(day, group, walker):
				self.days[day][group][person] = walker
				value_before_backtrack = None
				if slot == 105:
					return self.days
				else:
					self.place_from(slot + 1)

		self.place_from(slot - 1)

	def determine_first_walker_to_test(self, day, group, person, value_before_backtrack):
		if value_before_backtrack is not None:
			return value_before_backtrack + 1

		else:
			result = group
			result_greater_than = []

			if person != 0:
				result_greater_than.append(self.days[day][group][person - 1])

			if (person == 0 and group != 0) or (day < 2 and group != 0):
				result_greater_than.append(self.days[day][group - 1][person])

			if len(result_greater_than) != 0:
				result = max(result_greater_than) + 1

			return result

	def determine_last_walker_to_test(self, day, group, person):
		if person == 0:
			if group == 0:
				return 1
			if day != 0:
				return self.days[day - 1][group][0] + 1
		return 14

	def can_walk(self, day, group, walker):
		total_in_day = 0

		for groups in self.days[day]:
			total_in_day += groups.count(walker)
			if total_in_day > 0:
				return False

		people_walked_with = []
		for person in self.days[day][group]:
			if person is not None:
				people_walked_with.append(person)

		for day in self.days:
			for group in day:
				if walker in group:
					for person in group:
						if person != walker and person != None:
							people_walked_with.append(person)
							if len(set(people_walked_with)) != len(people_walked_with):
								return False
		return True

	def to_string(self):
		days_as_string = copy.deepcopy(self.days)
		
		for day in days_as_string:
			for group in day:
				for person in range(len(group)):
					if group[person] is not None:
						group[person] = chr(group[person] + ord('A'))
		return days_as_string

print Kirkman().place_from(15)
