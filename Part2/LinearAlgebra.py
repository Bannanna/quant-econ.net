##REVIEW LINEAR ALGEBRA##

import numpy as np
import matplotlib.pyplot as plt
import math
##Linear Model
##y1 = a11x1+a12x2+ ... +a1kxk

x = np.ones(3)
y = np.arange(1,4)

#[x1+y1, x2+y2, ...]
print 'x: ', x,'\ny: ', y
print 'x + y = ', x + y

##Inner Product
def innerproduct(xx, yy):
    if len(xx) == len(yy):
        try:
            ip = np.zeros(len(xx))
            for i, e in enumerate(xx):
                ip[i] = xx[i] * yy[i]
            return sum(ip)
        except err:
            print err
ipxy = innerproduct(x, y)
print 'Inner Product x and y = ', ipxy
print "Is homebrewed calculation of inner() same as numpy calculation?", np.inner(x,y) == ipxy

##Calculate norm of x
##||x|| = sqrt(xprime, x)
def norm(xx):
    n = np.zeros(len(xx))
    for i, x in enumerate(xx):
        n[i] = xx[i] * xx[i]
    return math.sqrt(sum(n))

print 'Norm x = ', norm(x)
print 'Three ways to calculate norm? ', norm(x) == np.sqrt(np.sum(x**2)) == np.linalg.norm(x),
