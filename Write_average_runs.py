# -*- coding: utf-8 -*-
import numpy as np


systems = {'300Kwater_on_20Ksilic'}  
runs={'RUN01', 'RUN02', 'RUN03', 'RUN04', 'RUN05', 'RUN06', 'RUN07', 'RUN08', 'RUN09', 'RUN10'}    #'RUN01', 'RUN02', 'RUN03', 'RUN04', 'RUN05', 'RUN06', 'RUN07', 'RUN08', 'RUN09', 'RUN10'
Ttimes = {'10'}
ramps = {'10K'}
radii = {1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5}
systeM = str('300Kwater_on_20Ksilic')
timE = str('10')

heights_results_file = open(f'../{systeM}/{timE}_ns/heights/Bash_heights_{systeM}_averaged.txt', 'w')
porosity_results_file = open(f'../{systeM}/{timE}_ns/porosity/porosity_density_{systeM}_averaged.txt', 'w')
SSA_results_file = open(f'../{systeM}/{timE}_ns/SSA/SSA_{systeM}_averaged.txt', 'w')


def write_heights(file, system, run, ramp, Ttime):

    heights_file = open('../{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Output_Files/Bash/Heights/heights_{2}_{0}_{4}ns.txt'.format(file, run, system, ramp, Ttime), 'r')
    
    
    line_heights = heights_file.readline()
    line_heights_cut = line_heights.split()
    Max = float(line_heights_cut[3])
    
    line_heights2 = heights_file.readline()
    line_heights_cut2 = line_heights2.split()
    Med = float(line_heights_cut2[3])
    
    line_heights3 = heights_file.readline()
    line_heights_cut3 = line_heights3.split()
    Av = float(line_heights_cut3[3])
    
    if file == 'heating_{0}K'.format(temp):
        
        line = f'{run}'+'\t'+f'{temp}'+'\t'+f'{Max}'+'\t'+f'{Med}'+'\t'+f'{Av}'+'\n'
        
        heights_results_file.write(line)
    
    if file == 'relax_{0}K'.format(temp_system):
        
        line = f'{run}'+'\t'+f'{temp_system}'+'\t'+f'{Max}'+'\t'+f'{Med}'+'\t'+f'{Av}'+'\n'
        
        heights_results_file.write(line)
    

for system in systems:

    for run in runs:
        
        for ramp in ramps:
            
            for Ttime in Ttimes:
                
                print(run)
            
                system_cut = system.split('_')
                system_temp = system_cut[2].split('K')
                temp_system = int(system_temp[0])
                print(temp_system)
                temp_range = range(temp_system, 210, 10)
                ntemp = len(temp_range)
                    
            
                for itemp in range(1, ntemp):
                    
                    temp = temp_range[itemp]            
                    file = 'heating_{0}K'.format(temp)
                    write_heights(file, system, run, ramp, Ttime)
            
                file = 'relax_{0}K'.format(temp_system)
                write_heights(file, system, run, ramp, Ttime)
            
            
            
            
def write_poros(file, system, run, ramp, Ttime):

    poros_file = open('../{1}/{2}/Heat_Ramps/{4}_ns/Analysis/Output_Files/Bash/Porosity/density-porosity_{1}_{0}_{4}ns.txt'.format(file, system, run, ramp, Ttime), 'r')
        
    line_poros = poros_file.readline()
    line_poros_cut = line_poros.split()
    dens = float(line_poros_cut[4])
    
    line_poros2 = poros_file.readline()
    line_poros_cut2 = line_poros2.split()
    poros = float(line_poros_cut2[4])
    
    if file == 'heating_{0}K'.format(temp):
        
        line = f'{run}'+'\t'+f'{temp}'+'\t'+f'{dens}'+'\t'+f'{poros}'+'\n'
        
        porosity_results_file.write(line)
    
    if file == 'relax_{0}K'.format(temp_system):
        
        line = f'{run}'+'\t'+f'{temp_system}'+'\t'+f'{dens}'+'\t'+f'{poros}'+'\n'
        
        porosity_results_file.write(line)



for run in runs:

    for system in systems:
        
        for ramp in ramps:
            
            for Ttime in Ttimes:
                
                print(run, ramp)
                
                system_cut = system.split('_')
                system_temp = system_cut[2].split('K')
                temp_system = int(system_temp[0])
                print(temp_system)
                temp_range = range(temp_system, 210, 10)
                ntemp = len(temp_range)
                
                for itemp in range(1, ntemp):
                    
                    temp = temp_range[itemp]            
                    file = 'heating_{0}K'.format(temp)
                    write_poros(file, system, run, ramp, Ttime)
                    
                file = 'relax_{0}K'.format(temp_system)
                write_poros(file, system, run, ramp, Ttime)
            
  
            
def write_sphere_access(file, system, run, ramp, Ttime, rad):

    sphere_file = open('../{1}/{2}/Heat_Ramps/{4}_ns/Analysis/Output_Files/Bash/SASA/{1}_{0}_SASA_Sphere-{5}_iCell-3-by-3_MirrorSep-0.0.txt'.format(file, system, run, ramp, Ttime, rad), 'r')
    
    density_file = open('../{1}/{2}/Heat_Ramps/{4}_ns/Analysis/Output_Files/Bash/Porosity/density-porosity_{1}_{0}_{4}ns.txt'.format(file, system, run, ramp, Ttime), 'r')

    for iosef in range(11):
        osef = sphere_file.readline()
    
    line_sphere = sphere_file.readline()
    line_sphere_cut = line_sphere.split()
    SASA_ini = float(line_sphere_cut[0])
    
    line_density = density_file.readline()
    line_density_cut = line_density.split()
    density = float(line_density_cut[4])
    
    H2O_mass = 500 * (2.989*(10^(-23)))     #this is in grams so will get A^2/g but would want m^2/g
    SSA_grams = ((SASA_ini)*(1*10^(-20)))/H2O_mass   #trying to convert the square angstrom to square metres
    SSA_vol = (SSA_grams) / density
    
    if file == 'heating_{0}K'.format(temp):
        
        line = f'{run}'+'\t'+f'{temp}'+'\t'+f'{rad}'+'\t'+f'{SSA_vol}'+'\n'
        
        SSA_results_file.write(line)
    
    if file == 'relax_{0}K'.format(temp_system):
        
        line = f'{run}'+'\t'+f'{temp_system}'+'\t'+f'{rad}'+'\t'+f'{SSA_vol}'+'\n'
        
        SSA_results_file.write(line)
    
    

for run in runs:

    for system in systems:
        
        for ramp in ramps:
            
            for rad in radii:
                
                for Ttime in Ttimes:
                    
                    print(run, ramp, rad)
                
                    system_cut = system.split('_')
                    system_temp = system_cut[2].split('K')
                    temp_system = int(system_temp[0])
                    print(temp_system)
                    temp_range = range(temp_system, 210, 10)
                    ntemp = len(temp_range)
                
                    for itemp in range(1, ntemp):
                        
                        print(temp)
                    
                        temp = temp_range[itemp]            
                        file = 'heating_{0}K'.format(temp)
                        write_sphere_access(file, system, run, ramp, Ttime, rad)
                    
                    file = 'relax_{0}K'.format(temp_system)
                    write_sphere_access(file, system, run, ramp, Ttime, rad)
                
                        

                
   