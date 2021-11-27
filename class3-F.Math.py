# Classes examples
# Class 3
# Paulo Pinheiro

import matplotlib.pyplot as plt
import numpy as np


# Line chart plot
x_axis = ['Mar', 'Apr', 'May', 'Jun', 'Jul']
y_axis = [35000, 29000, 27000, 32000, 33000]

plt.subplot(1, 2, 1)
plt.plot(x_axis, y_axis, 'b', linewidth=2)
plt.plot(x_axis, y_axis, 'r o')
plt.ylim(0, 40000)
plt.title('Mar to Jul production')
plt.xlabel('Months')
plt.ylabel('Production')
# plt.show()

# Bar chart plot

year = ['2014', '2015', '2016', '2017', '2018']
x = np.arange(5)
y1 = [7, 2, 5, 4, 1]
y2 = [32, 21, 17, 22, 13]
largura = 0.3
plt.subplot(1, 2, 2)
plt.bar(x, y1, largura, color='r')
plt.bar(x+largura, y2, largura, color='c')
plt.xticks(x, year)
plt.title('Afastamentos por acidentes e por doenças')
plt.xlabel('Ano')
plt.ylabel('Afastamentos')
plt.legend(['Acidentes', 'Doenças'], loc=1)
plt.show()

x = [132, 89, 115]
quartos = ['1 quarto', '2 quartos', '3 quartos']
cores = ['r', 'm', 'y']
plt.axis('equal')
plt.subplot(1, 2, 1)
plt.pie(x, labels=quartos, colors=cores, shadow=True, autopct='%1.1f%%')
plt.title('Vendas dos apartamentos')
# plt.show()

x = [132, 89, 115]
quartos = ['1 quarto', '2 quartos', '3 quartos']
cores = ['r', 'm', 'y']
plt.axis('equal')
plt.pie(x, labels=quartos, colors=cores, shadow=True, explode=(0.1, 0, 0), autopct='%1.1f%%')
plt.title('Vendas dos apartamentos')
plt.show()
