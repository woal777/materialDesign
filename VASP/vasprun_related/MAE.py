from VASP.vasprun_related.FeN import *


def below_fermi(orbital, spin):
    return zip(dos_dict[orbital].densities[spin][dos_dict[orbital].energies < ef],
               dos_dict[orbital].energies[dos_dict[orbital].energies < ef])


def above_fermi(orbital, spin):
    return zip(dos_dict[orbital].densities[spin][dos_dict[orbital].energies > ef],
               dos_dict[orbital].energies[dos_dict[orbital].energies > ef])


class Coupling:
    """
    dxy = |2> - |-2>
    dyz = |1> + |-1>
    dxz = |1> - |-1>
    dx2 = |2> + |-2>
    dz2 = |0>
    E_MCA = chi ** 2 / 4 sum_o,u [<Lz>^2 - <Lx>^2] / [e_u - e_o]
    """
    mae = 0

    '''
    dxy dyz dz2 dxz dx2
    0   0   0  -1   2
    0   0 -3/4  1  -1  
    0 -3/4  0   0   0
   -1   1   0   0   0
    2  -1   0   0   0
    '''

    def __init__(self):
        self.coupling_o1_o2(-3 / 4, 'dyz', 'dz2')
        self.coupling_o1_o2(1, 'dyz', 'dxz')
        self.coupling_o1_o2(-1, 'dyz', 'dx2')
        self.coupling_o1_o2(-1, 'dxz', 'dxy')

    @staticmethod
    def change_site(site):
        for orb in [Orbital.dxy, Orbital.dyz, Orbital.dz2, Orbital.dxz, Orbital.dx2]:
            dos_dict[orb.name] = cdos.get_site_orbital_dos(structure.sites[site], orb)

    def coupling_o1_o2(self, factor, o1, o2):
        self.mae = 0

        def sum_mae(orb1, orb2, spin1, spin2):
            is_flipped = (spin1 == spin2)
            if is_flipped:
                for i, e1 in below_fermi(orb1, spin1):
                    for j, e2 in above_fermi(orb2, spin2):
                        self.mae += factor * (i * j) ** 2 / (e2 - e1)
            else:
                for i, e1 in below_fermi(orb1, spin1):
                    for j, e2 in above_fermi(orb2, spin2):
                        self.mae -= factor * (i * j) ** 2 / (e2 - e1)

        sum_mae(o1, o2, Spin.down, Spin.down)
        sum_mae(o1, o2, Spin.up, Spin.down)
        sum_mae(o2, o1, Spin.down, Spin.down)
        sum_mae(o2, o1, Spin.up, Spin.down)
        # sum_mae(o1, o2, Spin.down, Spin.up)
        # sum_mae(o1, o2, Spin.up, Spin.up)
        # sum_mae(o2, o1, Spin.down, Spin.up)
        # sum_mae(o2, o1, Spin.up, Spin.up)

        print(self.mae * dx ** 2)


if __name__ == '__main__':
    c = Coupling()
