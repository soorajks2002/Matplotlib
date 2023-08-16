import matplotlib.pyplot as plt
import random

for i in range(100):
    heights = [i, i+random.randint(0, 5)]
    labels = ['first', 'second']
    plt.bar(x=labels, height=heights)
    plt.pause(0.001)

plt.show()
