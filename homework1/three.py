def three_partition(numbers):
	if len(numbers) % 3 != 0:
		return False
	elif len(numbers) == 0:
		return True
	else:
		numbers.sort()
		target = 3 * sum(numbers) // len(numbers)
		for x in range(1, len(numbers)):
			for y in range(2, len(numbers)):
				if numbers[0] + numbers[x] + numbers[y] == target:
					numbers.pop(y)
					numbers.pop(x)
					numbers.pop(0)
					print(" ")
					print(" ")
					print(numbers)
					return three_partition(numbers)
		return False
