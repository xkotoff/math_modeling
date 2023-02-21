import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01)

y = 0.01
omega = 0.05
z = y, omega

def diffunc(z, x):
    y, omega = z

    dy_dx = omega

    domega_dx = np.sin(y) * omega - 3 * x * omega - 5

    return dy_dx, domega_dx

y0 = np.pi - 0.1
omega0 = 0

z0 = y0, omega0


sol = odeint(diffunc, z0, x)

plt.plot(x, sol[:, 1], 'b', label='theta(x)') 

plt.legend()
plt.savefig('pic1.png')






