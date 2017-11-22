# Autor: Jose M Torres
# Adveccion

# Esta es la version adaptada para compilar en Cpython

# El dato inicial es un pulso gaussiano

# Se compila con
# > python setup_cy.py build_ext --inplace

import numpy as np
cimport numpy as np

cdef extern from "math.h":   # Se utiliza librería nativa
     double exp(double x)

# Parametros

N = 2000		      
cdef double dx = 0.05         # Se especifican tipos de dato estáticos
cdef double courant = 0.5     # 
cdef double dt = courant*dx   # 
Nt = 1500         
fout = 20         

cdef double x0 = 0.5*N*dx     
cdef double sig= 10.          
cdef double A = 1.0           

outfile=open('phi_cy.xl','w') 

# Arreglos

x = np.zeros((N), dtype=np.double)
phi = np.zeros((N), dtype=np.double)
phi_p = np.zeros((N), dtype=np.double)
phi_s = np.zeros((N), dtype=np.double)

for i in range(N):
    x[i]= i*dx
    phi[i]=A*exp( - ( (x[i]-x0) /sig)**2)

# Dato inicial
outfile.write('#t=0.0\n')
for i in range(N):
    outfile.write(str(x[i])+' '+str(phi[i])+'\n')
outfile.write('\n\n')


#  Ciclo de evolución
for i in range(1,Nt+1):
    phi_p[:]=phi

    # Interior
    for j in range(1,N-1):
        phi_s[j] = (-(phi_p[j+1]-phi_p[j-1])*0.5
		 +0.5*courant*(phi_p[j+1]-2.*phi_p[j]+phi_p[j-1])
		 )
        phi[j] = phi_p[j] + courant*phi_s[j]
    
    
    # Frontera
    phi[N-1] = phi_p[N-1] - courant*(phi_p[N-1]-phi_p[N-2])
    
    # output
    if not i%fout :
        outfile.write('#t='+str(i*dt)+'\n')
        for j in range(1,N-1):
            outfile.write(str(x[j])+' '+str(phi[j])+'\n')
        outfile.write('\n\n')

outfile.close()
print 'Done'
