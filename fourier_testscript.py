#!/usr/bin/env python # fourier_testscript.py
from fourier import *
import numpy as np
import numpy.linalg as nplinalg
from subprocess import call
ifile = open('fourier_input.txt','r')
content = ifile.read().split('u')
u0 = np.array(eval(content[0]))
u1 = np.array(eval(content[1]))
u2 = np.array(eval(content[2]))
a0 = powerspectrum(u0)
a1 = powerspectrum(u1)
a2 = powerspectrum(u2)
a0d = np.array(eval(content[3]))
a1d = np.array(eval(content[4]))
a2d = np.array(eval(content[5]))
call('python fourier.py', shell=True)
if nplinalg.norm(a0d-a0)<1e-7 and nplinalg.norm(a1d-a1)<1e-7 and nplinalg.norm(a2d-a2)<1e-7:
    print 'Calculation is correct'
else:
    print 'Calculation is incorrect'
print 'Your program should generate a figure. Compare it with the given figure \'spectra.pdf\'.'
