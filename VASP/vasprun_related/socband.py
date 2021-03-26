import xml.etree.cElementTree as ET
import numpy as np

from pymatgen import Spin


def main():
    def _vasprun_float(f):
        """
        Large numbers are often represented as ********* in the vasprun.
        This function parses these values as np.nan
        """
        try:
            return float(f)
        except ValueError as e:
            f = f.strip()
            if f == '*' * len(f):
                return np.nan
            raise e

    def _parse_varray(elem):
        m = [[float(i) for i in v.text.split()] for v in elem]
        return m

    def dos():
        # efermi = float(elem.find("i").text)
        energies = None
        tdensities = {}
        idensities = {}

        for s in elem.find("array").find("set").find("set").findall("set"):
            data = np.array(_parse_varray(s))
            energies = data[:, 0]
            spin = s.attrib["comment"]
            idensities[spin] = data[:, 1:]
        return energies, idensities


    tree = ET.iterparse('vasprun.xml')
    test = None
    for event, elem in tree:
        tag = elem.tag
        if not (tag == 'v' or tag == 'r' or tag == 'set') and tag == 'partial':
            test = dos()

    return test



if __name__ == '__main__':
    import os
    os.chdir('/home/jinho93/metal/1.FeRh/1.fm/soc')
    e, den = main()