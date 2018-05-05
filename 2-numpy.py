import numpy as np

# NumPy is the fundamental package for scientific computing with Python.
# It has a powerful N-dimensional array object (numpy.ndarray):
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.size)
print(type(a))

ones = np.ones((2, 3), dtype=np.int16)
print(ones)

print(np.arange(0, 2, 0.25))  # floating point precision is finite
print(np.linspace(0, 2, 9))  # better

# Financial: mortgage payment
print(np.pmt(.04 / 12, 360, 1000000))

# Linear Algebra: solve the system of equations 3 * x0 + x1 = 9 and x0 + 2 * x1 = 8
e1 = np.array([[3, 1], [1, 2]])
e2 = np.array([9, 8])
print(np.linalg.solve(e1, e2))

# More here: https://docs.scipy.org/doc/numpy/user/quickstart.html
