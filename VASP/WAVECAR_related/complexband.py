#%%
from pymatgen.io.vasp import Wavecar, Poscar
import os
import numpy as np


# os.chdir('/home/ksrc5/FTJ/1.bfo/111-dir/junction/sto/vasp/orig/dos')
def main(wave, de):
    a = None
    if wave.spin == 2:
        for s in range(2):
            for k in range(wave.nk):
                for b in range(wave.nb):
                    if wave.efermi + de < wave.band_energy[s][k][b][0] < wave.efermi + de + 1:
                        if a is None:
                            a = wave.get_parchg(poscar, k, b, s)
                        else:
                            a.linear_add(wave.get_parchg(poscar, k, b, s))
    else:
        for k in range(wave.nk):
            for b in range(wave.nb):
                if wave.efermi + de < wave.band_energy[k][b][0] < wave.efermi + de + 1:
                    if a is None:
                        a = wave.get_parchg(poscar, k, b)
                    else:
                        a.linear_add(wave.get_parchg(poscar, k, b))
    out=a.get_average_along_axis(2)
    
    return np.array(np.linspace(0, 1, len(out)), out).transpose()

if __name__ == '__main__':
    os.chdir('/home/ksrc5/FTJ/1.bfo/111-dir/junction/sto/vasp/vac/conf3/4.node03/dense_k_dos/again')
#    os.chdir('/home/ksrc5/FTJ/1.bfo/111-dir/junction/sto/vasp/orig/new_vca/dos2')
    wave = Wavecar('WAVECAR')
    poscar = Poscar.from_file('POSCAR')
    out = main(wave, 2)
    import matplotlib.pyplot as plt
    plt.imshow(out)

# %%
