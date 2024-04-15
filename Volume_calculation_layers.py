# -*- coding: utf-8 -*-


import math
import numpy as np
import pandas as pd

Rho_c = 0.94  #  in g/cm3
#a = 3.12506e-7  # in cm
N = 500  
NAvogadro=6.02214129 * 1e23  # 1/mol
mWater=18.0153  # in g

system = str('300Kwater_on_20Ksilic')
time = str('5')
RUN = str('RUN10')
heating = str('heating_200K')


df = pd.read_csv(f"../{system}/{RUN}/Heat_Ramps/{time}_ns/Analysis/Gro_files/{system}_{heating}_{time}ns.gro",
                   delim_whitespace=True,
                   header=None,
                   skiprows=302,
                   nrows=2000,
                   names=["name", "letters", "number", "x", "y", "z", "x vel", "y vel", "z vel"],
                   )


df = df.drop(["x vel", "y vel", "z vel"], axis=1)


df = df[(df['letters'] == 'MW')]

print(df)

ymax = df['y'].max()
ymin = df['y'].min()

xmax = df['x'].max()
xmin = df['x'].min()

zmin = df['z'].min()
zmax = df['z'].max()

print(zmin, zmax)


total_VOL_layer1 = []
total_VOL_layer2 = []
total_VOL_layer3 = []
total_VOL_layer4 = []
total_VOL_layer5 = []
total_VOL_layer6 = []


print(np.arange(15, 18.6, 0.6))


for i in np.arange(xmin, xmax, 0.312506):   # 0.275 nm is diameter of water molecule        0.312506 gets 10 bins across one axis
    
    for j in np.arange(ymin, ymax, 0.312506):
            
        #print("The X axis: \n", i)
        
        #print("The Y axis: \n", j)
        
        z_max_layer1 = np.max(df['z'][(df['x'] > i) & (df['x'] < j) & (df['y'] > i) & (df['y'] < j) & (df['z'] > 15) & (df['z'] < 15.6)])
        
        total_vol_layer1 = z_max_layer1 * 0.312506 * 0.312506
        
        total_VOL_layer1.append(total_vol_layer1)
        
        
        z_max_layer2 = np.max(df['z'][(df['x'] > i) & (df['x'] < j) & (df['y'] > i) & (df['y'] < j) & (df['z'] > 15.6) & (df['z'] < 16.2)])
        
        total_vol_layer2 = z_max_layer2 * 0.312506 * 0.312506
        
        total_VOL_layer2.append(total_vol_layer2)
        
        
        z_max_layer3 = np.max(df['z'][(df['x'] > i) & (df['x'] < j) & (df['y'] > i) & (df['y'] < j) & (df['z'] > 16.2) & (df['z'] < 16.8)])
        
        total_vol_layer3 = z_max_layer3 * 0.312506 * 0.312506
        
        total_VOL_layer3.append(total_vol_layer3)
        
        
        z_max_layer4 = np.max(df['z'][(df['x'] > i) & (df['x'] < j) & (df['y'] > i) & (df['y'] < j) & (df['z'] > 16.8) & (df['z'] < 17.4)])
        
        total_vol_layer4 = z_max_layer4 * 0.312506 * 0.312506
        
        total_VOL_layer4.append(total_vol_layer4)
        
        
        z_max_layer5 = np.max(df['z'][(df['x'] > i) & (df['x'] < j) & (df['y'] > i) & (df['y'] < j) & (df['z'] > 17.4) & (df['z'] < 18)])
        
        total_vol_layer5 = z_max_layer5 * 0.312506 * 0.312506
        
        total_VOL_layer5.append(total_vol_layer5)
        
        
        z_max_layer6 = np.max(df['z'][(df['x'] > i) & (df['x'] < j) & (df['y'] > i) & (df['y'] < j) & (df['z'] > 18) & (df['z'] < 18.6)])
        
        total_vol_layer6 = z_max_layer6 * 0.312506 * 0.312506
        
        total_VOL_layer6.append(total_vol_layer6)
    


