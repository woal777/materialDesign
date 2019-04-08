import os


for i in ['{:03d}'.format(r) for r in range(1, 49)]:
    os.mkdir(i)
    kind = ''
    dft = ''
    with open('kind.inp') as k:
        kind = k.read()
    with open('dft.inp') as d:
        dft = d.read()
    with open(f'supercell-{i}.inp') as f:
        with open(f'{i}/input.inp') as i:
            i.write(f.readline())
            i.write(dft)
            lines = f.readlines()
            for j in lines:
                if j.__contains__('END COORD'):
                    i.write(j)
                    i.write(kind)
                else:
                    i.write(j)
