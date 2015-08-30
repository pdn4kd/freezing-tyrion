import matplotlib.pyplot as plt
import numpy as np
#import csv

#numpy csv parsing
csv = np.genfromtxt('Tc_DR7.csv', delimiter=",")
Tp = csv[:,3]
Tm = csv[:,4]

print Tp

#csv parsing
#with open('Tc_DR7.csv', 'rb') as csvfile:
#	csvreader = csv.reader(csvfile, dialect='excel') 
#	for row in csvreader:
#		for col in row:
			#if(col == "ID"):
#			print col
		#print ','.join(col)
		

#scatter plots
#plt.scatter(Tp, Tm)
#plt.scatter(x2, y2, c="r")
#plt.show()

#histograms
#data = np.random.normal(loc=0, scale=2.0, size=100)
#plt.hist(data, bins=5, align="mid")
#plt.xlabel("X", fontsize=5)
#plt.ylabel("y", fontsize=20)
#plt.title("random histogram")
#plt.show()
#plt.hist(data, bins=[-4,-2,0,2,4])
#plt.xlabel("X", fontsize=30)
#plt.ylabel("y", fontsize=1)
#plt.title("AnOtHeR random histogram", fontsize=8)
#plt.show()
