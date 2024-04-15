# -*- coding: utf-8 -*-
#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from os import listdir

systems = {'300Kwater_on_20Ksilic'}
runs = {'RUN10'}                # Skipped RUN09 20 Ksilic and went to 40Ksilic
Ttimes = {'10'}
ramps = {'10K'}

def find_Zmax(file, system, ramp, run, Ttime):

    xyz_file = open('../{1}/{3}/Heat_Ramps/{4}_ns/Analysis/XYZ/{1}_{0}_{4}ns.xyz'.format(file, system, ramp, run, Ttime), 'r')

    txt_file = open('../{1}/{3}/Heat_Ramps/{4}_ns/Analysis/XYZ/Zmax_{1}_{0}_{4}ns.txt'.format(file, system, ramp, run, Ttime), 'w')

    truc = xyz_file.readline()
    osef = xyz_file.readline()

    #txt_file.write(truc)

    Zmax = 0

    for iline in range(0, 300):
    
        line = xyz_file.readline()
        line_cut = line.split()
        
        if float(line_cut[3]) > Zmax:
            
            Zmax = float(line_cut[3])
            
    xyz_file.seek(0)
    osef = xyz_file.readline()
    osef = xyz_file.readline()
         
    line_write = f'{Zmax}'                                     
    
    txt_file.write(line_write)
        
    txt_file.close()
    xyz_file.close()

for ramp in ramps:
    
    for system in systems:
        
        for run in runs:
            
            for Ttime in Ttimes:
                
                system_cut = system.split('_')
                system_temp = system_cut[2].split('K')
                temp_system = int(system_temp[0])
                print(temp_system)
                
                for temp in range(temp_system+10, 210, 10):
            
                    print(ramp, system, temp)
                    file = 'heating_{0}K'.format(temp, ramp)
                    find_Zmax(file, system, ramp, run, Ttime)

                if ramp == '10K':

                    file = 'relax_{0}K'.format(temp_system)
                    find_Zmax(file, system, ramp, run, Ttime)
        
  
