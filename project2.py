import matplotlib.pyplot as plt
import numpy as np

def ellips(a=5, b =3):
 X, Y = np.meshgrid(x, y)
 x = np.arange (-2 * a, 2 * a, 0.1)
 y = np.arange (-2 * a, 2 * a, 0.1)

 fxy = X**2 / a**2 + Y**2 / b**2 - 1
 plt.contour(X, Y, fxy, levels=[0])
 plt.axis('equal')
 plt.savefig('pic_1.png')
ellips()