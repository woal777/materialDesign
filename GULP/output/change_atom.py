import numpy as np

with open('zno.xyz') as f:
    lines = f.readlines()
    n = int(lines[0]) + 2
    snapshot = []
    for a in range(len(lines) // n):
        snapshot.append(lines[a * n:(a + 1) * n])
    for i, j in enumerate(snapshot[0]):
        if i < 2:
            continue
        x, y, z = j.split()[-3:]
        if 16 > float(z) > 10 and 8 > float(y) > 4 and 10 > float(x) > 6:
            print(j)
            if j.__contains__('Zn'):
                for k in range(len(snapshot)):
                    snapshot[k][i] = snapshot[k][i].replace('Zn', 'Ni')
            else:
                for k in range(len(snapshot)):
                    snapshot[k][i] = snapshot[k][i].replace('O', 'N')
    #    for i in snapshot:
    #        for j in range(2280, )
    #        i[1963] = i[1963].replace('La', 'Ce')
    #        i[2000] = i[2000].replace('La', 'Ce')
    #        i[2001] = i[2001].replace('La', 'Ce')
    #        print(i[2000])
    snapshot = np.array(snapshot)
    print(snapshot.shape)
    reduced = snapshot[::4]
    print(reduced.shape)
    with open('reduced.xyz', 'w') as g:
        for i in reduced:
            g.writelines(i)
