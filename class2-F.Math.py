# Practical activity 2
# Class 2
# Paulo Pinheiro

from sympy import *

# Question 1

""" def profit(marg):
    return (marg + 11500)/(300 * 0.725)

num = float(input('Digite: '))
print(profit(num)) """

# Question 2

# Expand the expression
x, y = symbols("x y")
init_printing()
print(expand((5*x + 3*y + 2*x*y)**3))

# Question 3

# Factor the expression shown:
print(factor(2*x**2*y**3 + 6*x**5*y**4 - 15*x**2*y**4))

# Question 4

# Profit from a meat company based on market price. Price is 22.00, profit is?

y = (- 120*x**2 + 4800*x)
y.subs(x,22)