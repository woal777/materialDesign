from MDAnalysis.coordinates.DCD import DCDReader
from MDAnalysis.coordinates.XYZ import XYZReader
from MDAnalysis.analysis.rms import RMSD
from MDAnalysis.core.universe import Universe, AtomGroup, Atom
from MDAnalysis.tests.datafiles import PSF, DCD
from MDAnalysis.coordinates.PDB import PDBReader
dcd = DCDReader('/home/jinho93/slab/LAO/grimes/opt/test/lao.dcd')
xyz = XYZReader('/home/jinho93/slab/LAO/grimes/opt/test/lao.xyz')
Universe(xyz)
for ts in dcd.trajectory:
    print(ts.forces)

    #print(f"Frame: {ts.frame:5d}, Time: {ts.time:8.3f} ps {dir(ts)}")
