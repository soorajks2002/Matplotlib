import matplotlib.pyplot as plt
import random

language = ["python", "c++", "java", "javascript", "dart", "mojo"]
users = []

for i in range(len(language)):
    users.append(random.randint(25, 150))

plt.bar(language, users)

plt.bar(x=language, height=users, color='black')

plt.bar(x=language, height=users, align='edge')

plt.bar(x=language, height=users, width=0.2)

plt.bar(x=language, height=users, color='black', width=0.5, edgecolor='red')

plt.bar(x=language, height=users, color='black', width=0.5, edgecolor='red', lw=5)

plt.bar(x=language, height=users, alpha=0.5)

plt.show()