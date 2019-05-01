import re
import os
import matplotlib.pyplot as plt

os.chdir('/home/jinho93/oxides/cluster/zno/rnd/600k/nve/49')
with open('report.vasp') as f:
    temp = []
    ke = []
    pe = []
    time = []
    for l in f:
        if re.search('Temperature {7}', l):
            temp.append(float(l.split()[-2]))
        elif re.search('Kinetic energy ', l):
            ke.append(float(l.split()[-2]))
        elif re.search('Potential energy ', l):
            pe.append(float(l.split()[-2]))
        elif re.search('Time : ', l):
            time.append(float(l.split()[-3]))
    plt.plot(time, temp, label='temp')
    plt.plot(time, ke, label='Kinetic energy ')
    #plt.plot(time, pe, label='Potential energy ')
    plt.legend()
    plt.show()
