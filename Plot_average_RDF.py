# -*- coding: utf-8 -*-
import pandas as pd
import glob
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import plotly.express as px
import plotly.graph_objects as go
import math
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from matplotlib import cm
import matplotlib.pyplot as mplplot
from sklearn import preprocessing
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)

time = str('100')
atom = str('O')


files = glob.glob(f"../RDF/rdf_{atom}_*.txt")
df20 = pd.concat(
    [
        pd.read_csv(
            f,
            sep='\s+',
            skiprows=1,
            names=["coordinate", f"{f.split('_')[-3][:-1]}"],
        ).set_index("coordinate")
        for f in sorted(files, key=lambda f_: int(f_.split("_")[-3][:-1]))
    ],
    axis=1,
)

df20.index = df20.index * 10

print(df20)

#########


files = glob.glob(f"../RDF/rdf_{atom}_*.txt")
df40 = pd.concat(
    [
        pd.read_csv(
            f,
            sep='\s+',
            skiprows=1,
            names=["coordinate", f"{f.split('_')[-3][:-1]}"],
        ).set_index("coordinate")
        for f in sorted(files, key=lambda f_: int(f_.split("_")[-3][:-1]))
    ],
    axis=1,
)


df40.index = df40.index * 10

print(df40)

###########


files = glob.glob(f"../RDF/rdf_{atom}_*.txt")
df60 = pd.concat(
    [
        pd.read_csv(
            f,
            sep='\s+',
            skiprows=1,
            names=["coordinate", f"{f.split('_')[-3][:-1]}"],
        ).set_index("coordinate")
        for f in sorted(files, key=lambda f_: int(f_.split("_")[-3][:-1]))
    ],
    axis=1,
)


df60.index = df60.index * 10

print(df60)

###########


files = glob.glob(f"../RDF/rdf_{atom}_*.txt")
df80 = pd.concat(
    [
        pd.read_csv(
            f,
            sep='\s+',
            skiprows=1,
            names=["coordinate", f"{f.split('_')[-3][:-1]}"],
        ).set_index("coordinate")
        for f in sorted(files, key=lambda f_: int(f_.split("_")[-3][:-1]))
    ],
    axis=1,
)


df80.index = df80.index * 10


print(df80)

#########


files = glob.glob(f"../RDF/rdf_{atom}_*.txt")
df100 = pd.concat(
    [
        pd.read_csv(
            f,
            sep='\s+',
            skiprows=1,
            names=["coordinate", f"{f.split('_')[-3][:-1]}"],
        ).set_index("coordinate")
        for f in sorted(files, key=lambda f_: int(f_.split("_")[-3][:-1]))
    ],
    axis=1,
)


df100.index = df100.index * 10

print(df100)

########


files = glob.glob(f"../RDF/rdf_{atom}_*.txt")
df120 = pd.concat(
    [
        pd.read_csv(
            f,
            sep='\s+',
            skiprows=1,
            names=["coordinate", f"{f.split('_')[-3][:-1]}"],
        ).set_index("coordinate")
        for f in sorted(files, key=lambda f_: int(f_.split("_")[-3][:-1]))
    ],
    axis=1,
)


df120.index = df120.index * 10

print(df120)

####################################


# Split jet map 
jet = mplplot.get_cmap('jet')

colors = jet(np.linspace(0,1,19))
colors2 = jet(np.linspace(0.11111111,1.22,19))
colors3 = jet(np.linspace(0.22222222,1.22,19))
colors4 = jet(np.linspace(0.33333333, 1.35,19))
colors5 = jet(np.linspace(0.44444444, 1.51,19))
colors6 = jet(np.linspace(0.55555556, 1.62,19))


#############################################


fig, ax = plt.subplots(6, 1, figsize=(15,20))     
# Remove horizontal space between axes
fig.subplots_adjust(wspace=0, hspace=0)
plt.rcParams["axes.linewidth"]	= 2
plt.rcParams["mathtext.default"] = "regular"

