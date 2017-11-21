

# Autor: Jose M Torres
# Adveccion

# Este programa resuelve la ecuacion de adveccion en una dimension
# usando un metodo de diferencias finitas

# El dato inicial es un pulso gaussiano

import numpy as np
import math


# Parametros

N = 2000          # Numero de puntos de la malla
dx = 0.05         # Intervalo espacial
courant = 0.5     # Parametro de courant dt/dx
dt = courant*dx   # Paso de tiempo
Nt = 1500         # Total de iteraciones
fout = 20         # Frecuencia de salida

x0 = 0.5*N*dx     # Localizacion del pulso gaussiano
sig= 10.           # Ancho del pulso
A = 1.0           # Amplitud del pulso


outfile=open('phi_num.xl','w') # Nombre del archivo de salida

#define arrays and initialize
x = np.linspace(0,(N-1)*dx,N)
phi = np.zeros(N)
phi_p = np.zeros(N)
phi_s = np.zeros(N)

for i in range(N):
    phi[i]=A*math.exp( - ( (x[i]-x0) /sig)**2)

# write initial data
outfile.write('#t=0.0\n')
for i in range(1,N-1):
    outfile.write(str(x[i])+' '+str(phi[i])+'\n')
outfile.write('\n\n')


# Loop
for i in range(1,Nt+1):
    phi_p[:]=phi

    #inner
    for j in range(1,N-1):
        phi_s[j] = (-(phi_p[j+1]-phi_p[j-1])*0.5
		 +0.5*courant*(phi_p[j+1]-2.*phi_p[j]+phi_p[j-1])
		 )
        phi[j] = phi_p[j] + courant*phi_s[j]
    
    
    #boundaries
    phi[N-1] = phi_p[N-1] - courant*(phi_p[N-1]-phi_p[N-2])
    
    # output
    if not i%fout :
        outfile.write('#t='+str(i*dt)+'\n')
        for j in range(1,N-1):
            outfile.write(str(x[j])+' '+str(phi[j])+'\n')
        outfile.write('\n\n')

outfile.close()
print 'Done'
