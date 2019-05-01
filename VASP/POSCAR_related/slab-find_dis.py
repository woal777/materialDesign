import pathlib
import time
from pymatgen.io.vasp.outputs import Structure
import os
import shutil
import re


class Slab:
    def __init__(self):
        self.s = Structure.from_file('POSCAR')
        self.n = 0
        self.output = []
        self.displacement = -0.1

    def main(self):
        while True:
            if os.path.exists(os.curdir + '/stop'):
                break
            self.loop()
            self.n += 1
            print(self.n)

    def loop(self):
        if not os.path.exists(f'conf{self.n}'):
            os.mkdir(f'conf{self.n}')
            shutil.copy('INCAR', f'conf{self.n}')
            shutil.copy('KPOINTS', f'conf{self.n}')
            shutil.copy('POTCAR', f'conf{self.n}')
            self.s.to('POSCAR', f'conf{self.n}/POSCAR')
            self.move()
            if self.n > 0:
                shutil.copy2(f'conf{self.n - 1}/CHGCAR', f'conf{self.n}')
                shutil.copy2(f'conf{self.n - 1}/WAVECAR', f'conf{self.n}')
            pathlib.Path(f'conf{self.n}/wait').touch()
        else:
            self.s = Structure.from_file(f'conf{self.n}/POSCAR')
            self.move()
        os.chdir(f'conf{self.n}')
        self.calculate()
        os.chdir('..')

    def calculate(self):
        if len(self.output) > 2:
            if self.output[-1] - self.output[-2] > 0:
                self.displacement = -self.displacement / 2
        if os.path.exists('finish'):
            self.add_output()
            return 0
        while not os.path.exists('finish'):
            try:
                self.add_output()
                time.sleep(3)
            except FileNotFoundError:
                time.sleep(3)
                pass

    def move(self):
        ind = []
        for i, site in enumerate(self.s.sites):
            if str(site.specie) == 'Pt':
                ind.append(i)
        self.s.translate_sites(ind, (0, 0, self.displacement), frac_coords=False)

    def add_output(self):
        with open('report.vasp') as stdio:
            output = stdio.read()
            for i in output.split('\n'):
                if re.search('F=', i):
                    self.output.append(float(i.split()[2]))
                    pathlib.Path('finish').touch()


if __name__ == '__main__':
    s = Slab()
    s.main()
