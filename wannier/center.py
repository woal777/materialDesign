from abipy.wannier90 import wout


wo = wout.WoutFile('/home/ksrc5/FTJ/1.bfo/111-dir/wannier/wannier90.up.wout')
print(wo.wf_centers)
p = 0
for i in wo.structure.sites:
    if i.species_string == 'Fe':
        p += i.z * 8
    elif i.species_string == 'Bi':
        p += i.z * 5
    else:
        p += i.z * 6
    print(i.z)
