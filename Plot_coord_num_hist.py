# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.pyplot as mplplot
import scipy.stats as sp
import glob
from matplotlib import cm

files = glob.glob("../*.cn33")
df = pd.concat(
    [
        pd.read_csv(
            f,
            delim_whitespace=True,
            skiprows=4,
            nrows=7, 
            header=None,
            names=["coord_num", "count", f"{f.split('_')[-2][:-1]}"],
        ).set_index("coord_num")
        for f in sorted(files, key=lambda f_: int(f_.split("_")[-2][:-1]))
    ],
    axis=1,
)


######################

df = df.drop("count", axis=1)
df2 = df.drop([1, 6, 7])
df_1 = df.drop([1, 2, 3, 4, 5, 7])
df_1 = df_1 * 10
df_2 = df.drop([2, 3, 4, 5, 6])
df_2 = df_2 * 100

#######################

# Split jet map 
jet = mplplot.get_cmap('jet')
barWidth = 0.04

# Set position of bar on X axis 
br1 = df2.index
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]
br5 = [x + barWidth for x in br4]
br6 = [x + barWidth for x in br5]
br7 = [x + barWidth for x in br6]
br8 = [x + barWidth for x in br7]
br9 = [x + barWidth for x in br8]
br10 = [x + barWidth for x in br9]
br11 = [x + barWidth for x in br10]
br12 = [x + barWidth for x in br11]
br13 = [x + barWidth for x in br12]
br14 = [x + barWidth for x in br13]
br15 = [x + barWidth for x in br14]
br16 = [x + barWidth for x in br15]
br17 = [x + barWidth for x in br16]
br18 = [x + barWidth for x in br17]
br19 = [x + barWidth for x in br18]



br1_1 = df_1.index
br2_1 = [x + barWidth for x in br1_1] 
br3_1 = [x + barWidth for x in br2_1]
br4_1 = [x + barWidth for x in br3_1]
br5_1 = [x + barWidth for x in br4_1]
br6_1 = [x + barWidth for x in br5_1]
br7_1 = [x + barWidth for x in br6_1]
br8_1 = [x + barWidth for x in br7_1]
br9_1 = [x + barWidth for x in br8_1]
br10_1 = [x + barWidth for x in br9_1]
br11_1 = [x + barWidth for x in br10_1]
br12_1 = [x + barWidth for x in br11_1]
br13_1 = [x + barWidth for x in br12_1]
br14_1 = [x + barWidth for x in br13_1]
br15_1 = [x + barWidth for x in br14_1]
br16_1 = [x + barWidth for x in br15_1]
br17_1 = [x + barWidth for x in br16_1]
br18_1 = [x + barWidth for x in br17_1]
br19_1 = [x + barWidth for x in br18_1]



br1_2 = df_2.index
br2_2 = [x + barWidth for x in br1_2] 
br3_2 = [x + barWidth for x in br2_2]
br4_2 = [x + barWidth for x in br3_2]
br5_2 = [x + barWidth for x in br4_2]
br6_2 = [x + barWidth for x in br5_2]
br7_2 = [x + barWidth for x in br6_2]
br8_2 = [x + barWidth for x in br7_2]
br9_2 = [x + barWidth for x in br8_2]
br10_2 = [x + barWidth for x in br9_2]
br11_2 = [x + barWidth for x in br10_2]
br12_2 = [x + barWidth for x in br11_2]
br13_2 = [x + barWidth for x in br12_2]
br14_2 = [x + barWidth for x in br13_2]
br15_2 = [x + barWidth for x in br14_2]
br16_2 = [x + barWidth for x in br15_2]
br17_2 = [x + barWidth for x in br16_2]
br18_2 = [x + barWidth for x in br17_2]
br19_2 = [x + barWidth for x in br18_2]




mplplot.figure(dpi=1200)
mpl.rcParams["axes.linewidth"]	= 2
fig, ax = plt.subplots(figsize=(9,6))


