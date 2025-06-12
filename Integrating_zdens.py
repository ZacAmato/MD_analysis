# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import numpy as np
from scipy.integrate import simpson
from numpy import trapz
from scipy.integrate import quad
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

area_array = []

for i in np.arange(3, 44, 1):  
    
    area_trap_layer = np.trapz(df['zdens'][1:i])
    
    area_array.append(area_trap_layer)
    

finallist = list(dict.fromkeys(area_array))

finallist.insert(0, 0)
df['cumul'] = finallist

#############

First_50 = np.interp(50, df['cumul'], df.index)
First_100 = np.interp(100, df['cumul'], df.index)
First_150 = np.interp(150, df['cumul'], df.index)
First_200 = np.interp(200, df['cumul'], df.index)
First_250 = np.interp(250, df['cumul'], df.index)
First_300 = np.interp(300, df['cumul'], df.index)
First_350 = np.interp(350, df['cumul'], df.index)
First_400 = np.interp(400, df['cumul'], df.index)
First_450 = np.interp(450, df['cumul'], df.index)
First_500 = np.interp(500, df['cumul'], df.index)

data = [[50, First_50], [100, First_100], [150, First_150], [200, First_200], [250, First_250], [300, First_300], [350, First_350], [400, First_400], [450, First_450], [500, First_500]]

df_cumul = pd.DataFrame(data, columns = ['number', 'distance'])

df_cumul.to_csv(f"../{system}/{run}/Heat_Ramps/{time}_ns/Analysis/Output_Files/Density/cumul/cumul_densnum_{system}_{types}_{temp}K_{time}ns.txt", index=False, header=True, sep=' ')
