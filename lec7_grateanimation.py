import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots() #создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2) #обьект анимации

xdata, ydata = [], [] #координаты анимации

ax.set_xlim(0, 2*np.pi) #пределы изменения х
ax.set_ylim(-1, 1) #пределы изменения у

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    anim_object.set_data(xdata, ydata)
    return anim_object,
ani = FuncAnimation(fig, update, frames=np.arange(0, 2*np.pi, 0.1), interval=100)
ani.save('lec7_grateanimation.gif')