finallist1 = list(dict.fromkeys(total_VOL_layer1))
finallist2 = list(dict.fromkeys(total_VOL_layer2))
finallist3 = list(dict.fromkeys(total_VOL_layer3))
finallist4 = list(dict.fromkeys(total_VOL_layer4))
finallist5 = list(dict.fromkeys(total_VOL_layer5))
finallist6 = list(dict.fromkeys(total_VOL_layer6))


dfvol1 = pd.DataFrame(finallist1)
dfvol1 = dfvol1.dropna()

print(dfvol1)

total_volume1 = dfvol1.sum()

dfvol2 = pd.DataFrame(finallist2)
dfvol2 = dfvol2.dropna()
total_volume2 = dfvol2.sum()

dfvol3 = pd.DataFrame(finallist3)
dfvol3 = dfvol3.dropna()
total_volume3 = dfvol3.sum()

dfvol4 = pd.DataFrame(finallist4)
dfvol4 = dfvol4.dropna()
total_volume4 = dfvol4.sum()

dfvol5 = pd.DataFrame(finallist5)
dfvol5 = dfvol5.dropna()
total_volume5 = dfvol5.sum()

dfvol6 = pd.DataFrame(finallist6)
dfvol6 = dfvol6.dropna()
total_volume6 = dfvol6.sum()


print(total_volume1, total_volume2, total_volume3, total_volume4, total_volume5, total_volume6)


#print("Volume (nm3) = ", total_volume)

#total_volume_cm = total_volume / 1e21

#print("Volume (cm3) = ", total_volume_cm)

#density = ( (N/NAvogadro) * mWater ) / total_volume_cm

#print("Density = ", density)

#porosity = 1 - ( density / Rho_c)

#print("Porosity = ", porosity)


########

#df_poros = pd.DataFrame(porosity)

#print(df_poros)


#df_dens = pd.DataFrame(density)

#print(df_dens)

#headers = ['Porosity', 'Density']

#last = pd.concat([df_poros, df_dens], axis=1, keys=headers)

#print(last)

#last.to_csv(f"../{system}/{RUN}/Heat_Ramps/{time}_ns/Analysis/Output_Files/porosity_{system}_{heating}_{time}ns.txt", index=False, header=True, sep=' ')

 ########
 
 
columns = ['Volume (nm3)']
 
df_vol1 = pd.DataFrame(total_volume1, columns=columns)

print(df_vol1)

df_vol2 = pd.DataFrame(total_volume2, columns=columns)
df_vol3 = pd.DataFrame(total_volume3, columns=columns)
df_vol4 = pd.DataFrame(total_volume4, columns=columns)
df_vol5 = pd.DataFrame(total_volume5, columns=columns)
df_vol6 = pd.DataFrame(total_volume6, columns=columns)

#df_vol1.to_csv(f"../{system}/{RUN}/Heat_Ramps/{time}_ns/Analysis/Output_Files/Porosity/layer1_volume_{system}_{heating}_{time}ns.txt", index=False, header=True, sep=' ')
#df_vol2.to_csv(f"../{system}/{RUN}/Heat_Ramps/{time}_ns/Analysis/Output_Files/Porosity/layer2_volume_{system}_{heating}_{time}ns.txt", index=False, header=True, sep=' ')
#df_vol3.to_csv(f"../{system}/{RUN}/Heat_Ramps/{time}_ns/Analysis/Output_Files/Porosity/layer3_volume_{system}_{heating}_{time}ns.txt", index=False, header=True, sep=' ')
#df_vol4.to_csv(f"../{system}/{RUN}/Heat_Ramps/{time}_ns/Analysis/Output_Files/Porosity/layer4_volume_{system}_{heating}_{time}ns.txt", index=False, header=True, sep=' ')
#df_vol5.to_csv(f"../{system}/{RUN}/Heat_Ramps/{time}_ns/Analysis/Output_Files/Porosity/layer5_volume_{system}_{heating}_{time}ns.txt", index=False, header=True, sep=' ')
#df_vol6.to_csv(f"../{system}/{RUN}/Heat_Ramps/{time}_ns/Analysis/Output_Files/Porosity/layer6_volume_{system}_{heating}_{time}ns.txt", index=False, header=True, sep=' ')


 
