from math import exp, sqrt
import sys
import numpy
D0, S, r0 = 3.6, 1.0455, 1.724
beta = 1.8174
A = D0 / (S - 1) * exp(beta * sqrt(2 * S) * r0)
B = S * D0 / (S - 1) * exp(beta * sqrt(2 / S) * r0)
za = (beta * sqrt(2 * S))
zb = beta * sqrt(2 / S)

Rc, Dc = 2.6, .2
rtaper = Rc - Dc
rmax = Rc + Dc
numpy.savetxt(sys.stdout, [A, B, za, zb], fmt='%2.6f', newline=' ')
print(rtaper, rmax)