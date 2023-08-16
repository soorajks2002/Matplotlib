import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('seaborn-v0_8-dark')

x = np.random.randint(low=1, high=100, size=50)

plt.plot(x)
plt.savefig("sample_plot.png", dpi=300, transparent=False)
# plt.show()
