import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
t = np.arange(0,100,0.05)

def lissajous(t=t,n=1.5,a=5,b=5,c=0):
    x = []
    y = []
    
    def lissajous_x(t,n=n,a=a,c=c):
        return a*np.sin(n*t+c)

    def lissajous_y(t,b=b):
        return b*np.sin(t)
    
    for i in t:
        x.append(lissajous_x(i))
        y.append(lissajous_y(i))
    
    p = np.array((x,y))
    #plt.plot(p[1],p[0])   #np.array((x,y))
    return p

data = lissajous()
anim = FuncAnimation(fig, lissajous)
#plt.show()

#lissajous()
plt.show()