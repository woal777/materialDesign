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
        print('main')
        while True:
            if os.path.exists(os.curdir + '/stop'):
                break
            self.loop()
            self.n += 1
            break

    def loop(self):
        if not os.path.exists(f'conf{self.n}'):
            os.mkdir(f'conf{self.n}')
            shutil.copy('INCAR', f'conf{self.n}')
            shutil.copy('KPOINTS', f'conf{self.n}')
            shutil.copy('POTCAR', f'conf{self.n}')
            self.s.to('POSCAR', f'conf{self.n}/POSCAR')
            pathlib.Path(f'conf{self.n}/wait').touch()
        os.chdir(f'conf{self.n}')
        self.calculate()
        os.chdir('..')

    def calculate(self):
        if len(self.output) > 2:
            if self.output[-1] - self.output[-2] > 0:
                self.displacement = -self.displacement / 2
            self.move()
        while True:
            try:
                with open('report.vasp') as stdio:
                    output = stdio.read()
                    if output.__contains__('F='):
                        for i in output.split('\n'):
                            if re.search('F=', i):
                                self.output.append(float(i.split()[2]))
                                break
                    else:
                        continue
                        time.sleep(3)
            except FileNotFoundError:
                time.sleep(3)
                pass

    def move(self):
        ind = []
        for i, site in enumerate(self.s.sites):
            if str(site.specie) == 'Pt':
                ind.append(i)
        self.s.translate_sites(ind, (0, 0, self.displacement))


if __name__ == '__main__':
    s = Slab()
    s.main()
