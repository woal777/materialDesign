from pymatgen.electronic_structure.plotter import BSPlotterProjected
from pymatgen.io.vasp.outputs import BSVasprun
vrun = BSVasprun('/home1/jinho/HfO2/Pca21_material_project/PBE/bulk/bands/GXSYG/'+'vasprun.xml', True, True)
bs = vrun.get_band_structure('/home1/jinho/HfO2/Pca21_material_project/PBE/bulk/bands/GXSYG/'+'KPOINTS')
plotter = BSPlotterProjected(bs)
plt = plotter.get_elt_projected_plots_color()

plt.xlim((.0, .5))
plt.ylim((-4, 6))
plt.show()