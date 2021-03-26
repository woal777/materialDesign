from pymatgen import Molecule, Element
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    p_arr = []
    with open('lao.xyz') as f:
        arr = f.readlines()
        n_atom = int(arr[0])
        print(n_atom)
        n_atom += 2
        num_shot = 100
        for num_step in range(num_shot):
            tmp = ''.join(arr[(n_atom * num_step):n_atom * (num_step + 1)])
            m = Molecule.from_str(tmp, 'xyz')
            p = np.zeros(3)
            # La2 = [492, 493, 496, 497]
            # La2 = [397, 398]
            for j, i in enumerate(m.sites):
                # if j in La2:
                #     p += i.coords * 2
                if i.specie == Element.Al:
                    p += i.coords * 3
                elif i.specie == Element.La:
                    p += i.coords * 3
                elif i.specie == Element.O:
                    p += i.coords * -2
                # else:
                #     p -= i.coords * 2.04

            p_arr.append(p)

    p_arr = np.array(p_arr)
    return p_arr, n_atom - 2


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/2.100/2.conf/nose-hoover')
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