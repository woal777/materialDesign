arr = []
path = '/home/jinho93/slab/LAO/nvt/island/dipole_effect/'
with open(path + 'example15.grs') as f:
    for l in f:
        if l.__contains__('core'):
            tmp = l.split()[:5]
            tmp.pop(1)
            arr.append(' '.join(tmp) + '\n')

with open(path + 'output.xyz', 'w') as f:
    f.write(f'{len(arr)}\n')
    f.write('\n')
    f.writelines(arr)