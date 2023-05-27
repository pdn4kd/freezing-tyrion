'''Calculates the probability of a long streak.
First version is Taken from equation derived at https://math.stackexchange.com/questions/383704/probability-of-streaks which in turn uses https://www.askamathematician.com/2010/07/q-whats-the-chance-of-getting-a-run-of-k-successes-in-n-bernoulli-trials-why-use-approximations-when-the-exact-answer-is-known/ with a terrible convention.
'''

import numpy as np

#example: run of 4 in 24 trials with 63% chance of success
p = 0.63
q = 1-p
k = 4
n = 24


def nck(n, k):
	'''classic n choose k, or combinations of k items chosen from a set of n. takes ints n, k. returns n!/(k!(n-k)!'''
	a = np.math.factorial(n)/np.math.factorial(k)/np.math.factorial(n-k)
	return a

sum1 = np.arange(np.floor((n-k)/(k+1)) + 1)
S1 = [nck(n-k*(t+1),t) * (-q*p**k)**t for t in sum1]

sum2 = np.arange(np.floor(n/(k+1)) + 1)
#print(sum1,sum2)
#print(S1)
S2 = [nck(n-k*t,t) * (-q*p**k)**t for t in sum2]

#print("t1 max: ", (n-k)/(k+1)+1)
#print("t2 max: ", n/(k+1)+1)

#print(S2)
streak = p**k * np.sum(S1) - np.sum(S2)
print(1+streak) #suggests that the formula is wrong

#an alternate version found at https://math.stackexchange.com/questions/59738/probability-for-the-length-of-the-longest-run-in-n-bernoulli-trials#comment1032559_59749
# probability, num trials, streak length
#p = 0.63
#n = 4
#m = 2

#sequence = np.arange(1, np.floor((n+1)/(m+1)) + 1)

#P = [(-1)**(j+1) * (p+((n-j*m+1)/j)*(1-p)) * nck(n-j*m,j-1) * p**(j*m) * (1-p)**(j-1) for j in sequence]
#prob = np.sum(P)
#print(P, prob)

#Yet another approach is in https://arxiv.org/PS_cache/math/pdf/0511/0511652v1.pdf
# We want the probability of getting run of r in n trials.
# for this we have: y_n = 1 - β_n,r + p^r * β_n-r,r
# β_n,r = \sum_{l=0}^{n/(r+1)} (-1)^l * nck(n-lr, l) * (q*p^r)^l

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
