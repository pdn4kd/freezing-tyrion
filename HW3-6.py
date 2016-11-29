#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from scipy.integrate import quad

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

def luminosity(rs, d):
	'''
	luminosity function for any point on the disk of the star, 
	normalized so total is (supposedly) 1.0.
	Set u0 to 0 and u1 to 1 for lambert-like (no temperature/opacity, just angle).
	Set u0 to 1 and u1 to 0 for constant luminosity across disk.
	'''
	u0 = 0.8
	u1 = 0.2
	return (u0 + u1*np.sqrt(rs**2-d**2)/rs) / (u0*np.pi*rs**2 + u1*np.pi*rs**2/2)

# find overlap area when transiting.
def overlap(rp, rs, d):
	area = rp**2*np.arccos((d**2+rp**2-rs**2)/(2*d*rp)) + rs**2*np.arccos((d**2+rs**2-rp**2)/(2*d*rs)) - 0.5*np.sqrt((-d+rp+rs)*(d+rp-rs)*(d-rp+rs)*(d+rp+rs))
	return area

#Chunk up run: no overlap, partial overlap, complete overlap.
#Luminosity of star is assumed to not vary in obscured region. This will produce significant errors for larger planets, unless u1 component is small.
#Output is normalized.
def light(rp, rs, d):
	if (d > (rs+rp)): # not blocked
		return 1.0
	elif (d < (rs-rp)): # fully blocked
		return 1-luminosity(rs, d)*np.pi*rp**2
	else: # partial obscuration
		rl = rs-0.5*(rp+rs-d) # distance of center of intersection for luminosity estimate
		return 1-overlap(rp, rs, d)*luminosity(rs, rl)

y1 = [light(r_planet, r_star, xs) for xs in distance]

fig, ax = plt.subplots()
ax.plot(time, y1, linewidth=3, color="#FFAA88")
ax.set_xlim(1082,1084)
ax.set_ylim(0.975,1.005)
ax.set_xlabel("Time Since Epoch (Julian Days)")
ax.set_ylabel("Relative Brightness (Solar Units)")
ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
ax.set_title("Example Jupiter Transit")
plt.show()
#plt.savefig("HW3_6a-1.png", format='png')
#plt.savefig("HW3_6a-1.svg", format='svg')
#plt.savefig("HW3_6a-1.pdf", format='pdf')

#output file for fitting.
#should we have noise?
#f = open("HW3-6_transit_raw.csv", mode='w')
#f.write("Time,Relative Brightness\n")
#for x, y in np.nditer([time, y1]):
#	print("%f,%f" % (x,y))
#	f.write("%f,%f\n" % (x,y))
#f.close()
