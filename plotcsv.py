#import matplotlib.pyplot as plt
import numpy as np
#from astropy.table import Table #needed for better csv parsing?

#simple numpy csv parsing, fails to account for headers
csv = np.genfromtxt('Tc_DR7.csv', delimiter=",")
Tp_DR7 = csv[:,2]
Tm_DR7 = csv[:,3]
Tc_DR7 = csv[:,4]
csv = np.genfromtxt('Tc_S82.csv', delimiter=",")
Tp_S82 = csv[:,2]
Tm_S82 = csv[:,3]
Tc_S82 = csv[:,4]

#fancier numpy csv parsing to deal with headers
arraycsv = np.genfromtxt('Tc_DR7.csv', dtype=None, delimiter=",", names=True)
print arraycsv['Tc']
'''
import csv
csvarray = np.genfromtxt('Tc_DR7.csv', delimiter=",", skip_header=1)
with open('Tc_DR7.csv', 'rb') as csvfile:
	csvreader = csv.reader(csvfile, dialect='excel') 
	for row in csvreader:
		for col in row:
			if(col == "ID"):
				print col
		#print ','.join(col)
'''
'''
fig, cx=plt.subplots()
cx.contour(Tp_DR7,Tm_DR7)
#cx.contour(Tp_S82, Tm_S82, color="#0000FF", s=1, label="S82")
cx.set_xlim([0.002,0.014])
cx.set_ylim([0.003,0.009])
cx.set_xlabel("$T_p$", fontsize=20)
cx.set_ylabel("$T_m$", fontsize=20)
cx.set_title("$Image \, and \, Model \, Tidal \, Parameters \, (GALAPAGOS \, Masking)$", fontsize=30)
legend = cx.legend(loc=0, scatterpoints=1, fancybox=True)
plt.show()
'''
'''
#scatter plots, need legends
fig, ax=plt.subplots()
ax.scatter(Tp_DR7, Tm_DR7, color="#FF0000", s=5, label="DR7")
ax.scatter(Tp_S82, Tm_S82, color="#0000FF", s=1, label="S82")
ax.set_xlim([0.002,0.014])
ax.set_ylim([0.003,0.009])
ax.set_xlabel("$T_p$", fontsize=20)
ax.set_ylabel("$T_m$", fontsize=20)
ax.set_title("$Image \, and \, Model \, Tidal \, Parameters \, (GALAPAGOS \, Masking)$", fontsize=30)
legend = ax.legend(loc='lower right', scatterpoints=1, fancybox=True)
legend.set_title("foobar") #note how legend had to be set as a thing for this manipulation
plt.show()
#fig.savefig("scatter.png", format="png", dpi=150)

#histograms, need legends
#normalizing
weights_DR7 = [1.0 / len(Tc_DR7)] * len(Tc_DR7);
weights_S82 = [1.0 / len(Tc_S82)] * len(Tc_S82);

fig, bx=plt.subplots()
bx.hist(Tc_DR7, weights=weights_DR7, bins=[0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.010, 0.011, 0.012], histtype="stepfilled", color="gray", label="DR7")
bx.hist(Tc_S82, weights=weights_S82, bins=[0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.010, 0.011, 0.012], histtype='step', linewidth=2, color="k", label="S82")
bx.set_xlabel("$T_c$", fontsize=20)
bx.set_ylabel("$Relative \, Frequency$", fontsize=20)
bx.set_title("$T_c \, Distribution \, (GALAPAGOS \, Masking)$", fontsize=25)
bx.legend(loc='upper left', frameon=False)
plt.show()
#fig.savefig("scatter.pdf", format="pdf")
'''
