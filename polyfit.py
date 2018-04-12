import numpy as np
import matplotlib.pyplot as plt

from numpy.polynomial import polynomial as P

x = np.linspace(0,1,51)
print(x)
#y = x**3 - x + (np.random.randn(len(x)) / 10)
y = x**2
print(y)

c, stats = P.polyfit(x,y,3,full=True)
yt = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3

#c, stats = P.polyfit(x,y,2,full=True)
#yt = c[0] + c[1]*x + c[2]*x**2

plt.figure(1)
plt.subplot(211)
plt.plot(x, y)

plt.subplot(212)
plt.plot(x, yt)
plt.show()
