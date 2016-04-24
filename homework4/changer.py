import math, copy
class Changer(object):

	def __init__(self, denominations):
		self.denominations = denominations

	def can_make_change_for(self, amount):
		minimum_coins = [0]

		for current_value in range(1, amount + 1):
			coins_needed = -float("infinity")
			for denomination in self.denominations:
				if current_value - denomination >= 0:
					new_minimum = minimum_coins[current_value - denomination] + 1
					if coins_needed < 0 or (new_minimum < coins_needed and new_minimum > -float("infinity")):
						coins_needed = new_minimum
			minimum_coins.append(coins_needed)

		return minimum_coins[amount]

	def can_make_change_using_each_coin_once(self, amount):
		minimum_coins = [0]
		denominations_used = [[]]

		for current_value in range(1, amount + 1):
			coins_needed = -float("infinity")
			current_denomination = None
			for denomination in self.denominations:
				if current_value - denomination >= 0 and denomination not in denominations_used[current_value - denomination]:
					new_minimum = minimum_coins[current_value - denomination] + 1
					if coins_needed < 0 or (new_minimum < coins_needed and new_minimum > -float("infinity")):
						coins_needed = new_minimum
						current_denomination = denomination
			if current_denomination is not None:
				denominations_used.append(copy.deepcopy(denominations_used[current_value - current_denomination]))
				denominations_used[current_value].append(current_denomination)
			else:
				denominations_used.append([])
			minimum_coins.append(coins_needed)

		return minimum_coins[amount]

	def can_make_change_with_limited_coins(self, amount, max_coins):
		return self.can_make_change_for(amount) > -float("infinity") and self.can_make_change_for(amount) <= max_coins
