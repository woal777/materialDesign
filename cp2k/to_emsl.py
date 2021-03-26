#%%
import os
import re

os.chdir('/home/jinho93/new/oxides/perobskite/sbvo/0/xas/cp2k')
orbit = re.compile('[spdfg]')
n = 0
with open('output', 'w') as g:
    with open('test') as f:
        g.write(f.readline())
        for l in f:
            if orbit.search(l):
                n += 1
                if 's' in l:
                    g.write(f'1 0 0 {l.split()[0]} 1 s\n')
                elif 'p' in l:
                    g.write(f'1 1 1 {l.split()[0]} 1 p\n')
                elif 'd' in l:
                    g.write(f'1 2 2 {l.split()[0]} 1 d\n')
                elif 'f' in l:
                    g.write(f'1 3 3 {l.split()[0]} 1 f\n')
                else:
                    g.write(f'1 4 4 {l.split()[0]} 1 g\n')
            else:
                g.write(l)    
    g.write(f'{n}')                    
# %%
