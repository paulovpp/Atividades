import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.interpolate import *

# Linear regression
# Class example 1 - Linear regression with plotted line

# months = np.array([1, 2, 3, 4])
# production = np.array([5000, 5300, 5200, 5500])
# a, b, correlation1, p, error = stats.linregress(months, production)

# print('Linear regression equation: y = %.2fx + %.2f'%(a, b))
# print('Correlation coefficient: r = %.2f'% correlation1)

# plt.plot(months, production, 'o', label = 'Original data')
# f = a * months + b
# plt.plot(months, f, 'r', label = 'Regression line')
# plt.ylim(4900, 5600)
# plt.legend()
# plt.show()


# Interpolation
# Construction interpolation

x = [0, 10, 20]
y = [0, 7, 0]
f = interp1d(x, y, kind='quadratic')
xi = np.linspace(0, 20, 100)
yi = f(xi)
plt.plot(x, y, 'o')
plt.plot(xi, yi)
# plt.show()
g = lagrange(x, y)  # find the function of the interpolation
print(g)