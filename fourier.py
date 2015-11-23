#!/usr/bin/env python # fourier.py
import numpy as np
import pylab as pl
from numpy import *
N=1024
h=2*pi/1024
x=arange(0,1024*h,h)
def powerspectrum(u):
    amp=np.fft.fft(u)
    N=amp.shape[0]
    M=N/2;m=arange(M);odd=slice(1,None,2)
    if N%2==0:
        powspec=np.abs(amp/N)*2;
        powspec[0]=powspec[0]/2;powspec[M]=powspec[M]/2
        return powspec[:M+1]
    elif N%2!=0:
        powspec=np.abs(amp/N)*2;
        powspec[0]=powspec[0]/2;#powspec[M]=powspec[M]/2
        return powspec[:M+1]
if __name__ == '__main__':
    M=N/2;m=arange(M);odd=slice(1,None,2);m=range(M/2)
    u0=4*(np.abs((x/pi)-1)-1)*((x/pi)-1)
    u1=(8/pi)*(np.abs((x/pi)-1))-(4/pi)
    u2=np.zeros(len(x))
    for i,j in enumerate(x):
        if j<pi:u2[i]=-8/(pi**2)
        elif j>pi:
            if j<2*pi:u2[i]=8/(pi**2)
        else:u2[i]=0 #default value anyway!
    for i in [u0,u1,u2]:
        y=powerspectrum(i)
        pl.hold(True)
        pl.semilogy(m[odd],y[:M/2][odd])
    pl.savefig('spectra.png')
