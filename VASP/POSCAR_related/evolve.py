import os

from pymatgen.io.vasp import Xdatcar
from pymatgen_diffusion.aimd.van_hove import EvolutionAnalyzer

os.chdir('/home/jinho93/oxides/cluster/zno/vasp/1.aimd/2.10A/2.02/3fs')
structures = Xdatcar('XDATCAR').structures
e = EvolutionAnalyzer(structures)
for s in structures:
    s.substitute()
e.plot_rdf_evolution(('O', 'O'))