plt.bar(br1, df2['20'], width = barWidth, color= jet(np.linspace(0,1,19)[0]))
plt.bar(br1_1, df_1['20'], width = barWidth, color= jet(np.linspace(0,1,19)[0]))
plt.bar(br1_2, df_2['20'], width = barWidth, color= jet(np.linspace(0,1,19)[0]))

plt.bar(br2, df2['30'], width = barWidth, color= jet(np.linspace(0,1,19)[1]))
plt.bar(br2_1, df_1['30'], width = barWidth, color= jet(np.linspace(0,1,19)[1]))
plt.bar(br2_2, df_2['30'], width = barWidth, color= jet(np.linspace(0,1,19)[1]))

plt.bar(br3, df2['40'], width = barWidth, color= jet(np.linspace(0,1,19)[2]))
plt.bar(br3_1, df_1['40'], width = barWidth, color= jet(np.linspace(0,1,19)[2]))
plt.bar(br3_2, df_2['40'], width = barWidth, color= jet(np.linspace(0,1,19)[2]))

plt.bar(br4, df2['50'], width = barWidth, color= jet(np.linspace(0,1,19)[3]))
plt.bar(br4_1, df_1['50'], width = barWidth, color= jet(np.linspace(0,1,19)[3]))
plt.bar(br4_2, df_2['50'], width = barWidth, color= jet(np.linspace(0,1,19)[3]))

plt.bar(br5, df2['60'], width = barWidth, color= jet(np.linspace(0,1,19)[4]))
plt.bar(br5_1, df_1['60'], width = barWidth, color= jet(np.linspace(0,1,19)[4]))
plt.bar(br5_2, df_2['60'], width = barWidth, color= jet(np.linspace(0,1,19)[4]))

plt.bar(br6, df2['70'], width = barWidth, color= jet(np.linspace(0,1,19)[5]))
plt.bar(br6_1, df_1['70'], width = barWidth, color= jet(np.linspace(0,1,19)[5]))
plt.bar(br6_2, df_2['70'], width = barWidth, color= jet(np.linspace(0,1,19)[5]))

plt.bar(br7, df2['80'], width = barWidth, color= jet(np.linspace(0,1,19)[6]))
plt.bar(br7_1, df_1['80'], width = barWidth, color= jet(np.linspace(0,1,19)[6]))
plt.bar(br7_2, df_2['80'], width = barWidth, color= jet(np.linspace(0,1,19)[6]))

plt.bar(br8, df2['90'], width = barWidth, color= jet(np.linspace(0,1,19)[7]))
plt.bar(br8_1, df_1['90'], width = barWidth, color= jet(np.linspace(0,1,19)[7]))
plt.bar(br8_2, df_2['90'], width = barWidth, color= jet(np.linspace(0,1,19)[7]))

plt.bar(br9, df2['100'], width = barWidth, color= jet(np.linspace(0,1,19)[8]))
plt.bar(br9_1, df_1['100'], width = barWidth, color= jet(np.linspace(0,1,19)[8]))
plt.bar(br9_2, df_2['100'], width = barWidth, color= jet(np.linspace(0,1,19)[8]))

plt.bar(br10, df2['110'], width = barWidth, color= jet(np.linspace(0,1,19)[9]))
plt.bar(br10_1, df_1['110'], width = barWidth, color= jet(np.linspace(0,1,19)[9]))
plt.bar(br10_2, df_2['110'], width = barWidth, color= jet(np.linspace(0,1,19)[9]))

plt.bar(br11, df2['120'], width = barWidth, color= jet(np.linspace(0,1,19)[10]))
plt.bar(br11_1, df_1['120'], width = barWidth, color= jet(np.linspace(0,1,19)[10]))
plt.bar(br11_2, df_2['120'], width = barWidth, color= jet(np.linspace(0,1,19)[10]))

