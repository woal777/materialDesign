#!/home/jinho93/miniconda3/envs/my_pymatgen/bin/python
with open('CHGCAR') as f:
    l = f.read()
    fr = l.find('\n \n')
    to = l.find('\n', fr + 5)
    out = l.rfind(l[fr + 5: to])
    with open('SPIN.vasp', 'w') as g:
        g.write(l[:fr + 5])
        g.write(l[out:])
