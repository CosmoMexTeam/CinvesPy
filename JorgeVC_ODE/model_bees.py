import numpy as np

def NoPolicy(y,param): 
# return derivatives of the patch with parameters param
    W = y[0]
    A = y[1]
    N = W + A

    b = param[0]
    d = param[1]
    mu = param[2]
    alpha = param[3]
   
    dW = b*W + d*A - mu*N*W - alpha*N*W
    dA = alpha*N*W - mu*N*A
    
    return np.array([ dW, dA])

def Policy(y,param): #Deprecate!!!
# return derivatives of the patch with parameters param
    W = y[0]
    A = y[1]
    N = W + A

    b = param[0]
    d = param[1]
    mu = param[2]
    alpha = param[3]
    rho = param[4]
   
    dW = b*W + d*A - mu*N*W - alpha*N*W - d*A/(1.0 + rho * W)
    dA = alpha*N*W - mu*N*A
    
    return np.array([ dW, dA])

def Complete(y,param): 
# return derivatives of the patch with parameters param
    W = y[0]
    A = y[1]
    N = W + A

    rho = param[4]
    b = param[0]
    d = param[1]
    mu = param[2]
    alpha = param[3]
    gamma = 0.1
   
    dW = b*(1.0-rho)*W + b*d*A - mu*N*W - alpha*N*W - gamma*A*W/(1.0 + rho*W)
    dA = alpha*N*W - mu*N*A
    
    return np.array([ dW, dA])
    
def BeneficialPolicy(y,param):
    W = y[0]
    A = y[1]
    N = W + A

    rho = param[4]
    b = param[0]
    d = param[1]
    mu = param[2]
    alpha = param[3]
    gamma = 0.1
   
    dW = b*W + param[0]*d*A - mu*N*W - alpha*N*W - gamma*A*W/(1.0 + rho*W)
    dA = alpha*N*W - mu*N*A
    
    return np.array([ dW, dA])

def lotka(y,param):
    W = y[0]
    A = y[1]
    N = W + A

    b = param[0]
    d = param[1]
    mu = param[2]
    alpha = param[3]
   
    dW = (1.0 - A)*W
    dA = 0.1*(W - 1.0)*A
    
    return np.array([ dW, dA])
