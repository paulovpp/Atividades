# Activity examples
# Class 2
# Paulo Pinheiro

from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# Question 1
# Calculate the profit

""" def profit(marg):
    return (marg + 11500)/(300 * 0.725)

num = float(input('Digite: '))
print(profit(num)) """

# Question 2
# Expand the expression

x, y = symbols("x y")
init_printing()
print(expand((5 * x + 3 * y + 2 * x * y) ** 3))

# Question 3
# Factor the expression shown:

print(factor(2 * x ** 2 * y ** 3 + 6 * x ** 5 * y ** 4 - 15 * x ** 2 * y ** 4))
print()

# Question 4
# Profit from a meat company based on market price. Price is 22.00, profit is?

y = (- 120 * x ** 2 + 4800 * x)
print(y.subs(x, 22))
print()

# Question 5
# Find the coordinates of a candidate

coef = [-0.8, 0.8, 0]
print(np.roots(coef))
print()

# Question 6
# Find the roots for a profit function

coef1 = [-2, 400, -15000]
print(np.roots(coef1))
print()

# Question 7
# Find the length of a bump

coef2 = [-0.5, 0.75, 0]
len = np.roots(coef2)
print('The length of the bump is: ', len[0] - len[1], 'm')
print()

# Question 8
# Find the equilibrium point between revenue and expense

R, C = symbols('R C')
R = 555 * x
C = 215 * x + 22500

# Eq function: equals both arguments
xp = solve(Eq(R, C), x)
yp = R.subs(x, xp[0])
print(float(xp[0]))
print(float(yp))

# Question 9
# Plot two functions a and b

x = np.linspace(0,100,100)
a = 0.99 * x + 19.90
b = 0.79 * x + 29.90
plt.plot(x, a)
plt.plot(x, b)
plt.show()
