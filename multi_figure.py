import matplotlib.pyplot as plt
import random
from matplotlib import style

# style.use('ggplot')
style.use('dark_background')

x1 = [random.randint(1, 20) for i in range(30)]
x2 = [random.randint(45, 67) for i in range(30)]

plt.figure(1)
plt.plot(x1)

plt.figure(2)
plt.plot(x2)

plt.show()
