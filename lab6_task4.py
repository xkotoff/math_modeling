import matplotlib.pyplot as plt
import numpy as np

def spiral(k=0.1):
    f = np.arange(0, 8*np.pi, 0.1)
    r = k*f
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x, y, color='purple', label='my spiral')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.legend()
    plt.savefig('pig_png')
spiral()




