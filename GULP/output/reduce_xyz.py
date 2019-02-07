import numpy as np

with open('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/nvt.para.6/island/19/step2/lao.xyz') as f:
    lines = f.readlines()
    n = int(lines[0]) + 2
    snapshot = []
    for a in range(len(lines) // n):
        snapshot.append(lines[a*n:(a + 1)*n])
    snapshot = np.array(snapshot)
    print(snapshot.shape)
    reduced = snapshot[::5]
    print(reduced.shape)
    with open('reduced.xyz', 'w') as g:
        for i in reduced:
            g.writelines(i)