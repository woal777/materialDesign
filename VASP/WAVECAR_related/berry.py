from pymatgen.io.vasp.outputs import Wavecar
import os

if __name__ == '__main__':

    os.chdir('/home/jinho93/tmdc/mos2/2h/hse/bulk/dos')
    wave = Wavecar()
    print(wave)
    print(len(wave.coeffs[0][0]))
