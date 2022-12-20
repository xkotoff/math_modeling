''''''''''
import matplotlib.pyplot as plt
import numpy as np
 
time = np.arange(-2*np.pi, 2*np.pi, 0.1) #ПАРАМЕТР
R = 3

x =  R * (time - np.sin(time))
y =  R * (1 - np.cos(time))

plt.plot(x, y, ls = '--', lw = 3)

plt.axis('equal')
 
plt.savefig('pig_png')
'''''''''''

import matplotlib.pyplot as plt
import numpy as np
 
time = np.arange(-2*np.pi, 2*np.pi, 0.1) #ПАРАМЕТР
R = 3

x = R * np.cos(time)**3
y = R * np.sin(time)**3

plt.plot(x, y, ls = '--', lw = 3)

plt.axis('equal')
 
plt.savefig('pig_png')





