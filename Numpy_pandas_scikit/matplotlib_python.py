import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1,100)
y = 2 * x^2 + 3*x + 5

plt.title("matplot Demo")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y)
plt.show()