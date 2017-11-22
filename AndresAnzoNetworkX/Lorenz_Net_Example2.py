from  mpl_toolkits.mplot3d import Axes3D
from  scipy.integrate      import odeint

import matplotlib.pyplot as plt
import networkx          as nx
import numpy             as np

# Number of nodes and connection probability
N = 10; p = 0.65

# coupling strength
c = 1.1

# Inner coupling matriz
Gamma  = [0,1,0] 

# The NetworX graph
G = nx.erdos_renyi_graph(N,p)

A = nx.to_numpy_matrix(G)
for i in range(N): A[i,i] = -G.degree(i)

print A

def Net_Lorenz(X,t,sigma=10.0,rho=28.0,beta=8.0/3.0):

    odes = []
    for i in range(N):
        sumaX = 0; sumaY = 0; sumaZ = 0
        for j in range(N):
                sumaX += A[i,j]*(X[3*j])
                sumaY += A[i,j]*(X[3*j + 1])
                sumaZ += A[i,j]*(X[3*j + 2])
                
        odes.append(sigma*(X[3*i+1] - X[3*i])            + c*Gamma[0]*sumaX)
        odes.append(X[3*i] * (rho - X[3*i+2]) - X[3*i+1] + c*Gamma[1]*sumaY )
        odes.append(X[3*i] * X[3*i+1] - beta*X[3*i+2]    + c*Gamma[2]*sumaZ )

    return odes

# Initial condition
z0 = [np.random.uniform(-40.0,40.0) for i in range(3*N)]

t  = np.arange(0.0, 100.0, 0.01)
Z  = odeint(Net_Lorenz,z0,t) 

# --------------------------> Plot <--------------------------------------

colors = plt.get_cmap('jet')(np.linspace(0, 1.0,N))

fig = plt.figure()
ax = Axes3D(fig)

# Plot format
fontsize  = 25
linewidth = 2
labelsize = 15
alpha     = 1.0

# Loop over the network nodes
for nodei in range(N):

    col = colors[nodei] 

    x1  = [xi[3*nodei]   for xi in Z]  
    x2  = [xi[3*nodei+1] for xi in Z]  
    x3  = [xi[3*nodei+2] for xi in Z]  
    
    plt.figure(101,figsize=(14,14))
    ax.set_xlabel('x axis',fontsize=16)
    ax.set_ylabel('y axis',fontsize=16)
    ax.set_zlabel('z axis',fontsize=16)

    ax.plot(x1,x2,x3,color = col)
    plt.savefig('m5_Lphase.jpg',bbox_inches='tight',dpi=1080)

    plt.figure(201,figsize=(8,7))
    plt.subplot(311)
    plt.plot(t,x1,color = col,linewidth=linewidth,alpha=alpha)
    plt.xlabel("$t$",fontsize=0.001)
    plt.ylabel("$x(t)$",fontsize=fontsize)
    plt.xlim(0.0,5.0)
    plt.axvline(linewidth=linewidth, color="black")
    plt.tick_params(axis='x', labelsize=0.001)
    plt.tick_params(axis='y', labelsize=labelsize)
    plt.yticks([-60,0,+60])

    plt.subplot(312)
    plt.plot(t,x2,color = col,linewidth=linewidth,alpha=alpha)
    plt.xlabel("$t$",fontsize=0.001)
    plt.ylabel("$y(t)$",fontsize=fontsize)
    plt.xlim(0.0,5.0)
    plt.axvline(linewidth=linewidth, color="black")
    plt.tick_params(axis='x', labelsize=0.001)
    plt.tick_params(axis='y', labelsize=labelsize)
    plt.yticks([-20,0,+20])

    plt.subplot(313)
    plt.plot(t,x3,color = col,linewidth=linewidth,alpha=alpha)
    plt.xlabel("$t$",fontsize=fontsize)
    plt.ylabel("$z(t)$",fontsize=fontsize)
    plt.xlim(0.0,5.0)
    plt.axvline(linewidth=linewidth, color="black")
    plt.tick_params(axis='x', labelsize=labelsize)
    plt.tick_params(axis='y', labelsize=labelsize)
    plt.yticks([-20,0,+20])

plt.savefig('TimeSeries.jpg',bbox_inches='tight',dpi=1080)


#for i in range(N):

#    j0 = 3*i; j1 = 3*i + 1; j2 = 3*i + 2

#    col = colors[i]
    
#    ax.set_xlabel('x1 axis',fontsize=16)
#    ax.set_ylabel('x2 axis',fontsize=16)
#    ax.set_zlabel('x3 axis',fontsize=16)

#    ax.plot(z[:,j0],z[:,j1],z[:,j2],color = col)
#    plt.savefig('m5_Lphase.png')

#    plt.figure(3)
#    plt.plot(t,z[:,j0],color = col)
#    plt.xlabel("$t$",fontsize=16)
#    plt.ylabel("$x_{1}$",fontsize=16)
#    plt.savefig('m5_Lx1.png')

#    plt.figure(4)
#    plt.plot(t,z[:,j1],color = col)
#    plt.xlabel("$t$",fontsize=16)
#    plt.ylabel("$x_{2}$",fontsize=16)
#    plt.savefig('m5_Lx2.png')

#    plt.figure(5)
#    plt.plot(t,z[:,j2],color = col)
#    plt.xlabel("$t$",fontsize=16)
#    plt.ylabel("$x_{3}$",fontsize=16)
#    plt.savefig('m5_Lx3.png')

#plt.show()





