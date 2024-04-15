# -*- coding: utf-8 -*-

#############ALL PYTHON ANALYSIS IN ONE SCRIPT#############################

import math
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from matplotlib import cm

systems = {'300Kwater_on_100Ksilic'}  
runs = {'RUN07'}  
Ttimes = {'100'}
ramps = {'10K'}


###########################CALC SURF OCC#################################################################################

def calc_surfocc(file, system, ramp, probe, run, Ttime, temp):


    traj_file = open('../{1}/{3}/Heat_Ramps/{4}_ns/Analysis/Trajectories/traj_{1}_{0}_{4}ns.gro'.format(file, system, ramp, run, Ttime), 'r')
    
    dist_file = open('../{1}/{3}/Heat_Ramps/{4}_ns/Analysis/Output_Files/Density/cumul/cumul_densnum_{1}_{0}_{4}ns.txt'.format(file, system, ramp, run, Ttime), 'r')


    osef = dist_file.readline()
    
    nlines_dist = 10
    
    number = np.zeros(nlines_dist)
    distances = np.zeros(nlines_dist)
    
    for iline in range(nlines_dist):

        line = dist_file.readline()
        line_cut = line.split()
        number[iline] = float(line_cut[0])
        distances[iline] = float(line_cut[1]) / 10

 
    for dist in distances:

        natoms = 2300

        nlines = 0
        noxy = 0

        for line in traj_file:
            nlines=nlines+1

        nframe = int(nlines/2303)

        traj_file.seek(0)

        time_frame = np.zeros(nframe)
        traj_file.seek(0)

        max_z_silic_fin = 0
        min_z_silic_fin = 0

        size_box_x = 0.0
        size_box_y = 0.0
        size_box_z = 0.0

        for iframe in range(nframe):

            line_time = traj_file.readline()
            line_time_cut = line_time.split()
            time_frame[iframe] = float(line_time_cut[5])

            osef = traj_file.readline()

            if iframe == nframe-1:

                first_line = traj_file.readline()
                first_line_cut = first_line.split()
                max_z_silic_fin = float(first_line_cut[5])
                min_z_silic_fin = float(first_line_cut[5])

                for iatom in range(natoms-1):
                    line_z = traj_file.readline()
                    line_z_cut = line_z.split()

                    if line_z_cut[1] == 'SZ' and float(line_z_cut[5]) < min_z_silic_fin:
                        min_z_silic_fin = float(line_z_cut[5])
                    elif line_z_cut[1] == 'SZ' and float(line_z_cut[5]) > max_z_silic_fin:
                        max_z_silic_fin = float(line_z_cut[5])

            else:

                for iatom in range(natoms):
                    osef = traj_file.readline()

            if iframe == 0:

                line_size = traj_file.readline()
                line_size_cut = line_size.split()
                size_box_x = float(line_size_cut[0])
                size_box_y = float(line_size_cut[1])
                size_box_z = float(line_size_cut[2])

            else:

                osef = traj_file.readline()

        traj_file.seek(0)

        surf_occ_above_ini = 0
        surf_occ_above_fin = 0
        surf_occ_below_ini = 0
        surf_occ_below_fin = 0

# Calcul surf occ at first frame

        cut_system = system.split('_')
        cut_temp = cut_system[2].split('K')
        temp_relax = int(cut_temp[0])
        traj_file_ini = open('../{0}/{2}/Heat_Ramps/{3}_ns/Analysis/Trajectories/traj_{0}_relax_{1}K_{3}ns.gro'.format(system, temp_relax, run, Ttime))

        osef = traj_file_ini.readline()
        osef = traj_file_ini.readline()
        
        first_line = traj_file_ini.readline()
        first_line_cut = first_line.split()
        max_z_silic_ini = float(first_line_cut[5])
        min_z_silic_ini = float(first_line_cut[5])

        for iatom in range(natoms - 1):
            line_z_ini = traj_file_ini.readline()
            line_z_ini_cut = line_z_ini.split()

            if line_z_ini_cut[1] == 'SZ' and float(line_z_ini_cut[5]) < min_z_silic_ini:
                min_z_silic_ini = float(line_z_ini_cut[5])
            elif line_z_ini_cut[1] == 'SZ' and float(line_z_ini_cut[5]) > max_z_silic_ini:
                max_z_silic_ini = float(line_z_ini_cut[5])

        traj_file_ini.seek(0)

        osef = traj_file_ini.readline()
        osef = traj_file_ini.readline()

        matrix_above_ini = np.zeros((100, 100))
        matrix_below_ini = np.zeros((100, 100))

        for iatom in range(natoms):

            line_atom = traj_file_ini.readline()
            line_atom_cut = line_atom.split()
            height = float(line_atom_cut[5])

            for ibin in range(100):
                for jbin in range(100):
                    x_0 = (ibin+0.5)*size_box_x/100
                    y_0 = (jbin + 0.5) * size_box_y / 100

                    if line_atom_cut[1] == 'OW':

                        if dist == -1:
                                radius = math.sqrt((float(line_atom_cut[3])-x_0) ** 2+(float(line_atom_cut[4])-y_0) ** 2)
                                if height > max_z_silic_ini and radius<probe:
                                    matrix_above_ini[ibin][jbin] = 0.0001
                                elif height < min_z_silic_ini and radius<probe:
                                    matrix_below_ini[ibin][jbin] = 0.0001

                        elif 0 < height-max_z_silic_ini < dist:
                                radius = math.sqrt((float(line_atom_cut[3]) - x_0) ** 2 + (float(line_atom_cut[4]) - y_0) ** 2)
                                if radius < probe:
                                    matrix_above_ini[ibin][jbin] = 0.0001

                        elif 0 > height-min_z_silic_ini > -dist:
                                radius = math.sqrt((float(line_atom_cut[3]) - x_0) ** 2 + (float(line_atom_cut[4]) - y_0) ** 2)
                                if radius < probe:
                                    matrix_below_ini[ibin][jbin] = 0.0001

        for ibin in range(100):
            for jbin in range(100):
                surf_occ_above_ini = surf_occ_above_ini + matrix_above_ini[ibin][jbin]
                surf_occ_below_ini = surf_occ_below_ini + matrix_below_ini[ibin][jbin]

        print(file, dist, probe, surf_occ_above_ini, surf_occ_below_ini)

        traj_file_ini.close()

        for iosef in range((nframe-1)*(natoms+3)):
               osef = traj_file.readline()

