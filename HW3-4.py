#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

# M = mean anomaly
# E = eccentric anomaly, approximated by a 1st-order Taylor series centered 
# at M. This works very well for low eccentricity, but suffers increasingly 
# near 0 and 2 pi as e approaches 1. Newton-Raphson or Bisection would 
# probably improve precision.
# F = true anomaly
t = np.linspace(0, 1, num=1000)
for e in [0.3,0.6,0.9]:
	M = t*2*np.pi
	E = (M + e*np.sin(M) - M*e*np.cos(M))/(1 - e*np.cos(M)) #
	F = np.arccos((np.cos(E) - e) / (1 - e*np.cos(E)))
	E_true = (M-e*np.sin(M))/(2*np.pi) #comparison silliness
	
	fig, ax = plt.subplots()
	ax.plot(t, E, linewidth=1, color="#CC5533", label="Eccentric (Approx)")
	ax.plot(E_true, M, linewidth=1, color="#FFAA88", label="Eccentric (Actual)")
	ax.plot(t, M, linewidth=1, color="#77EE77", label="Mean")
	ax.plot(t, F, linewidth=2, color="#9977EE", label="True (Approx)")

	ax.set_xlim(0,max(t))
	ax.set_ylim(0,6.283)
	ax.set_xlabel("Time Since Epoch (orbital period)")
	ax.set_ylabel("Anomaly (Radians)")
	ax.set_title("Eccentricity = "+str(e))
	ax.legend(loc=2)
	plt.show()
	#plt.savefig("HW3_4_"+str(e)+".png")
