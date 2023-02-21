import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01)

def difunc(z, t):
    x, y = z

    dx_dt = 3 * x - 2 * y + (np.exp(3*t)) / (np.exp(t) + 1)

    dy_dt = x - (np.exp(3*t)) / (np.exp(t) + 1)
    
    return dx_dt, dy_dt

x0 = 5
y0 = -7

z0 = x0, y0

sol = odeint(difunc, z0, x)

plt.plot(x, sol[:, 1], 'b', label='theta(x)') 

plt.legend()
plt.savefig('pic1.png')


