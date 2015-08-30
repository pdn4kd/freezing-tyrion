import matplotlib.pyplot as plt
import numpy as np

xs = np.arange(0, 5, 0.5)
y1 = [x*3 for x in xs]
y2 = [x**2 for x in xs]
y3 = [x for x in xs]

plt.plot(xs, y1)
plt.plot(xs, y2)
plt.plot(xs, y3);
plt.show()

plt.plot([1,2,3], [1,2,3])
plt.plot([1,2,3], [3,1,2])
plt.show()
