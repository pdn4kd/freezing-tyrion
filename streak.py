'''Calculates the probability of a long streak. More accurately, the probability of at least one run of r heads for n flips of a coin with a probability of heads of p. (That is, a Bernoulli trial)

Directly taken from https://arxiv.org/PS_cache/math/pdf/0511/0511652v1.pdf
'''

import numpy as np

def nck(n, k):
	'''classic n choose k, or combinations of k items chosen from a set of n. takes ints n, k. returns n!/(k!(n-k)!'''
	a = np.math.factorial(n)/np.math.factorial(k)/np.math.factorial(n-k)
	return a

# We want the probability of getting run of r in n trials.
# for this we have: y_n = 1 - β_{n,r} + p^r * β_{n-r,r}
# β_{n,r} = \sum_{l=0}^{n/(r+1)} (-1)^l * nck(n-lr, l) * (q*p^r)^l

# Many places on the net will get you z_n, where y_n = 1-z_n
# z_n = β_{n-r,r} - β_{n,r}

# Default values with a streak of 4 in 24 runs at 13% chance ending up at ~1/200
p = 0.13
q = 1-p
r = 4
n = 24

def β(n, r):
	range = np.arange(0, np.floor(n/(r+1))+1)
	b = [(-1)**l * nck(n - l*r, l) * (q * p**r)**l for l in range]
	return (np.sum(b))

y = 1 - β(n, r) + p**r * β(n-r, r)
print(y)
