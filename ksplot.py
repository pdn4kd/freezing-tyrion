#! /usr/bin/python2.7
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#fancier numpy csv parsing to deal with headers
DR7 = np.genfromtxt('Tc_Obs_DR7.csv', dtype=None, delimiter=",", names=True)
S82 = np.genfromtxt('Tc_Obs_S82.csv', dtype=None, delimiter=",", names=True)
Tp_DR7 = DR7['Tp'] #not sure why these assignments are needed, but the plots generate a "ValueError: field named Tp not found" otherwise
Tc_DR7 = DR7['Tc']
Tp_S82 = S82['Tp']
Tc_S82 = S82['Tc']

print("Tc for DR7 vs S82:")
print(stats.ks_2samp(Tc_DR7, Tc_S82))
print("Tp for DR7 vs S82:")
print(stats.ks_2samp(Tp_DR7, Tp_S82))

'''
#scatter plots
fig, ax=plt.subplots()
ax.scatter(Tp_DR7, Tm_DR7, color="#FF7700", s=5, label="DR7")
ax.scatter(Tp_S82, Tm_S82, color="#0077FF", s=1, label="S82")
ax.set_xlim([0.002,0.014])
ax.set_ylim([0.003,0.009])
ax.set_xlabel("$T_p$", fontsize=20)
ax.set_ylabel("$T_m$", fontsize=20)
ax.set_title("$Image \, and \, Model \, Tidal \, Parameters \, (GALAPAGOS \, Masking)$", fontsize=30)
legend = ax.legend(loc=0, scatterpoints=1, fancybox=True)
plt.show()
#fig.savefig("scatter.png", format="png", dpi=150)
#histogram plots
#normalizing
weights_DR7 = [1.0 / len(Tc_DR7)] * len(Tc_DR7);
weights_S82 = [1.0 / len(Tc_S82)] * len(Tc_S82);

fig, bx=plt.subplots()
bx.hist(Tc_DR7, weights=weights_DR7, bins=[0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.010, 0.011, 0.012], histtype="stepfilled", color="gray", label="DR7")
bx.hist(Tc_S82, weights=weights_S82, bins=[0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.010, 0.011, 0.012], histtype='step', linewidth=2, color="k", label="S82")
bx.set_xlabel("$T_c$", fontsize=20)
bx.set_ylabel("$Relative \, Frequency$", fontsize=20)
bx.set_title("$T_c \, Distribution \, (GALAPAGOS \, Masking)$", fontsize=25)
bx.legend(loc=0, frameon=False)
plt.show()
#fig.savefig("scatter.pdf", format="pdf")
'''
