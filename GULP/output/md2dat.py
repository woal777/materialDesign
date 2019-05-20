import os
import re
import numpy as np


def main():
    with open('report.gulp')as f:
        Time = re.compile('Time :')
        Kinetic = re.compile('Kinetic')
        Potential = re.compile('Potential ene')
        Temperature = re.compile('Temperature   ')
        time = []
        ke = []
        pe = []
        temp = []
        for l in f:
            if Time.search(l):
                time.append(float(l.split()[-3]))
            elif Kinetic.search(l):
                ke.append(float(l.split()[-2]))
            elif Potential.search(l):
                pe.append(float(l.split()[-2]))
            elif Temperature.search(l):
                temp.append(float(l.split()[-2]))
        return np.array([time, ke, pe, temp])


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/cluster/zno/gulp/meskine/line/nve')
    output = main()
    np.savetxt('output.dat', output.transpose(), header='K.E. P.E. Temp')

