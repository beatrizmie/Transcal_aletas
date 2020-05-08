import numpy as np
from matplotlib import pyplot as plt

#1. Determinar as dimensões da aleta
#2. Determinar as taxas de transferência de calor
#3. Determinar a distribuição de temperatura ao longo da aleta
#4. Iniciamos fazendo um balanço de energia em um elemento diferencial apropriado

Ac = 0.03**2
L = 0.3

k = 200
h = 15
P = 4*0.03

m = np.sqrt((h*P)/(k*Ac))

x = np.linspace(0, L, 100)

T_inf = 300
T_base = 350
theta_base = T_base - T_inf

temp = []

for i in x:
    a = np.cosh(m*(L-i)) + h/(m*k) * np.sinh(m*(L-i))
    b = np.cosh(m*L) + h/(m*k) * np.sinh(m*L)
    theta = a/b * theta_base
    temp.append(theta + T_inf)
    print(theta + T_inf)
    
print(((np.cosh(m*(L/2)) + h/(m*k) * np.sinh(m*(L/2))) / (np.cosh(m*L) + h/(m*k) * np.sinh(m*L)) * theta_base) + T_inf)

plt.plot(x, temp, label='temperatura')
plt.show()