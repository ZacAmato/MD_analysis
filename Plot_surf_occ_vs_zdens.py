# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.gridspec as gridspec
import warnings
import matplotlib.pyplot as mplplot
from matplotlib import cm
import glob
import matplotlib.pyplot as plt

time = str('100')


zdens_20 = pd.read_csv(f"../300Kwater_on_20Ksilic/RUN01/Heat_Ramps/{time}_ns/Analysis/Output_Files/Density/densnum_300Kwater_on_20Ksilic_relax_20K_100ns.xvg",
                   delim_whitespace=True,
                   skiprows=24,
                   names=["Coord", "dens"],
                   ).set_index("Coord")


zdens_20.index = zdens_20.index - 15.05 

zdens_20.index = zdens_20.index * 10

print(zdens_20)


zdens_200 = pd.read_csv(f"../300Kwater_on_20Ksilic/RUN01/Heat_Ramps/{time}_ns/Analysis/Output_Files/Density/densnum_300Kwater_on_20Ksilic_heating_200K_100ns.xvg",
                   delim_whitespace=True,
                   skiprows=24,
                   names=["Coord", "dens"],
                   ).set_index("Coord")


zdens_200.index = zdens_200.index - 15.05 

zdens_200.index = zdens_200.index * 10

print(zdens_200)


surf_occ = pd.read_csv("../300Kwater_on_20Ksilic/RUN01/Heat_Ramps/100_ns/Analysis/Output_Files/Surface_Occ/mol_num/surf_occ_results.txt",
                   delim_whitespace=True,
                   names=["temp", "layer", "surf_occ"],
                   ).set_index("temp")


print(surf_occ)



# Split jet map 
jet = mplplot.get_cmap('jet')

colors = jet(np.linspace(0,1,19))


fig, ax = plt.subplots(1, 3, figsize=(20,7))
# Remove horizontal space between axes
#fig.subplots_adjust(wspace=0, hspace=0)
plt.rcParams["axes.linewidth"]	= 2
plt.rcParams["mathtext.default"] = "regular"


ax[0].scatter(surf_occ.index, surf_occ['surf_occ'], color=cm.viridis((surf_occ['layer'] - 50) /(500 - 50))   ) 
ax[0].tick_params(which="major", labelsize=16, width=1.5, length=6)
ax[0].tick_params(which="minor", labelsize=16, width=1.5, length=4)
ax[0].set_ylim([0.7, 1.01])
ax[0].set_ylabel('Proportion of Surface Occluded', fontsize=16)
ax[0].set_xlabel('Simulation Annealing Temperature (K)', fontsize=16)


ax[1].plot(zdens_20['dens'], zdens_20.index, c="#00008B", linewidth=0.8)
ax[1].tick_params(which="major", labelsize=16, width=1.5, length=6)
ax[1].tick_params(which="minor", labelsize=16, width=1.5, length=4)
ax[1].set_xlim(0,100)
ax[1].set_ylim(0,40)
ax[1].set_ylabel('Distance from surface ($\AA$)', fontsize=16)
ax[1].set_xlabel('O Number Density', fontsize=16)

ax[1].axhline(y = 2.8928007297276785, color = 'grey', linestyle = '--') 
ax[1].axhline(y = 4.783176928719159, color = 'grey', linestyle = '--') 
ax[1].axhline(y = 6.499039465211804, color = 'grey', linestyle = '--') 
ax[1].axhline(y = 9.02422926370281, color = 'grey', linestyle = '--') 
ax[1].axhline(y = 12.525926203434397, color = 'grey', linestyle = '--') 
ax[1].axhline(y = 15.690235870861704, color = 'grey', linestyle = '--') 
ax[1].axhline(y = 18.522200784467785, color = 'grey', linestyle = '--') 
ax[1].axhline(y = 21.85506257477766, color = 'grey', linestyle = '--') 
ax[1].axhline(y = 26.414745159955064, color = 'grey', linestyle = '--') 
ax[1].axhline(y = 36, color = 'grey', linestyle = '--') 



ax[2].plot(zdens_200['dens'], zdens_200.index, c="#AF111D", linewidth=0.8)
ax[2].tick_params(which="major", labelsize=16, width=1.5, length=6)
ax[2].tick_params(which="minor", labelsize=16, width=1.5, length=4)
ax[2].set_xlim(0,100)
ax[2].set_ylim(0,40)
#ax[2].set_ylabel('Distance from surface ($\AA$)', fontsize=16)
ax[2].set_xlabel('O Number Density', fontsize=16)


ax[2].axhline(y = 2.6006975790641937, color = 'grey', linestyle = '--') 
ax[2].axhline(y = 3.4979053786710343, color = 'grey', linestyle = '--') 
ax[2].axhline(y = 5.350136052088127, color = 'grey', linestyle = '--') 
ax[2].axhline(y = 6.480098847802554, color = 'grey', linestyle = '--') 
ax[2].axhline(y = 8.24624465317997, color = 'grey', linestyle = '--') 
ax[2].axhline(y = 9.748221259387632, color = 'grey', linestyle = '--') 
ax[2].axhline(y = 11.263474987579766, color = 'grey', linestyle = '--') 
ax[2].axhline(y = 12.777199089074452, color = 'grey', linestyle = '--') 
ax[2].axhline(y = 14.211702642672066, color = 'grey', linestyle = '--') 
ax[2].axhline(y = 18, color = 'grey', linestyle = '--')


props = dict(boxstyle='round', facecolor='lightgrey', alpha=0.5)

fig.text(0.59, 0.82, '20 K', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=16, bbox=props)
fig.text(0.858, 0.82, '200 K', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=16, bbox=props)

scalarmappable = cm.ScalarMappable(cmap=cm.viridis)
scalarmappable.set_array(range(50, 550, 50))
cbar_ax = fig.add_axes([0.04, 0.15, 0.02, 0.7])
cb = fig.colorbar(scalarmappable, cax = cbar_ax)
cb.ax.tick_params(labelsize=15)
cb.ax.yaxis.set_ticks_position('left')


fig.text(0.00001, 0.26, 'Number of Water Molecules', horizontalalignment='left', verticalalignment='bottom', rotation='vertical', color = 'black', size=16)


mplplot.savefig('../Plots/low_res_plots/lowres_surf_occ_vs_zdens.png', bbox_inches='tight', dpi=800)

