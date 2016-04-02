from math import floor
import copy
import sys
sys.setrecursionlimit(10000)

class Kirkman():
	days = [[[None, None, None] for count in range(5)] for count in range(7)]

	def find_solution(self):
		slot = 0

		while slot < 105:
			day = slot / 15
			group = slot % 15 / 3
			person = slot % 15 % 3

			value_before_backtrack = copy.deepcopy(self.days[day][group][person])
			self.days[day][group][person] = None

			start = self.determine_first_walker_to_test(day, group, person, value_before_backtrack)
			end = self.determine_last_walker_to_test(day, group, person)
			print start, end
			foundSolution = False
			for walker in range(start, end):
				if not foundSolution and self.can_walk(day, group, walker):
					self.days[day][group][person] = walker
					slot += 1
					foundSolution = True

			if not foundSolution:
				slot -= 1

			print self.to_string(), "\r",

	def place_from(self, slot):
		if slot < 0:
			return False

		day = slot / 15
		group = slot % 15 / 3
		person = slot % 15 % 3

		value_before_backtrack = copy.deepcopy(self.days[day][group][person])
		self.days[day][group][person] = None
		#print "\n", self.to_string()

		start = self.determine_first_walker_to_test(day, group, person, value_before_backtrack)
		end = self.determine_last_walker_to_test(day, group, person)
		self.to_string(), "\n\n"
		print "start", chr(start + ord('A')), "end", chr(end + ord('A'))
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
		return 0

	def determine_last_walker_to_test(self, day, group, person):
		return 15

	def can_walk(self, day, group, walker):
		total_in_day = 0

		for groups in self.days[day]:
			if walker in groups:
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

print Kirkman().find_solution()
#print example.to_string()
#cd documents/lmu/sophomore/"Second Semester"/algorithms/"Homework 3"
