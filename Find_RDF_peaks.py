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
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
from scipy.signal import find_peaks


atom = str('HW1HW2')
system = str('300Kwater_on_20Ksilic')
time = str('100')
file = str('heating_200K')


df = pd.read_csv(f"../{system}/{time}_ns/RDF/rdf_{atom}_{system}_{file}_{time}ns_averaged.txt",
                   delim_whitespace=True,
                   skiprows=1,
                   names=["r", "number"],
                   )



df['r'] = df['r'] * 10

print(df)

x = df['number']

peaks = find_peaks(x, prominence=0.4)  # 0.5 for relax

peak_pos = df["r"][peaks[0]]
peak_y = df["number"][peaks[0]]

print(peak_pos)


position_file = open(f'../{system}/{time}_ns/RDF/Peak_Positions/peak_position_{atom}_{system}_{file}_{time}ns.txt', 'w')

line = f'{peak_pos}'+'\n'+f'{peak_y}'+'\n'

position_file.write(line)



plt.figure(dpi=1200)
plt.figure(figsize= (9,6))
mpl.rcParams["axes.linewidth"]	= 1.5
fig,ax = plt.subplots()


ax.plot(df['r'], df['number'], color="#00008B")
ax.scatter(peak_pos, peak_y, color='r', marker='x')

ax.set_ylabel("$g_{OO}(r)$", fontsize=12)
ax.set_xlabel("r ($\AA$)", fontsize=12)
ax.tick_params(axis='x', labelsize=12, width=2, length=6)
ax.tick_params(axis='y', labelsize=12, width=2, length=6)
ax.set_xlim(1, 14)