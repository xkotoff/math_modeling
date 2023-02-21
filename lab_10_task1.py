import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def difffunc(k, x):
    y, z = k

    dy_dx = y**2 * z

    dz_dx = z / x - y * z**2

    return dy_dx, dz_dx

y0 = 1
z0 = -3

k0 = y0, z0


sol = odeint(difffunc, k0, x)

plt.plot(x, sol[:, 1], 'b', label='theta(x)') 

plt.legend()
plt.savefig('pic1.png')





