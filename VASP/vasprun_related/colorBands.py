from pymatgen.electronic_structure.plotter import BSPlotterProjected
from pymatgen.io.vasp.outputs import BSVasprun, Element
path = '/home/jinho93/interface/pzt-bso/loose/opti/band/'
vrun = BSVasprun(path+'vasprun.xml', True, True)
bs = vrun.get_band_structure(path+'KPOINTS')
plotter = BSPlotterProjected(bs)
#plt = plotter.get_elt_projected_plots_color(elt_ordered=[Element.O, Element.Hf])
#plt = plotter.get_plot(ylim=(-8, 5), vbm_cbm_marker=True)
plt = plotter.get_elt_projected_plots_color(elt_ordered=[Element.Ti, Element.Sn, Element.O])
plt.ylim((-5, 6))
plt.show()