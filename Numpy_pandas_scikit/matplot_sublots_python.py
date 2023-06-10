import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 10*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

#setup subplot

#first plot
plt.subplot(2,2,1)
plt.plot(x, y_sin)
plt.title('sine')

#Second plot
plt.subplot(2,2,2)
plt.plot(x, y_cos)
plt.title('cosine')

plt.show()