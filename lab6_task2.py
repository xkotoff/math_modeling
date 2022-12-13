import matplotlib.pyplot as plt
import numpy as np

def giperbola_plotter(k=1, title='giperbola plotter'):

 x = np.arange(0.1, 10,0.1)
 y = k/x

 x1= np.arange(-0.1, -10, -0.1)
 y1= k/x1

 plt.plot(x, y, color='red', label='my giperbola')
 plt.plot(x1, y1, color='blue', label='my giperbola1')
 plt.xlabel('coord - x')
 plt.ylabel('coord - y')
 plt.xlabel('coord - x1')
 plt.ylabel('coord - y1')
 plt.title(title)
 plt.legend()
 plt.savefig('pig_png')
giperbola_plotter()