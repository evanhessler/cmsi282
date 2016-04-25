from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subset_sum(numbers, value):
	current_list = []
	current_list_index = 0

	while current_list_index != value:
		for x in range(len(numbers) + 1):
			current_list = numbers[:x]
			for y in powerset(current_list):
				if sum(y) == value:
					print y
					return True

		current_list_index += 1

	return False
