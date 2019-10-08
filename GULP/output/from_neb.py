for i in range(12):
    h = open(f'POSCAR{i}.vesta')
    with open('POSCAR.vesta') as f:
        with open(f'{i:02d}.vesta', 'w') as g:
            struc = False
            for l, m in zip(f, h):
                if '0 0 0 0 0 0 0' in l:
                    struc = False
                if struc:
                    if '1.000' in l:
                        arr = l.split()
                        arr[4:7] = m.split()[4:7]
                        g.write(' '.join(arr) + '\n')
                else:
                    g.write(l)
                if 'STRUC' in l:
                    struc = True
