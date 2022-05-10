#%%
from matplotlib.pyplot import figure
import xml.etree.ElementTree as ET
from pymatgen.io.vasp import Outcar
import numpy as np
import os

def cond(vrun='vasprun.xml'):
    conductivity = []
    with open(vrun) as stream:
        for event, elem in ET.iterparse(stream):
            tag = elem.tag
            if tag == "conductivity":
                for arr in elem.find('array').find('set').findall('r'):
                    conductivity.append(arr.text.split())

    conductivity = np.array(conductivity, dtype=float)
    
    return conductivity


#%%
def epslion_intra(out, freq, eff_mass):
    gamma = 0.1
    n = 2e+28
    rho = 2e-7
    electron = 1.6e-19
    hbar = 6.582e-16
    h = 4.1357e-15
    mass = 9.11e-31 * eff_mass
    gamma = n * electron ** 2 * rho / mass * h
    wp = out.plasma_frequencies['intraband'][0,0]
    print(f'r={gamma}, wp={np.sqrt(wp)}')
    return [gamma * wp / (w ** 3 + w * gamma ** 2) if w !=0 else 0 for w in freq]

def epsilon_extra():
    arr = np.genfromtxt('IMAG.in')
    w = arr[:,0]
    eps = arr[:,1]   
    return w, eps

def sigma(eps, w):
    e0 = 8.8541878176e-12
    hbar = 6.582e-16
    h = 4.1357e-15
    return [i * j * e0 / h * 1e-2 / 2  for i, j in zip(eps, w)]

#%%
if __name__ == '__main__':
    # os.chdir('/backup/disk1/2022/JinhoByun/2021_Laser_n_Photonics_Reviews/strontium-niobate/loptics/dense-k/loptics')
    os.chdir('/home/jinho93/new/oxides/perobskite/sbvo/0/normal/optics/loptics')
    # os.chdir('/home/jinho93/new/oxides/perobskite/sbvo/50/conf-alter/optics/cond_Rev/loptics')
    outcar = Outcar('OUTCAR')
    outcar.read_freq_dielectric()
    import matplotlib.pyplot as plt
    x, y = epsilon_extra()
    # y2 = epslion_intra(outcar, x, 3.126)
    y2 = epslion_intra(outcar, x, 3.06)
    wtot = [r + s for r, s in zip(y, y2)]
    cond = sigma(wtot, x)
    # plt.plot(x, y)
    # plt.plot(x, y2)
    fig = plt.figure(figsize=(5, 5))
    plt.plot(x, cond)
    plt.xlim(0.6, 7)
    plt.ylim(0, 6)
    plt.show()
    # plt.plot(x, wtot)
    # plt.xlim(0.6, 7)
    # plt.ylim(0, 14)
    # plt.show()
    os.chdir('/home/jinho93')
    np.savetxt('x', x)
    np.savetxt('cond.dat', cond)
# %%

# %%
