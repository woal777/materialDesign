import numpy as np
import os
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/nvt.para.6/island/len-19/step2')
with open('lao.xyz') as f:
    lines = f.readlines()
    n = int(lines[0]) + 2
    snapshot = []
    for a in range(len(lines) // n):
        snapshot.append(lines[a*n:(a + 1)*n])
    for i in snapshot:
        i[1963] = i[1963].replace('La', 'Ce')
        i[2000] = i[2000].replace('La', 'Ce')
        i[2001] = i[2001].replace('La', 'Ce')
        print(i[2000])
    snapshot = np.array(snapshot)
    print(snapshot.shape)
    reduced = snapshot[::4]
    print(reduced.shape)
    with open('reduced.xyz', 'w') as g:
        for i in reduced:
            g.writelines(i)