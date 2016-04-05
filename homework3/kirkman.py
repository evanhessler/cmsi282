import copy

class Kirkman():
    days = [[[None, None, None] for count in range(5)] for count in range(7)]

    def find_solution(self):
        slot = 0

        while slot < 90:
            day = slot / 15
            group = slot % 15 / 3
            person = slot % 15 % 3

            value_before_backtrack = copy.deepcopy(self.days[day][group][person])
            self.days[day][group][person] = None

            start = self.determine_first_walker_to_test(day, group, person, value_before_backtrack)
            end = self.determine_last_walker_to_test(day, group, person)

            print "start", chr(start + ord('A')), "end", chr(end + ord('A'))
            foundSolution = False
            for walker in range(start, end):
                if not foundSolution and self.can_walk(day, group, walker):
                    self.days[day][group][person] = walker
                    slot += 1
                    foundSolution = True

            if not foundSolution:
                slot -= 1
                
        return self.days

    def determine_first_walker_to_test(self, day, group, person, value_before_backtrack):
        if value_before_backtrack is not None:
            return value_before_backtrack + 1
        else:
            result_greater_than = [-1]

            if person != 0:
                result_greater_than.append(self.days[day][group][person - 1])

            if person == 0 and group != 0:
                result_greater_than.append(self.days[day][group - 1][person])

            if day != 0 and person == 1 and group == 0:
                result_greater_than.append(self.days[day - 1][group][person])

            if day != 0 and person == 0 and group < 3:
                result_greater_than.append(group - 1)

            if day < 2 and group != 0:
                result_greater_than.append(self.days[day][group - 1][person])

            if day != 0 and (person != 0 or group > 2):
                result_greater_than.append(2)

            return max(result_greater_than) + 1


    def determine_last_walker_to_test(self, day, group, person):
        result_less_than_or_equal_to = [14]

        if day != 0 and person != 2:
            result_less_than_or_equal_to.append(11)

        if day != 0 and person == 0 and group < 3:
            result_less_than_or_equal_to.append(group)

        if person == 0 and day != 0 and group < 3:
            result_less_than_or_equal_to.append(self.days[day-1][group][0])

        return min(result_less_than_or_equal_to) + 1

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
            print day
