import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

# NumPy has a powerful N-dimensional array object (numpy.ndarray):
x = np.linspace(0, 1, 51)
print(x)

y = x**3 - x + (np.random.randn(len(x)) / 10)
print(y)

# NumPy can do least-squares fit of a polynomial to data:
c, stats = poly.polyfit(x, y, 3, full=True)
yt = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3

# Matplotlib can easily plot:
plt.figure(1)
plt.subplot(211)
plt.plot(x, y)
plt.subplot(212)
plt.plot(x, yt)
plt.show()
