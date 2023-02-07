import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
g = 6.67 * 10**-11
R = 6400000
h = 50 * R
r = np.arange(h+R, R, -1000)
def finc_meteo(v, r):
    dvdr = -G * M / (v * r**2)
    return dvdr

G = 6.67 * 10**(-11)
M = 6 * 20 ** 24
v0 = 1
v_r = odeint(finc_meteo, v0, r)

plt.plot(r, v_r[:, 0])
plt.savefig('meteo.png')
