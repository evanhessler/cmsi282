import random
import timeit

def bozosort(list):
	if sorted(list) == list:
		return list
	else:
		one = random.choice(list)
		two = random.choice(list)
		list[list.index(one)] = two
		list[list.index(two)] = one
		bozosort(list)

my_randoms = random.sample(xrange(1, 101), 7)
start = timeit.default_timer()
bozosort(my_randoms)
stop = timeit.default_timer()
print my_randoms
print str(1000 * (stop - start))
