import numpy as np
import os
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/nvt.para.6/island/len-19/step2')
with open('lao.xyz') as f:
    lines = f.readlines()
    n = int(lines[0]) + 2
    snapshot = []
    for a in range(len(lines) // n):
        snapshot.append(lines[a*n:(a + 1)*n])
    #snapshot = np.array(snapshot)
    l: str
    arr = []
    count = 0
    for num, l in enumerate(snapshot[0][2:]):
        if 13 > float(l.split()[-1]) > 9:
                arr.append(num)
                count += 1
    reduced = [[s[i + 2] for i in arr] for s in snapshot]
    for _ in reduced:
        _.insert(0,'\n')
        _.insert(0, f"{count}\n")
    snapshot = np.array(snapshot)
    with open('reduced_atoms.xyz', 'w') as g:
        for i in reduced:
            g.writelines(i)
