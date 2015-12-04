import matplotlib.pyplot as plt
import numpy as np

P = 0 # payload mass
E = 0.5 # engine mass (LV-909)
F = 60 # thrust (LV-909)
R = 9 # tankage mass ratio
Ve = 9.80665*345 # effective exhaust velocity (LV-909)
TMR = np.arange(0, 40, 0.2) # thrust to mass ratios
#dV = [Ve*np.log(R*F/((x*(E+P)*(R-1))+F)) for x in TMR]
Terrier00 = [Ve*np.log(R*F/((x*(E+0)*(R-1))+F)) for x in TMR]
Terrier01 = [Ve*np.log(R*F/((x*(E+0.1)*(R-1))+F)) for x in TMR]
Terrier03 = [Ve*np.log(R*F/((x*(E+0.3)*(R-1))+F)) for x in TMR]
Terrier10 = [Ve*np.log(R*F/((x*(E+1)*(R-1))+F)) for x in TMR]
Terrier30 = [Ve*np.log(R*F/((x*(E+3)*(R-1))+F)) for x in TMR]
Terrier100 = [Ve*np.log(R*F/((x*(E+10)*(R-1))+F)) for x in TMR]

fig, ax=plt.subplots()
#ax.plot(TMR, dV, color="#0099FF", label="LV-909 (0 payload)")
ax.plot(TMR, Terrier00, color="#0000AA", label="LV-909 (0.0 payload)")
ax.plot(TMR, Terrier01, color="#0099FF", label="LV-909 (0.1 payload)")
ax.plot(TMR, Terrier03, color="#0099FF", label="LV-909 (0.3 payload)")
ax.plot(TMR, Terrier10, color="#0099FF", label="LV-909 (1.0 payload)")
ax.plot(TMR, Terrier30, color="#0099FF", label="LV-909 (3.0 payload)")
ax.plot(TMR, Terrier100, color="#00AAFF", label="LV-909 (10 payload)")
#ax.set_xlim([0.002,0.014])
#ax.set_ylim([0.003,0.009])
ax.set_xlabel("Accelleration at maximum mass (m/s/s)", fontsize=15)
ax.set_ylabel("dV (m/s)", fontsize=15)
ax.set_title("LV-909 'Terrier' vs LV-N 'Nerv'", fontsize=20)
legend = ax.legend(loc=0, fancybox=True)
plt.show()
#fig.savefig("lvn909_v105.png", format="png", dpi=150)
#fig.savefig("lvn909_v105.svg", format="svg")
