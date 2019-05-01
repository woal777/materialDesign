from pymatgen.io.pwscf import PWInput
import os

os.chdir('/home/ksrc5/FTJ/bfo/111-dir/sto-bfo/qe')
pio = PWInput.from_file('scf.in')
print(pio)
