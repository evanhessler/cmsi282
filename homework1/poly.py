class Polynomial:
	def __init__(self, coefficients):
		self.coefficients = coefficients
	def evaluate(self, x):
		total = 0
		for c in self.coefficients:
			total += self.coefficients[c] * x ** c
		return total
