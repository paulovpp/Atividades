from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x, y = symbols("x y")
init_printing()

print(factor(x**2*y**5 + 3*x**3*y**4 - x**3*y**6))
print()
