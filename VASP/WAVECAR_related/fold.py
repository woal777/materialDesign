import os
from unfold import make_kpath, removeDuplicateKpoints, find_K_from_k, save2VaspKPOINTS
from unfold import EBS_cmaps
from unfold import EBS_scatter
from unfold import unfold

os.chdir(
    '/home/jinho93/oxides/perobskite/strontium-titanate/2.supc/vasp/1.defect/5.Vo/333/hub/4.4eV/dense/m5.ismear/k444/4.lmaxmix/band')

M = [[3.0, 0.0, 0.0],
     [0.0, 3.0, 0.0],
     [0.0, 0.0, 3.0]]


# high-symmetry point of a Hexagonal BZ in fractional coordinate
kpts = [[0.5, 0.0, 0.0],  # M
        [0.0, 0.0, 0.0],  # G
        [0.0, 0.0, 0.5]]  # G
# create band path from the high-symmetry points, 30 points inbetween each pair
# of high-symmetry points
kpath = make_kpath(kpts, nseg=30)
K_in_sup = []
for kk in kpath:
    kg, g = find_K_from_k(kk, M)
    K_in_sup.append(kg)
# remove the duplicate K-points
reducedK = removeDuplicateKpoints(K_in_sup)


# basis vector of the primitive cell
cell = [[3.9082120409162044, 0.0000000000000000,  0.0],
        [0, 3.9082120409162044,  0.0],
        [0.0000, 0.0000000000000000, 3.9082120409162044]]

WaveSuper = unfold(M=M, wavecar='WAVECAR')

sw = WaveSuper.spectral_weight(kpath)
ef = 4.8211


EBS_scatter(kpath, cell, sw, nseg=30, eref=-4.01,
        ylim=(-3, 4), 
        factor=5)

e0, sf = WaveSuper.spectral_function(nedos=4000)
EBS_cmaps(kpath, cell, e0, sf, nseg=30, eref=-4.01,
        show=False,
        ylim=(-3, 4))