import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
t = np.arange(0,50,0.05)

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
    
    return np.array((x,y))

def update(rotation):
    plt.clf()
    frame = a = lissajous(n=1+4/6,c=rotation/20)
    plt.plot(a[1], a[0])

anim = FuncAnimation(fig,update)
#plt.show()
#anim.save("lissajous_anim_n=1,666.gif",fps=120)