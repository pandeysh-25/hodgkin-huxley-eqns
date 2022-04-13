#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: shashankpandey

"""
import numpy as np
import math
from matplotlib.pylab import *


def HodgkHux(I0,T0):
    dt = 0.01; # differential time(suitably small)
    T  = math.ceil(T0/dt)
    gNa0 = 120   # [mS/cm^2]
    ENa  = 115;  # [mV]
    gK0  = 36;   # [mS/cm^2]
    EK   = -12;  # [mV]
    gL0  = 0.3;  # [mS/cm^2]
    EL   = 10.6; # [mV]

    t = np.arange(0,T)*dt
    V = np.zeros([T,1])
    m = np.zeros([T,1])
    h = np.zeros([T,1])
    n = np.zeros([T,1])

    V[0]=-70.0 # initial voltage
    m[0]=0.05 # assumptions
    h[0]=0.54 # of the
    n[0]=0.34 # hh parameters' initial values
    spikes=0

    for i in range(0,T-1):
        V[i+1] = V[i] + dt*(gNa0*m[i]**3*h[i]*(ENa-(V[i]+65)) + gK0*n[i]**4*(EK-(V[i]+65)) + gL0*(EL-(V[i]+65)) + I0);
        m[i+1] = m[i] + dt*((2.5-0.1*(V[i]+65)) / (np.exp(2.5-0.1*(V[i]+65)) -1)*(1-m[i]) - 4*np.exp(-(V[i]+65)/18)*m[i]);
        h[i+1] = h[i] + dt*(0.07*np.exp(-(V[i]+65)/20)*(1-h[i]) - 1/(np.exp(3.0-0.1*(V[i]+65))+1)*h[i]);
        n[i+1] = n[i] + dt*((0.1-0.01*(V[i]+65)) / (np.exp(1-0.1*(V[i]+65)) -1)*(1-n[i]) - 0.125*np.exp(-(V[i]+65)/80)*n[i]);
        if (i!=T-1):
            if (V[i+1]>0 and V[i]<=0):
                spikes+=1
    return V,m,h,n,t,spikes*100/3
 
T0 = 30
x = np.linspace(0,10,30)
I0 = np.array([1 if math.floor(2*t)%2 == 0 else 0 for t in x])
print(I0)
 

 #q1
'''inp1 = float(input("Enter amplitude of current 1: "))
inp2 = float(input("Enter amplitude of current 2: "))
for i in I0:
    V1,m1,h1,n1,t1,spike=HodgkHux(inp1*i,T0)
    V2,m2,h2,n2,t2,spike=HodgkHux(inp2*i,T0)
    
plot(t1,V1)
plot(t2,V2)'''

#q2
'''inp1 = 2.89
inp2 = 2.91
for i in I0:
    V1,m1,h1,n1,t1,spike=HodgkHux(inp1*i,T0)
    V2,m2,h2,n2,t2,spike=HodgkHux(inp2*i,T0)
    
plot(t1,V1)
plot(t2,V2)'''
 
#q3
'''input= [i/3 for i in range(45)]
spik=[0 for i in range(45)]
for j in range(45):
    for i in I0:
        V,m,h,n,t,spik[j]=HodgkHux(input[j]*i,T0)
    
            
plot(input,spik)'''
       
      
 

