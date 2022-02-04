# Exercício extra 4 - maximizar lucro
# obter o preço que maximiza o lucro e o lucro respectivo   #Otimização do lucro normalmente se resolve com derivada = o
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x, L, f = symbols('x L f')
L = -2*x**2+7000*x-12000
df = diff(L, x)  # derivada primeira
p = solve(Eq(df, 0))  # fazendo a derivada ser igual a 0
Lucro = L.subs(x, p[0])  # substituindo x na função L
print('Melhor Preço: ', p[0])
print('Lucro maximizado: ', Lucro)


f = -2*x**5+23*x**3-7*x
init_printing()
print(diff(f, x, 2))  # derivada segunda, derivar 2 vezes.


x = np.linspace(0, 10, 10000)
f = 3 * np.sin(x) + 2*x**3
plt.plot(x, f)
plt.show()

