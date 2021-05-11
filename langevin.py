#!/usr/bin/python3

from math import *

def langevin(x):
    if (abs(x)<0.0000001):
        l=x/3
    elif(x>700):
        l=1
    elif(x<-700):
        l=-1
    else:
        l=cosh(x)/sinh(x)-1/x
    return l

mu_r=1e4 # dimensionless
mu0=4*pi*1e-7 # T*m/A

Bs=.7    # T

Hmin=0   # A/m
Hmax=1000 # A/m
nH=1001   # number of H points

with open('l4test.dat', 'w') as f:
    for i in range(0,nH):
        H=Hmin+i*(Hmax-Hmin)/(nH-1)
        print(H,Bs*langevin(3*mu_r*mu0*H/Bs),file=f)
