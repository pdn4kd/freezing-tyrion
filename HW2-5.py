#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

'''
Toy lightcurve generation program for AST 613 homework.
Intersection equation from Wolfram Alpha:
http://mathworld.wolfram.com/Circle-CircleIntersection.html
'''

G = 6.674e-11
r_star = 1.0*6.957e8 #solar radii -> meters
r_planet = 1.0*6.9911e7 #jupiter radii -> meters
sma = 5.2*149597870700 #AU -> meters
m_star = 1.0*1.98855e30 #Solar masses -> kg
impact = 0.05*r_star #impact parameter
anomaly = np.arange(1e-5, 3.14159, 1e-5) #chunking planet's orbit based on mean anomaly. Epoch is maximum elongation because that is easiest to impliment.
x = sma*np.cos(anomaly) #projecting the view in-plane to get distance to star
distance = np.sqrt(x**2+impact**2) # and distance to star, given impact parameter
time = anomaly*np.sqrt(sma**3/(m_star*G))/86400 #anomaly -> time in julian days, only works in circular orbit

# find overlap area when transiting.
def overlap(rp, rs, d):
	area = rp**2*np.arccos((d**2+rp**2-rs**2)/(2*d*rp)) + rs**2*np.arccos((d**2+rs**2-rp**2)/(2*d*rs)) - 0.5*np.sqrt((-d+rp+rs)*(d+rp-rs)*(d-rp+rs)*(d+rp+rs))
	return area

#Chunk up run: no overlap, partial overlap, complete overlap.
#Output is normalized.
def light(rp, rs, d):
	if (d > (rs+rp)):
		return 1.0 # not blocked
	elif (d < (rs-rp)):
		return (rs**2 - rp**2)/rs**2 # fully blocked
	else:
		return (np.pi*rs**2-overlap(rp, rs, d))/(np.pi*rs**2)

y1 = [light(r_planet, r_star, xs) for xs in distance]

fig, ax = plt.subplots()
ax.plot(time, y1, linewidth=3, color="#FFAA88")
ax.set_xlim(1082,1084)
ax.set_ylim(0.985,1.005)
ax.set_xlabel("Time Since Epoch (Julian Days)")
ax.set_ylabel("Relative Brightness (Arbitrary Units)")
ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
ax.set_title("Example Jupiter Transit")
plt.show()
#plt.savefig("HW2_5.png")
