#%%

from VASP.vasprun_related.optics import *
import os

if __name__ == '__main__':
    os.chdir('/home/jinho93/new/oxides/perobskite/sbvo/0/normal/optics/loptics')
    x1, ep_ex1 = epsilon_extra()
    outcar1 = Outcar('OUTCAR')
    outcar1.read_freq_dielectric()
    os.chdir('/home/jinho93/new/oxides/perobskite/sbvo/50/conf-alter/optics/cond_Rev/loptics')
    x2, ep_ex2 = epsilon_extra()
    outcar2 = Outcar('OUTCAR')
    outcar2.read_freq_dielectric()
    outcar = [outcar1, outcar2]
    x = [x1, x2]
    ep_ex = [ep_ex1, ep_ex2]
    ep_in1 = epslion_intra(outcar1, x2, 3.06)
    ep_in2 = epslion_intra(outcar2, x2, 3.13)
    ep_in = [ep_in1, ep_in2]
    wtot = [[r + s for r, s in zip(y, y2)] for y, y2 in zip(ep_ex, ep_in)]
    cond = [sigma(wtots, xs) for wtots, xs in zip(wtot, x)]
    os.chdir('/home/jinho93')
    for i in range(len(x)):
        np.savetxt(f'cond{i}.dat', np.array([x[i], cond[i]]).T)
# %%

# %%