for col in range(len(df20.columns)):
    ax[0].plot(df20.index, df20.iloc[:,col], c=colors[col])
    ax[0].tick_params(which="major", labelsize=17, width=1.5, length=6)
    ax[0].tick_params(which="minor", labelsize=17, width=1.5, length=4)
    ax[0].set_ylim(-0.4, 23)   
    ax[0].set_xlim(2, 14)
    ax[0].set_xticks(range(2, 15, 1))
    ax[0].set_ylabel('$g_{OO}(r)$', fontsize=24)
    #ax[0].set_title('20 K Deposition', fontsize=20)
    

# Create a set of inset Axes: these should fill the bounding box allocated to them.
ax2 = plt.axes([0,0,1,1])
# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax[0], [0.26,0.33,0.65,0.62])
ax2.set_axes_locator(ip)
 
for col in range(len(df20.columns)):
    ax2.plot(df20.index, df20.iloc[:,col], c=colors[col])
    ax2.set_xlim(2.3, 8)  
    ax2.set_ylim(-0.4, 4) 
    ax2.tick_params(which="major", labelsize=14, width=1.5, length=6)
    ax2.tick_params(which="minor", labelsize=14, width=1.5, length=4)

    # Mark the region corresponding to the inset axes on ax1 and draw lines
    # in grey linking the two axes.
    mark_inset(ax[0], ax2, loc1=3, loc2=4, fc="none", ec='0.5')

    
#####################################################################################
    
for col in range(len(df40.columns)):
    ax[1].plot(df40.index, df40.iloc[:,col], c=colors2[col])
    ax[1].tick_params(which="major", labelsize=17, width=1.5, length=6)
    ax[1].tick_params(which="minor", labelsize=17, width=1.5, length=4)
    ax[1].set_ylim(-0.4, 23)
    ax[1].set_xlim(2, 14)
    ax[1].set_xticks(range(2, 15, 1))
    ax[1].set_ylabel('$g_{OO}(r)$', fontsize=24)
    #ax[1].set_title('40 K Deposition', fontsize=20)




ax3 = plt.axes([0,0,1,1])
ip = InsetPosition(ax[1], [0.26,0.33,0.65,0.62])
ax3.set_axes_locator(ip)

for col in range(len(df40.columns)):
    ax3.plot(df40.index, df40.iloc[:,col], c=colors2[col])
    ax3.set_xlim(2.3, 8)
    ax3.set_ylim(-0.4, 4)
    ax3.tick_params(which="major", labelsize=14, width=1.5, length=6)
    ax3.tick_params(which="minor", labelsize=14, width=1.5, length=4)


#################################################################################

for col in range(len(df60.columns)):
    ax[2].plot(df60.index, df60.iloc[:,col], c=colors3[col])
    ax[2].tick_params(which="major", labelsize=17, width=1.5, length=6)
    ax[2].tick_params(which="minor", labelsize=17, width=1.5, length=4)
    ax[2].set_ylabel('$g_{OO}(r)$', fontsize=24)
    ax[2].set_ylim(-0.4, 23)
    ax[2].set_xlim(2, 14)
    ax[2].set_xticks(range(2, 15, 1))
    #ax[2].set_title('60 K Deposition', fontsize=20)



ax4 = plt.axes([0,0,1,1])
ip = InsetPosition(ax[2], [0.26,0.33,0.65,0.62])
ax4.set_axes_locator(ip)
 
for col in range(len(df60.columns)):
    ax4.plot(df60.index, df60.iloc[:,col], c=colors3[col])
    ax4.set_xlim(2.3, 8)
    ax4.set_ylim(-0.4, 4)
    ax4.tick_params(which="major", labelsize=14, width=1.5, length=6)
    ax4.tick_params(which="minor", labelsize=14, width=1.5, length=4)

    
#################################################################################    
    

for col in range(len(df80.columns)):
    ax[3].plot(df80.index, df80.iloc[:,col], c=colors4[col])
    ax[3].tick_params(which="major", labelsize=17, width=1.5, length=6)
    ax[3].tick_params(which="minor", labelsize=17, width=1.5, length=4)
    ax[3].set_ylim(-0.4, 23)
    ax[3].set_xlim(2, 14)
    ax[3].set_xticks(range(2, 15, 1))
    ax[3].set_ylabel('$g_{OO}(r)$', fontsize=24)
    #ax[3].set_title('80 K Deposition', fontsize=20)
    
    

