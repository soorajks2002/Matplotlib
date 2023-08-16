import matplotlib.pyplot as plt
import random

years = [200+x for x in range(25)]
weights = [60+random.randint(-10, 10) for x in range(25)]

# plt.plot(years, weights)

# plt.plot(years, weights, c='black')

# plt.plot(years, weights, lw=5)

plt.plot(years, weights, lw=2, linestyle="--")

plt.show()
