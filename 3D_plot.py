import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(low=1, high=100, size=100)
y = np.random.randint(low=1, high=100, size=100)
z = np.random.randint(low=1, high=100, size=100)

plt.figure(1)
ax = plt.axes(projection='3d')
ax.scatter(x, y, z)
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_zlabel('z label')
ax.set_title("3D Scatter Plot Projection")
plt.savefig('sample_3d_scatter.png')

plt.figure(2)
ax = plt.axes(projection='3d')
ax.plot(x, y, z)
ax.set_title("3D Line Chart Projection")

plt.show()
