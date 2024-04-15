# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import numpy as np
from scipy.integrate import simpson
from numpy import trapz
from scipy.integrate import quad
# typing is just for clarity
from typing import List
from scipy.optimize import curve_fit
from scipy.interpolate import *   



system = str('300Kwater_on_100Ksilic')
types = str('heating')
temp = str('200')
time = str('100')
run = str('RUN10') 


df = pd.read_csv(f"../{system}/{run}/Heat_Ramps/{time}_ns/Analysis/Output_Files/Density/densnum_{system}_{types}_{temp}K_{time}ns.xvg",
                   delim_whitespace=True,
                   skiprows=24,
                   names=["coord", "zdens"],
                   ).set_index('coord')


df.index = df.index - 15

df.index = df.index * 10

df = df.loc[(df!=0).any(axis=1)]

print(df)


###############


area_array = []

for i in np.arange(3, 44, 1):  
    
    area_trap_layer = np.trapz(df['zdens'][1:i])
    
    area_array.append(area_trap_layer)
    

finallist = list(dict.fromkeys(area_array))

finallist.insert(0, 0)



print(finallist)

df['cumul'] = finallist

#print(df)

#############

First_50 = np.interp(50, df['cumul'], df.index)

#print("50 Oxygens = ", First_50)



First_100 = np.interp(100, df['cumul'], df.index)

#print("100 Oxygens = ", First_100)


First_150 = np.interp(150, df['cumul'], df.index)

#print("150 Oxygens = ", First_150)


First_200 = np.interp(200, df['cumul'], df.index)

#print("200 Oxygens = ", First_200)


First_250 = np.interp(250, df['cumul'], df.index)

#print("250 Oxygens = ", First_250)



First_300 = np.interp(300, df['cumul'], df.index)

#print("300 Oxygens = ", First_300)


First_350 = np.interp(350, df['cumul'], df.index)

#print("350 Oxygens = ", First_350)


First_400 = np.interp(400, df['cumul'], df.index)

#print("400 Oxygens = ", First_400)



First_450 = np.interp(450, df['cumul'], df.index)

#print("450 Oxygens = ", First_450)


First_500 = np.interp(500, df['cumul'], df.index)

#print("500 Oxygens = ", First_500)


data = [[50, First_50], [100, First_100], [150, First_150], [200, First_200], [250, First_250], [300, First_300], [350, First_350], [400, First_400], [450, First_450], [500, First_500]]

df_cumul = pd.DataFrame(data, columns = ['number', 'distance'])

print("CUMUL DF: \n", df_cumul)


df_cumul.to_csv(f"../{system}/{run}/Heat_Ramps/{time}_ns/Analysis/Output_Files/Density/cumul/cumul_densnum_{system}_{types}_{temp}K_{time}ns.txt", index=False, header=True, sep=' ')


##############################################################################################


plt.figure(dpi=1200)
mpl.rcParams["axes.linewidth"]	= 2
ax = plt.figure(figsize= (8,6)).add_subplot(1, 1, 1)


ax.plot(df.index, df['cumul'], label='data')
#ax.plot(np.polyval(poly, df.index), color='orange', label='fit')

#plt.plot(df.index, func(df.index, *popt), 'r--', label='fit')

#ax.plot(df.index, df['zdens'], color='k', linewidth=0.5)
#ax.fill_between(filled_x, y1=filled_y)

ax.set_xlabel("Distance from surface ($\AA$)", fontsize=14)
ax.set_ylabel("Cumulative O Number", fontsize=14)
ax.tick_params(which="major", labelsize=12, width=2, length=6)
ax.tick_params(which="minor", labelsize=12, width=2, length=4)

#plt.legend(frameon=False)

#plt.savefig(f'../{system}/{run}/Heat_Ramps/{time}_ns/Analysis/Images/Zdens_Cumul/zdens_cumul_{system}_{types}_{temp}K.png', bbox_inches='tight', dpi=1200)