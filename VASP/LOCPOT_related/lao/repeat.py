#%%
import numpy as np
import os

# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/dos')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/4/lvhar')
dat = np.genfromtxt('PLANAR_AVERAGE.dat')
# dat = np.genfromtxt('MACROSCOPIC_AVERAGE.dat')
before = []
after  = []
dat[:,0] *= -1
dat = dat[::-1]

for i, j in dat:
    before.append([i - dat[0,0], j])
    after.append([i - 2 * dat[0,0], j])
    
before = np.array(before)
after = np.array(after)

dat = np.concatenate([dat, before, after],axis=0)
# dat = np.concatenate([dat, after], axis=0)


np.savetxt('planer-repeat.dat', dat)
print('done')
# np.savetxt('macro-repeat.dat', dat)