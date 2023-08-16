import matplotlib.pyplot as plt
import random
from matplotlib import style

style.use('dark_background')

g1 = [random.randint(1, 10) for i in range(30)]
g2 = [random.randint(11, 20) for i in range(30)]
g3 = [random.randint(21, 30) for i in range(30)]
g4 = [random.randint(31, 40) for i in range(30)]

fig, ax = plt.subplots(nrows=2, ncols=2)

ax[0][0].plot(g1)
ax[0][1].plot(g2)
ax[1][0].plot(g3)
ax[1][1].plot(g4)

ax[0][0].set_title('graph 1')
ax[0][1].set_title('graph 2')
ax[1][0].set_title('graph 3')
ax[1][1].set_title('graph 4')

ax[1][1].set_xlabel('x value')
ax[0][0].set_ylabel('y value')

fig.suptitle('Sub Plots Example')
plt.show()
