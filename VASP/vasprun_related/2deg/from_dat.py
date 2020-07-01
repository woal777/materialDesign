import numpy as np

dat = np.genfromtxt('/home/jinho93/interface/pzt-bso/loose/opti/dos/output/dos.dat')

bools = (dat[:, 0] < 0) * (-.5 < dat[:, 0])
dx = dat[1,0] - dat[0,0]
print(np.sum(dat[:, 12][bools]) * dx)