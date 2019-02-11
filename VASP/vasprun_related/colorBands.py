from pymatgen.electronic_structure.plotter import BSPlotterProjected
from pymatgen.io.vasp.outputs import BSVasprun, Element
path = '/home/jinho93/oxides/amorphous/igzo/band/'
vrun = BSVasprun(path+'vasprun.xml', True, True)
bs = vrun.get_band_structure(path+'KPOINTS')
plotter = BSPlotterProjected(bs)
plt = plotter.get_plot(ylim=(0, 5), vbm_cbm_marker=True)
#plt = plotter.get_elt_projected_plots_color(elt_ordered=[Element.O, Element.In, Element.Ga])

plt.ylim((0, 5))
plt.show()