import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
t = np.arange(0,50,0.01)

def lissajous(i,n=1.5,a=5,b=5,c=0):

    def lissajous_x(t,n=n,a=a,c=c):
        return a*np.sin(n*t+c)

    def lissajous_y(t,b=b):
        return b*np.sin(t)

    yield lissajous_x(i),lissajous_y(i)

def update(rotation):
    plt.clf()
    out = list(lissajous(t,c=rotation*10))[0]
    plt.plot(out[1],out[0])

anim = FuncAnimation(fig,update,frames=t)
#anim.save("lissajous_anim_n=1,666.gif",fps=120)
plt.show()
