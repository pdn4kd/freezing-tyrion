import matplotlib.pyplot as plt
import numpy as np

#scatter plots
#x1 = np.random.normal(0, 2, 30)
#x2 = np.random.normal(0, 2, 30)
#y1 = np.random.normal(0, 2, 30)
#y2 = np.random.normal(0, 2, 30)

#plt.scatter(x1, y1)
#plt.scatter(x2, y2, c="r")
#plt.show()

#histograms
data = np.random.normal(loc=0, scale=2.0, size=100)
plt.hist(data, bins=5, align="mid")
plt.xlabel("X", fontsize=5)
plt.ylabel("y", fontsize=20)
plt.title("random histogram")
plt.show()
plt.hist(data, bins=[-4,-2,0,2,4])
plt.xlabel("X", fontsize=30)
plt.ylabel("y", fontsize=1)
plt.title("AnOtHeR random histogram", fontsize=8)
plt.show()
