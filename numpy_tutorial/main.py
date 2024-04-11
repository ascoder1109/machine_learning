import numpy as np

# Create 1D Array
a = np.array([1, 2, 3, 4, 5], dtype='int32')
print(a)

# Create 2D Array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# Get number of dimensions
print("Number of dimension of a array:", a.ndim)

# Get the shape of an array
print("Size of array b:", b.shape)

# Type of array
print("Type of array:", a.dtype)

a1 = np.array([[1, 2, 3, 4, 5, 6, 7],
               [8, 9, 10, 11, 12, 13, 14]])
print(a1)

# Get a specific element [r,c]
print(a1[1, 5])

zeroArray = np.zeros((3, 4))
print(zeroArray)

oneArray = np.ones((3, 4))
print(oneArray)

nineArray = np.full((3, 4), 9)
print(nineArray)

# Random number array
randomArray = np.random.rand(3, 4)
print(randomArray)

integerRandomArray = np.random.randint(7, size=(3, 3))
print(integerRandomArray)

# Identity Matrix
identityMatrix = np.identity(5)
print(identityMatrix)

output = np.ones((5, 5))
print(output)

z = np.zeros((3, 3))
print(z)
z[1, 1] = 9

print(z)

output[1:4, 1:4] = z
print(output)

copyOfa = np.copy(a)
print(copyOfa)

a += 2
print(a)

########## Linear Algebra
aArray = np.ones((2,3))
print(a)

bArray = np.full((3,2),2)
print(bArray)

print(np.matmul(aArray, bArray))

c = np.identity(3)
print(np.linalg.det(c))

########## Statistics

stats = np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats))
print(np.max(stats, axis=1))

print(np.max(stats))

print(stats.mean())

####### Reorganising Arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((4,2))
print(after)


