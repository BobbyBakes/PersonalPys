#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kyu
#
# Created:     10/10/2012
# Copyright:   (c) Kyu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

##x
##array([  0.00000000e+00,   6.13592315e-03,   1.22718463e-02, ...,
##         6.26477754e+00,   6.27091346e+00,   6.27704938e+00])
>>> si=sin(x)
>>> pylab.plot(x,si)
[<matplotlib.lines.Line2D object at 0x0407E6F0>]
>>> pylab.show()
>>> fftsi=np.fft.fft(si)
>>> pylab.plot(x,fftsi)
[<matplotlib.lines.Line2D object at 0x04299270>]
>>> pylab.show()
>>> xlong=arange(-50,50,.001)
>>> si=sin(xlong)
>>> fftsi=np.fft.fft(si)
>>> pylab.plot(xlong,fftsi)
[<matplotlib.lines.Line2D object at 0x04064750>]
>>> pylab.show()
>>> si=sin(3*xlong)+cos(xlong)
>>> fftsi=np.fft.fft(si)
>>> pylab.plot(xlong,fftsi)
[<matplotlib.lines.Line2D object at 0x03608BF0>]
>>> pylab.show()
>>> co=cos(xlong)
>>> fftco=np.fft.fft(co)
>>> pylab.plot(xlong,fftco)
[<matplotlib.lines.Line2D object at 0x03D89890>]
>>> pylab.show()