import numpy as np

a = np.array([1,2,3])   # 1D array
print("Example of 1D array", a)

b = np.array([[1,2],[3,4]])
print("Example of 2D array", b)

c = np.array([1,2,3,4,5], dtype = 'complex')
print("Array of complex numbers", c)

d = np.array([[1,2,3],[4,5,6]])
print("The dimensions of the array is : ",d.shape)

d.shape=(3,2)
print("the transpose array elements are :",d)

e = d.reshape(3,2)
print("the reshaped array elements are :",e)


#one D array
f = np.arange(24)
f.ndim
print(f)

#now reshape it to 3d array

g = f.reshape(2,4,3)
print(g)


#use of dtype

h = np.empty([3, 2, 4], dtype=int)

print("The 3D array is given by : ",h)


#ones and zeros
i = np.ones(3); j = np.zeros(3)
k = np.ones([4,4], dtype=float); l = np.zeros([4,4], dtype=float)

print("Single dimension of ones and zeros is given by :", i,j)
print("Multi dimension of ones and zeros is given by :", k,l)


x = np.linspace(10, 20, 5)
y = np.linspace(10, 20, 10, retstep=False)

print(x)
print(y)
