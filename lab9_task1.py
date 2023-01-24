import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(5, 100, 0.01)

def bact_function(c, t):
    dmdt = k * c
    return dmdt
c_t = 10
k = 1 / 15 

c_t = odeint(bact_function, c_t, t)

plt.plot(t, c_t[:,0], label='Размножение бактерий')
plt.xlabel('Период распада, секунды')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.legend()

plt.savefig('bact.png')