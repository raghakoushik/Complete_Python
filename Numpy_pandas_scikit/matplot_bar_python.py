from matplotlib import pyplot as plt

x1 = [2,5,8,10]
y1 = [7,12,16,6]

x2 = [3,6,9,11]
y2 = [8,6,15,7]

plt.bar(x1, y1)
plt.bar(x2, y2, color = 'r')
plt.title("Bar graph")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.show()