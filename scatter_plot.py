import matplotlib.pyplot as plt
import numpy as np

x = np.random.random_integers(low=1, high=100, size=200)
y = np.random.random_integers(low=1, high=100, size=200)


plt.scatter(x=x, y=y)

plt.scatter(x=x, y=y, color="black")

plt.scatter(x=x, y=y, marker="+")

plt.scatter(x=x, y=y, marker="*", s=150)

plt.scatter(x=x, y=y, marker="*", s=150, alpha=0.3)

plt.show()
