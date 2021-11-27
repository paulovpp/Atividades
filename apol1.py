from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x, y = symbols("x y")
init_printing()
y = (- 7 * x ** 2 + 5200 * x - 80000)
print(y.subs(x, 350))
print()


R, C = symbols('R C')
R = 511 * x
C = 392 * x + 22500
xp = solve(Eq(R, C), x)
yp = R.subs(x, xp[0])
print(float(xp[0]))
print()

R, C = symbols('R C')
R = 314 * x
C = 179 * x + 10530
xp = solve(Eq(R, C), x)
yp = R.subs(x, xp[0])
print(float(xp[0]))
print()

x, y = symbols("x y")
init_printing()

print(expand((2*x + y)**3))
print()

print(factor(x**2*y**5 + 3*x**3*y**4 - x**3*y**6))
print()
