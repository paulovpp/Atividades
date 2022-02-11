from filecmp import cmp
import sys
import numpy as np
from sympy import comp

# Class example 1 - Convert dollars into reais

# tab1 = np.array([[5.90, 7.10],[2.38, 2.52],[2.90, 2.00]])
# tab_res = tab1 * 4.10
# print(tab_res)


# Class example 2 - Inner and cross products

# u = np.array([3, -5, 2])
# v = np.array([4, 6, 3])
# uv_inner = np.inner(u, v)
# uv_cross = np.cross(u, v)

# print(uv_inner)
# print(uv_cross)


# Linear systems
# Class example 2 - Inner and cross products

# sys_A = np.array([[4, 2, -1],[3, 3, 2],[0, 5, 2]]) # array of coefficients
# sys_b = np.array([[7], [20], [-1]])  # constants
# sol = np.linalg.solve(sys_A, sys_b)
# print(sol)


# Class example 3 - Simple linear system

# sys_c = np.array([[1, 3, 4],[2, -1, 1],[-4, 2, -2]])
# sys_c_const = np.array([[18], [10], [-7]])
# sol_c = np.linalg.solve(sys_c, sys_c_const)
# print(sol_c)
# Error because the matrix is singular


# Class example 4 - Boxes and pallets

# sys_d = np.array([[10, 120],[8, 80]])
# sys_d_const = np.array([[844], [576]])
# sol_d = np.linalg.solve(sys_d, sys_d_const)
# print(sol_d)


# Trigonometric functions
# Class example 5 - Trigonometric simple functions

# arc_1 = np.deg2rad(57)
# print(np.sin(arc_1))

# arc_2 = np.rad2deg(np.arccos(0.7))
# print(arc_2)


# Complex numbers
# Numerical sets
# Class example 7 - Write a complex number in python
# z1 = 3 + 5j
# z1 = complex(3, 5)
# print(z1)

# Module of a complex number
# print(abs(z1))

# Operations with complex numbers
# z2 = complex(7, -3)
# sum = z1 + z2
# prod = z1 * z2
# division = z1 / z2
# print(sum)
# print(prod)
# print(division)


# Linear systems with complex numbers
# Solve a simple linear system

# c1 = complex(2, 1)
# c2 = complex(5, -1)
# c3 = complex(7, 4)
# c4 = complex(3, 8)
# c5 = complex(2, 5)

# cmpl_a = np.array([[c1, c2], [c2, c3]])
# cmpl_b = np.array([[c4],[c5]])
# cmpl_sol_1 = np.linalg.solve(cmpl_a, cmpl_b)
# print(cmpl_sol_1)

# Solve a linear system with complex numbers

# (3 + 2j)a + (-2 - 6j)b = 70|_ 0 deg
# (-2 - 6j)a + (10 + j)b = 110|_ 0 deg

# r1 = 70
# r2 = 110
# theta_1 = np.deg2rad(0)
# theta_2 = np.deg2rad(30)
# c1 = complex(3, 2)
# c2 = complex(-2, -6)
# c3 = complex(10, 1)
# c4 = complex(r1 * np.cos(theta_1), r1 * np.sin(theta_1))
# c5 = complex(r2 * np.cos(theta_2), r2 * np.sin(theta_2))

# cmpl_sys_a = np.array([[c1, c2], [c2, c3]])
# cmpl_sys_b = np.array([[c4],[c5]])
# cmpl_sol_1 = np.linalg.solve(cmpl_sys_a, cmpl_sys_b)
# print(cmpl_sol_1)


# Problem from the text 
# 1.7 Example 7 - Matrices and vectors

badges = np.array([[3, 1, 3], [6, 5, 5]])
shirts = np.array([[100, 50], [50, 100], [50, 50]])
result = np.matmul(badges, shirts)
print(result)
