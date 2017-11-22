import numpy as np

def TwoPatch(y,param,p11,p22i): 
# return derivatives of the patch with parameters param
   S = y[0]
   E = y[1]
   I = y[2]
   R = y[3]
   Sv = y[4]
   Ev = y[5]
   Iv = y[6]
   
   S2 = y[7]
   E2 = y[8]
   I2 = y[9]
   R2 = y[10]
   Sv2 = y[11]
   Ev2 = y[12]
   Iv2 = y[13]
   
   Cum = y[14]
   Cum2 = y[15]
   
   N = S + E + I + R
   N2 = S2 + E2 + I2 + R2
   Nv = Sv + Ev + Iv
   Nv2 = Sv2 + Ev2 + Iv2
   if(p22i>1.0):
		p22 = 1.0
   else:
		p22 = p22i
   p12 = (1.0 - p11)
   p21 = (1.0 - p22)
   Neff1 = p11*N + p21*N2
   Neff2 = p12*N + p22*N2
   
   mu = param[0] 
   beta = param[1]
   a = param[2]
   nu = param[3]
   gamma = param[4]
   muv = param[5]
   nuv = param[6]
   delta = param[7]
   q = param[8]
   
   mu2 = param[12]
   beta2 = param[13]
   a2 = param[14]
   nu2 = param[15]
   gamma2 = param[16]
   muv2 = param[17]
   nuv2 = param[18]
   delta2 = param[19]
   q2 = param[20]
   
   dS = mu*N - a*p11*beta*S*Iv/Neff1 - mu*S - p12*beta*a2*S*Iv2/Neff2
   dE = a*p11*beta*S*Iv/Neff1 - (mu + nu)*E + p12*beta*a2*S*Iv2/Neff2
   dI = nu*E - (mu + gamma)*I
   dR = gamma*I - mu*R
   dSv = muv*(Nv - q*Iv) - p11*a*beta*Sv*I/Neff1 - (muv + delta)*Sv - p21*a*beta*Sv*I2/Neff1
   dEv = p11*a*beta*Sv*I/Neff1  - (nuv + muv)*Ev + p21*a*beta*Sv*I2/Neff1
   dIv = nuv*Ev + q*muv*Iv - nuv*Iv
   dCum = nu*E
   
   dS2 = mu2*N2 - p22*a2*beta*S2*Iv2/Neff2 - mu2*S2 - p21*beta*a*S2*Iv/Neff1
   dE2 = p22*a2*beta*S2*Iv2/Neff2 - (mu2 + nu2)*E2  + p21*beta*a*S2*Iv/Neff1
   dI2 = nu2*E2 - (mu2 + gamma2)*I2
   dR2 = gamma2*I2 - mu2*R2
   dSv2 = muv2*(Nv2 - q2*Iv2) - p22*a2*beta*Sv2*I2/Neff2 - (muv2 + delta2)*Sv2 - p12*a2*beta*Sv2*I/Neff2
   dEv2 = p22*a2*beta*Sv2*I2/Neff2 - (nuv2 + muv2)*Ev2 + p12*a2*beta*Sv2*I/Neff2
   dIv2 = nuv2*Ev2 - nuv2*Iv2 + q2*muv2*Iv2
   dCum2 = nu2*E2
   return np.array([ dS, dE, dI, dR, dSv, dEv, dIv, dS2, dE2, dI2, dR2, dSv2, dEv2, dIv2 , dCum, dCum2])
   
