import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('dark_background')

fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.add_subplot(1,1,1)

N=2000
Nt = 1500
fout=20
dx= 0.05

output = np.loadtxt('phi_num.xl')
steps = Nt/fout

k=0

def animate(i):
    global k
    fx = output[N*k:N*(k+1)-1,1]
    x = output[N*k:N*(k+1)-1,0]
    k += 1
    ax1.clear()
    plt.plot(x,fx,color='cyan')
    plt.grid(True)
    plt.ylim([-1,1])
    plt.xlim([0,N*dx])

anim = animation.FuncAnimation(fig,animate,frames=360,interval=20)
plt.show()
#plt.plot(output[N*k:N*(k+1)-1,0],output[N*k:N*(k+1)-1,1],marker='x',color='g')