plt.bar(br12, df2['130'], width = barWidth, color= jet(np.linspace(0,1,19)[11]))
plt.bar(br12_1, df_1['130'], width = barWidth, color= jet(np.linspace(0,1,19)[11]))
plt.bar(br12_2, df_2['130'], width = barWidth, color= jet(np.linspace(0,1,19)[11]))

plt.bar(br13, df2['140'], width = barWidth, color= jet(np.linspace(0,1,19)[12]))
plt.bar(br13_1, df_1['140'], width = barWidth, color= jet(np.linspace(0,1,19)[12]))
plt.bar(br13_2, df_2['140'], width = barWidth, color= jet(np.linspace(0,1,19)[12]))

plt.bar(br14, df2['150'], width = barWidth, color= jet(np.linspace(0,1,19)[13]))
plt.bar(br14_1, df_1['150'], width = barWidth, color= jet(np.linspace(0,1,19)[13]))
plt.bar(br14_2, df_2['150'], width = barWidth, color= jet(np.linspace(0,1,19)[13]))

plt.bar(br15, df2['160'], width = barWidth, color= jet(np.linspace(0,1,19)[14]))
plt.bar(br15_1, df_1['160'], width = barWidth, color= jet(np.linspace(0,1,19)[14]))
plt.bar(br15_2, df_2['160'], width = barWidth, color= jet(np.linspace(0,1,19)[14]))

plt.bar(br16, df2['170'], width = barWidth,  color= jet(np.linspace(0,1,19)[15]))
plt.bar(br16_1, df_1['170'], width = barWidth,  color= jet(np.linspace(0,1,19)[15]))
plt.bar(br16_2, df_2['170'], width = barWidth,  color= jet(np.linspace(0,1,19)[15]))

plt.bar(br17, df2['180'], width = barWidth, color= jet(np.linspace(0,1,19)[16]))
plt.bar(br17_1, df_1['180'], width = barWidth, color= jet(np.linspace(0,1,19)[16]))
plt.bar(br17_2, df_2['180'], width = barWidth, color= jet(np.linspace(0,1,19)[16]))

plt.bar(br18, df2['190'], width = barWidth, color= jet(np.linspace(0,1,19)[17]))
plt.bar(br18_1, df_1['190'], width = barWidth, color= jet(np.linspace(0,1,19)[17]))
plt.bar(br18_2, df_2['190'], width = barWidth, color= jet(np.linspace(0,1,19)[17]))

plt.bar(br19, df2['200'], width = barWidth, color= jet(np.linspace(0,1,19)[18]))
plt.bar(br19_1, df_1['200'], width = barWidth, color= jet(np.linspace(0,1,19)[18]))
plt.bar(br19_2, df_2['200'], width = barWidth, color= jet(np.linspace(0,1,19)[18]))


plt.xlim(1,8)   

ax.set_ylabel("Probability", fontsize=14)
ax.set_xlabel("Coordination Number", fontsize=14)
ax.tick_params(which="major", labelsize=14, width=2, length=6)
ax.tick_params(which="minor", labelsize=14, width=2, length=4)

barWidth2 = 1.35 

plt.xticks([r + barWidth2 for r in range(len(df.index))], ['1', '2', '3', '4', '5', '6', '7']) 


scalarmappable = cm.ScalarMappable(cmap=cm.jet)
scalarmappable.set_array(range(20, 210, 10))
cbar_ax = fig.add_axes([0.93, 0.15, 0.02, 0.7])
cb = fig.colorbar(scalarmappable, cax = cbar_ax)
cb.ax.tick_params(labelsize=14)
cb.set_label(label= 'T$_{anneal}$ (K)', size='x-large')


fig.text(0.74, 0.198, 'x 10', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=14)
fig.text(0.83, 0.198, 'x 100', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=14)
fig.text(0.17, 0.198, 'x 100', horizontalalignment='left', verticalalignment='bottom', rotation='horizontal', color = 'black', size=14)

mplplot.savefig('../OO_coord_num.jpg', bbox_inches='tight', dpi=600)