ax5 = plt.axes([0,0,1,1])
ip = InsetPosition(ax[3], [0.26,0.33,0.65,0.62])
ax5.set_axes_locator(ip)
 
for col in range(len(df80.columns)):
    ax5.plot(df80.index, df80.iloc[:,col], c=colors4[col])
    ax5.set_xlim(2.3, 8)
    ax5.set_ylim(-0.4, 4)
    ax5.tick_params(which="major", labelsize=14, width=1.5, length=6)
    ax5.tick_params(which="minor", labelsize=14, width=1.5, length=4)

    
    
#################################################################################    
    
    
for col in range(len(df100.columns)):
    ax[4].plot(df100.index, df100.iloc[:,col], c=colors5[col])
    ax[4].tick_params(which="major", labelsize=17, width=1.5, length=6)
    ax[4].tick_params(which="minor", labelsize=17, width=1.5, length=4)
    ax[4].set_ylim(-0.4, 23)
    ax[4].set_xlim(2, 14)
    ax[4].set_xticks(range(2, 15, 1))
    ax[4].set_ylabel('$g_{OO}(r)$', fontsize=24)
    #ax[4].set_title('100 K Deposition', fontsize=20)
    
    

ax6 = plt.axes([0,0,1,1])
ip = InsetPosition(ax[4], [0.26,0.33,0.65,0.62])
ax6.set_axes_locator(ip)
 
for col in range(len(df100.columns)):
    ax6.plot(df100.index, df100.iloc[:,col], c=colors5[col])
    ax6.set_xlim(2.3, 8)
    ax6.set_ylim(-0.4, 4)
    ax6.tick_params(which="major", labelsize=14, width=1.5, length=6)
    ax6.tick_params(which="minor", labelsize=14, width=1.5, length=4)

    
##################################################################################  
    
for col in range(len(df120.columns)):
    ax[5].plot(df120.index, df120.iloc[:,col], c=colors6[col])
    ax[5].tick_params(which="major", labelsize=17, width=1.5, length=6)
    ax[5].tick_params(which="minor", labelsize=17, width=1.5, length=4)
    #ax[5].set_yticks([])
    ax[5].set_ylim(-0.4, 23)
    ax[5].set_xlim(2, 14)
    ax[5].set_xticks(range(2, 15, 1))
    ax[5].set_xlabel('r ($\AA$)', fontsize=24)
    ax[5].set_ylabel('$g_{OO}(r)$', fontsize=24)
    #ax[5].set_title('120 K Deposition', fontsize=20)


ax7 = plt.axes([0,0,1,1])
ip = InsetPosition(ax[5], [0.26,0.33,0.65,0.62])
ax7.set_axes_locator(ip)
 
for col in range(len(df120.columns)):
    ax7.plot(df120.index, df120.iloc[:,col], c=colors6[col])
    ax7.set_xlim(2.3, 8)
    ax7.set_ylim(-0.4, 4)
    ax7.tick_params(which="major", labelsize=14, width=1.5, length=6)
    ax7.tick_params(which="minor", labelsize=14, width=1.5, length=4)


##################################################################################


props = dict(boxstyle='round', facecolor='lightgrey', alpha=0.5)

fig.text(0.92, 0.97, '20 K', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=20, bbox=props)
fig.text(0.92, 0.807, '40 K', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=20, bbox=props)
fig.text(0.92, 0.646, '60 K', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=20, bbox=props)
fig.text(0.92, 0.485, '80 K', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=20, bbox=props)
fig.text(0.912, 0.322, '100 K', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=20, bbox=props)
fig.text(0.912, 0.16, '120 K', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=20, bbox=props)


scalarmappable = cm.ScalarMappable(cmap=cm.jet)
scalarmappable.set_array(range(20, 210, 10))
cbar_ax = fig.add_axes([1.02, 0.15, 0.02, 0.75])
cb = fig.colorbar(scalarmappable, cax = cbar_ax)
cb.ax.tick_params(labelsize=17)


mplplot.tight_layout()
fig.text(1.095, 0.478, 'T$_{anneal}$ (K)', horizontalalignment='left', verticalalignment='bottom', rotation='vertical', color = 'black', size=28)

#mplplot.savefig(f'../inset_RDF_{atom}_average.jpg', bbox_inches='tight', dpi=200)


