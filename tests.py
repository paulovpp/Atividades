from sympy import *
# import numpy as np
# import matplotlib.pyplot as plt

x, y = symbols("x y")
init_printing()

y = x**5 + x**3 - x**2
print(diff(y, x, 3))