#calc surf occ for last frame

        osef = traj_file.readline()
        osef = traj_file.readline()

        matrix_above_fin = np.zeros((100, 100))
        matrix_below_fin = np.zeros((100, 100))

        for iatom in range(natoms):

            line_atom = traj_file.readline()
            line_atom_cut = line_atom.split()
            height = float(line_atom_cut[5])

            for ibin in range(100):
                for jbin in range(100):
                    x_0 = (ibin+0.5)*size_box_x/100
                    y_0 = (jbin + 0.5) * size_box_y / 100

                    if line_atom_cut[1] == 'OW':

                        if dist == -1:
                                radius = math.sqrt((float(line_atom_cut[3])-x_0) ** 2+(float(line_atom_cut[4])-y_0) ** 2)
                                if height > max_z_silic_fin and radius<0.275:
                                    matrix_above_fin[ibin][jbin] = 0.0001
                                elif height < min_z_silic_fin and radius<0.275:
                                    matrix_below_fin[ibin][jbin] = 0.0001

                        elif 0 < height-max_z_silic_fin < dist:
                                radius = math.sqrt((float(line_atom_cut[3]) - x_0) ** 2 + (float(line_atom_cut[4]) - y_0) ** 2)
                                if radius < 0.275:
                                    matrix_above_fin[ibin][jbin] = 0.0001

                        elif 0 > height-min_z_silic_fin > -dist:
                                radius = math.sqrt((float(line_atom_cut[3]) - x_0) ** 2 + (float(line_atom_cut[4]) - y_0) ** 2)
                                if radius < 0.275:
                                    matrix_below_fin[ibin][jbin] = 0.0001

        for ibin in range(100):
            for jbin in range(100):
                surf_occ_above_fin = surf_occ_above_fin + matrix_above_fin[ibin][jbin]
                surf_occ_below_fin = surf_occ_below_fin + matrix_below_fin[ibin][jbin]

        print(dist, probe, surf_occ_above_fin, surf_occ_below_fin)
        
        if dist == distances[0]:
            mol_num = 50
            
        if dist == distances[1]:
            mol_num = 100
            
        if dist == distances[2]:
            mol_num = 150
        
        if dist == distances[3]:
            mol_num = 200
            
        if dist == distances[4]:
            mol_num = 250
            
        if dist == distances[5]:
            mol_num = 300
            
        if dist == distances[6]:
            mol_num = 350
            
        if dist == distances[7]:
            mol_num = 400
            
        if dist == distances[8]:
            mol_num = 450
            
        if dist == distances[9]:
            mol_num = 500


        output_file = open('../{1}/{4}/Heat_Ramps/{5}_ns/Analysis/Output_Files/Surface_Occ/mol_num/surf_occ_{1}_{0}_{3}.out'.format(file, system, ramp, mol_num, run, Ttime), 'w')

        line_to_write = 'Surf_occ_above_ini (%)    Surf_occ_below_ini (%)      Surf_occ_above_fin (%)    Surf_occ_below_fin (%)    mol_num    Temp (K)  \n'
        output_file.write(line_to_write)

        line_to_write = 'Dist = {0} nm         probe = {1} nm\n'.format(dist, probe)
        output_file.write(line_to_write)

        line_frame = str(surf_occ_above_ini)+'   '+str(surf_occ_below_ini)+'     '+str(surf_occ_above_fin)+'   '+str(surf_occ_below_fin)+'  '+str(mol_num)+'  '+str(temp)+' \n'
        output_file.write(line_frame)

        output_file.close()

for ramp in ramps:
    
    for run in runs:
        
        for Ttime in Ttimes:
            
            for system in systems:
                    
                system_cut = system.split('_')
                system_temp = system_cut[2].split('K')
                temp_system = int(system_temp[0])

                for temp in range(temp_system+10, 150, 10):   #temp_system+10, 210, 10

                    print(ramp, system, temp)
                    file = 'heating_{0}K'.format(temp, ramp)
                    calc_surfocc(file, system, ramp, 0.275, run, Ttime, temp)

                if ramp == '10K':

                    file = 'relax_{0}K'.format(temp_system)
                    calc_surfocc(file, system, ramp, 0.275, run, Ttime, temp)
