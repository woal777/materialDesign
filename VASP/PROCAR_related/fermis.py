#%%
import pyprocar as pr
import os   

os.chdir('/home/jinho93/oxides/perobskite/strontium-ruthenate/113')
pr.fermi2D('PROCAR', outcar='OUTCAR', energy=1, fermi=1)
# %%
