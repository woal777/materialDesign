from fractions import Fraction

from pymatgen import Molecule, Element
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    p_arr = []
    n_atom = 0
    for num_step in range(400):
        if num_step == 0:
            filename = 'example'
        else:
            filename = f'example_{num_step}'
        with open(filename) as f:
            p = np.zeros(3)
            for l in f:
                if l.__contains__('thermostat'):
                    break
                if l.__contains__('core'):
                    if num_step == 1:
                        n_atom += 1

                    try:
                        coord = np.array(l.split()[2:5]).astype(float)
                    except ValueError:
                        tmp = [float(Fraction(r)) for r in l.split()[2:5]]
                        coord = np.array(tmp)
                    if l.__contains__('Al'):
                        p += coord * 3
                    elif l.__contains__('La'):
                        p += coord * 3
                    elif l.__contains__('O'):
                        p += coord * 0.04
                elif l.__contains__('shel'):
                    try:
                        coord = np.array(l.split()[2:5]).astype(float)
                    except ValueError:
                        tmp = [float(Fraction(r)) for r in l.split()[2:5]]
                        coord = np.array(tmp)
                    p += coord * -2.04
            p_arr.append(p)

                # else:
                #     p -= i.coords * 2.04


    p_arr = np.array(p_arr)
    return p_arr, n_atom


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/2.100/2.conf/again2')
    p, n = main()
    n //= 5
    pz = p[:, 2]
    e = 1.6e-19
    a = 3.81127
    vol = a ** 3
    pz *= e / n / vol * 1e+20
    np.savetxt('pz.dat', pz)
    plt.plot(pz)
    plt.show()