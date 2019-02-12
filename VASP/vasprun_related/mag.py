from pymatgen.io.vasp import Outcar

oc = Outcar('OUTCAR')
for i in oc.magnetization:
    print(i['tot'])
