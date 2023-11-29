import numpy as np

a = np.array([0, 1, 2, 3, 4, 5])
'''
print(a)
print(a.dtype) # Check the type of the values stored in numpy array
print(type(a))
print(a.size)

# Slicing
b = a[1:5]
print(b)
b[2:4] = 100, 200
print(b)


arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[0:6:2])  # define steps in slicing [start:end:step]


# use a list to select more than one specific index
c = np.array([20, 1, 2, 3, 4])
select = [0, 2, 3,4]
d = c[select]

print(d)
print(c.size)
print(c.ndim) # Get the number of dimensions of numpy array
print(c.shape) # Get the shape/size of numpy array as a tuple of integers

# Numpy statistical functions
e = np.array([1, -1, 1, -1])
mean = e.mean()
print(mean)

standard_deviation = a.std()
print(standard_deviation)

max_e = e.max()
print(max_e)



# Numpy Array Operations
# Addition
u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u, v)
print(z)

# Subtraction
a = np.array([10, 20, 30])
b = np.array([5,10, 15])
c = np.subtract(a, b)
print(c)

# Multiply
x = np.array([1, 2])
y = np.array([2, 1])
z = np.multiply(x, y)
print(z)

# Division
a = np.array([10, 20, 30])
b = np.array([2, 10, 5])
c = np.divide(a, b)
print(c)

# Dot Product
x = np.array([1, 2])
y = np.array([3, 2])
z = np.dot(x, y)
print(z)

# Adding constant to a numpy array
u = np.array([1, 2, 3, -1])
print(u+1)

# Linspace
# Makeup a numpy array within [-2, 2] and 5 elements
a=np.linspace(-2, 2, 9)
print(a)


# Iterating 1-D arrays
arr1 = np.array([1, 2, 3])
for x in arr1:
    print(x)
'''
