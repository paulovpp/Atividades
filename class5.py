import numpy as np

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

# Class example 2 - Inner and cross products

sist_A = np.array([[4, 2, -1],[3, 3, 2],[0, 5, 2]]) # array of coefficients
sist_b = np.array([[7], [20], [-1]])  # constants
sol = np.linalg.solve(sist_A, sist_b)
print(sol)