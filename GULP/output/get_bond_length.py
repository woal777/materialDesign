import os
import numpy as np
import matplotlib.pyplot as plt
from MDAnalysis import Universe
from MDAnalysis.analysis.rdf import InterRDF
from MDAnalysis.lib.distances import distance_array


def main():
    nbins = 300
    with open('cluster.xyz') as f:
        u = Universe(f)
        oxy = u.select_atoms('name O and prop 0 < z and prop z < 20', updating=True)
        zinc = u.select_atoms('name Zn and prop 0 < z and prop z < 20')
        rdfs = []
        rdfs.append(np.linspace(0, 15, nbins))
        for ts in u.trajectory[::len(u.trajectory) - 1]:
            dist = distance_array(zinc.positions, oxy.positions)
            rdf, edge = np.histogram(dist, bins=nbins, range=(0, 15))
            vol = 4 / 3 * np.pi * (np.power(edge[1:], 3) - np.power(edge[:-1], 3))
            print(len(vol), len(rdf))
            print(vol)
            rdf = rdf / vol
            plt.plot(np.linspace(0, 15, nbins), rdf)
            rdfs.append(rdf)
        rdfs = np.array(rdfs).transpose()
        np.savetxt('output2.dat', rdfs)
        plt.show()


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/cluster/zno/gulp/whitmore/line/conf4')
    main()
