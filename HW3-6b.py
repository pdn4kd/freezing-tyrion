#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
plt.rc('font', family='Arial') #necessary to show the greek characters properly

#obs_fake = np.genfromtxt('HW3-6_transit_raw.csv', dtype=None, delimiter=',', names=True)
obs_real = np.genfromtxt('10bin.csv', dtype=None, delimiter=',', names=True)

G = 6.674e-11
r_star = 1.14*6.957e8 #solar radii -> meters
r_planet_range = np.arange(1.0*6.9911e7, 1.9*6.9911e7, 0.1*6.9911e7) #jupiter radii -> meters
p_planet_range = np.arange (3.50*86400, 3.58*86400, 0.01*86400) #JD -> seconds. Actual period is half this, but code currently cannot distinguish between primary and secondary eclipses.
m_star = 1.13*1.98855e30 #Solar masses -> kg
m_planet = 0.69*1.898e27 #Jupiter masses -> kg
epoch_range = np.arange(2453235.4, 2453235.6, 0.1) #actual JD max depth is ~2453235.5
impact_range = np.linspace(0.0, 0.9*r_star, num=10)

x1 = np.array([10**(-0.4*x) for x in obs_real['Rel_Mag']]) #mag -> relative flux

# constants for the hand-fit sanity check function. Current values are wrong.
#r_planet = 1.6*6.9911e7 #jupiter radii -> meters
#p_planet = 7.05*86400 #planet period JD -> seconds
#epoch = 2453235.5
#impact = 0.0*r_star #impact parameter

def trueanomaly(period, time=0, epoch=0):
	'''
	Circular uninclined orbit assumed.
	All must be in the same units.
	'''
	return 2*np.pi*(time-epoch)/period

def luminosity(rs, d):
	'''
	luminosity function for any point on the disk of the star, 
	normalized so sum does not have to be 1.0
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

def light(rp, rs, d, nu):
	'''
	Chunk up run: no overlap, partial overlap, complete overlap. 
	Numpy *will* throw warnings if the planet is bigger than the star. 
	Luminosity of star is assumed to not vary in obscured region. 
	This will be very incorrect for larger planets, unless u1 component is small.
	Output is normalized.
	'''
	if (d > (rs+rp) or np.cos(nu) < 0): # not blocked -- alongside or behind star
		return 1.0
	elif (d < (rs-rp)): # fully blocked
		return 1-luminosity(rs, d)*np.pi*rp**2
	else: # partial obscuration
		rl = rs-0.5*(rp+rs-d) # distance of center of intersection for luminosity estimate
		return 1-overlap(rp, rs, d)*luminosity(rs, rl)

def dist(p_period, sma, time, impact, epoch):
	nu = trueanomaly(p_period, time*86400.0, epoch*86400.0)
	x = sma*np.sin(nu) #projecting the view in-plane to get distance to star
	return np.sqrt(x**2+impact**2) # and distance to star, given impact parameter

def magnitude(rs, rp, pp, ms, mp, b, epoch, t):
	sma = (G*(ms+mp)*(pp/np.pi/2)**2)**(1.0/3) #meters
	x = dist(pp, sma, t, b, epoch)
	nu = trueanomaly(pp, t*86400.0, epoch*86400.0)
	return light(rp, rs, x, nu)

chisquarednumin = 1e9
fig, ax = plt.subplots()
ax.set_xlabel("Time (Julian Days)")
ax.set_ylabel("Relative Brightness (Stellar Units)")
ax.xaxis.set_major_formatter(FormatStrFormatter('%1.0f'))
ax.set_title("Model Transit(s) vs Real Data")
ideal_obs = np.linspace(obs_real['JD'][0], obs_real['JD'][-1], num=10*len(obs_real['JD']))
#model_transit = [magnitude(r_star, r_planet, p_planet, m_star, m_planet, impact, epoch, ts) for ts in ideal_obs]
ax.plot(obs_real['JD'], x1, linewidth=0, marker='.', markersize=2, color="#6699EE", label="Observations")
#ax.plot(ideal_obs, model_transit, linewidth=1, color="#008800", label="Model (Hand-fit)")
ax.set_xlim(np.floor(obs_real['JD'][0]), np.ceil(obs_real['JD'][-1]))

for epochi in epoch_range:
	for p_planeti in p_planet_range:
		for r_planeti in r_planet_range:
			for impacti in impact_range:
				y1 = [magnitude(r_star, r_planeti, p_planeti, m_star, m_planet, impacti, epochi, ts) for ts in obs_real['JD']]
				chisquared = sum(((x1-y1)**2)/y1/y1)
				chisquarednu = chisquared/len(obs_real['Rel_Mag'])
				print(chisquarednu)

				if (chisquarednu < chisquarednumin):
					chisquaredmin = chisquared
					chisquarednumin = chisquarednu
					ymin = y1
					impactmin = impacti
					r_planetmin = r_planeti
					p_planetmin = p_planeti
					epochmin = epochi

print("min chisquared: ", chisquaredmin)
print("min reduced chisquared: ", chisquarednumin)
print("r_planet (Jupiters): ", r_planetmin/6.9911e7)
print("p_planet (days): ", p_planetmin/86400.0)
sma = (G*(m_planet+m_star)*(p_planetmin/np.pi/2)**2)**(1.0/3)
print("sma (AU):", sma/149597870700.0)
print("b (stellar radii): ", impactmin/r_star)
print("Epoch: ", epochmin)
print("\nDepth, duration, i:", r_planetmin/r_star, r_star/(np.pi*sma), np.cos(impactmin/r_star))
ymin2 = [magnitude(r_star, r_planetmin, p_planetmin, m_star, m_planet, impactmin, epochmin, ts) for ts in ideal_obs]
ax.plot(ideal_obs, ymin2, linewidth=1, color="#FFAA88", label="Lowest χ²/ν")
ax.legend()

plt.savefig("HW3_6b-1.png", format='png')
plt.savefig("HW3_6b-1.svg", format='svg')
#plt.show()
