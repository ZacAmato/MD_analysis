# -*- coding: utf-8 -*-
#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np


systems = {'300Kwater_on_40Ksilic'}
runs = {'RUN01'}          
Ttimes = {'10'}
ramps = {'10K'}

def Convert_gro_xyz(file, system, ramp, run, Ttime):
    
    gro_file = open('../{1}/{3}/Heat_Ramps/{4}_ns/Analysis/Gro_files/{1}_{0}_{4}ns.gro'.format(file, system, ramp, run, Ttime), 'r')

    xyz_file = open('../{1}/{3}/Heat_Ramps/{4}_ns/Analysis/XYZ/{1}_{0}_{4}ns.xyz'.format(file, system, ramp, run, Ttime), 'w')

    truc = gro_file.readline()
    osef = gro_file.readline()

    xyz_file.write(truc)
    xyz_file.write('2300 \n')

    z_0 = 10.0

    for iline in range(2300):
    
        line = gro_file.readline()
        line_cut = line.split()

        if iline == 0:
            z_0 = float(line_cut[5])

        if float(line_cut[5]) < z_0:
            z_0 = float(line_cut[5])

    gro_file.seek(0)
    osef = gro_file.readline()
    osef = gro_file.readline()
    
    for iline in range(2300):
    
        line = gro_file.readline()
        line_cut = line.split()
    
        if line_cut[1] == 'SZ':
        
            if iline < 100:
        
                line_write = 'SZ'+'\t'+f'{float(line_cut[3])*10:.5f}'+'\t'+f'{float(line_cut[4])*10:.5f}'+'\t'+f'{float(line_cut[5])*10 - ((z_0)*10):.5f}'+'\n'

            else:
            
                line_write = 'SO'+'\t'+f'{float(line_cut[3])*10:.5f}'+'\t'+f'{float(line_cut[4])*10:.5f}'+'\t'+f'{float(line_cut[5])*10 - ((z_0)*10):.5f}'+'\n'
            
            
        if line_cut[1] == 'SZ1':
        
            if iline < 100:
        
                line_write = 'SZ'+'\t'+f'{float(line_cut[3])*10:.5f}'+'\t'+f'{float(line_cut[4])*10:.5f}'+'\t'+f'{float(line_cut[5])*10 - ((z_0)*10):.5f}'+'\n'

            else:
            
                line_write = 'SO'+'\t'+f'{float(line_cut[3])*10:.5f}'+'\t'+f'{float(line_cut[4])*10:.5f}'+'\t'+f'{float(line_cut[5])*10 - ((z_0)*10):.5f}'+'\n'


        elif line_cut[1] == 'OW':

            line_write = 'OW'+'\t'+f'{float(line_cut[3])*10:.5f}'+'\t'+f'{float(line_cut[4])*10:.5f}'+'\t'+f'{float(line_cut[5])*10 - ((z_0)*10):.5f}'+'\n'

        
        elif line_cut[1] == 'HW1' or line_cut[1] == 'HW2':

            line_write = 'HW'+'\t'+f'{float(line_cut[3])*10:.5f}'+'\t'+f'{float(line_cut[4])*10:.5f}'+'\t'+f'{float(line_cut[5])*10 - ((z_0)*10):.5f}'+'\n'

        
        elif line_cut[1] == 'MW':

            line_write = 'QW'+'\t'+f'{float(line_cut[3])*10:.5f}'+'\t'+f'{float(line_cut[4])*10:.5f}'+'\t'+f'{float(line_cut[5])*10 - ((z_0)*10):.5f}'+'\n'

        xyz_file.write(line_write)
        
    xyz_file.close()
    gro_file.close()

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
                    Convert_gro_xyz(file, system, ramp, run, Ttime)
            
                if ramp == '10K':

                    file = 'relax_{0}K'.format(temp_system)
                    Convert_gro_xyz(file, system, ramp, run, Ttime)
                
        
   
