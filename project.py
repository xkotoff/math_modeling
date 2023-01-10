import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='black', label='Ball')
 
def circle_move(R, vx0, vy0, time):
    x0 = 0
    y0 = -vy0 * time

    if y0 >= -1.72:
        alpha = np.arange(0, 2*np.pi, 0.1)
        x = x0 + R*np.cos(alpha)
        y = y0 + R*np.sin(alpha)
    else:
        x0 = 0
        y0 = -1.72
        alpha = np.arange(0, 2*np.pi, 0.1)
        x = x0 + 1.1 * R*np.cos(alpha)
        y = y0 + R*np.sin(alpha)
    return x, y
 
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animate(i):
    ball.set_data(circle_move(R=0.5, vx0=0.05, vy0=0.05, time=i))
    
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=100,
                              interval=40
                             )
 
ani.save('lec_7_complex_animation.gif')
