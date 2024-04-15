# -*- coding: utf-8 -*-

#############ALL PYTHON ANALYSIS IN ONE SCRIPT#############################

import math
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from matplotlib import cm

systems = {'300Kwater_on_20Ksilic'}
runs = {'RUN05'}
Ttimes = {'100'}
ramps = {'10K'}
 

#####################CALCULATE HEIGHTS#######################################################

def calc_heights(file, run, system, ramp, Ttime):
   
    traj_file = open('../{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Trajectories/traj_{2}_{0}_{4}ns.gro'.format(file, run, system, ramp, Ttime), 'r')

    natoms = 2300

    nlines = 0
    noxy = 0

    for line in traj_file:
        nlines=nlines+1

    nframe = int(nlines/2303)

    traj_file.seek(0)

    time_frame = np.zeros(nframe)
    max_height = np.zeros(nframe)
    min_height = np.zeros(nframe)
    minmax_height = np.zeros(nframe)
    aver_height_max = np.zeros(nframe)
    aver_height_min = np.zeros(nframe)

    traj_file.seek(0)

    for iframe in range(nframe):

        line_time = traj_file.readline()
        line_time_cut = line_time.split()
        time_frame[iframe] = float(line_time_cut[5])

        osef = traj_file.readline()

        line_ref = traj_file.readline()
        line_ref_cut = line_ref.split()
        ref_height = float(line_ref_cut[5])

        min_height[iframe] = 40.0

        for iatom in range(natoms-1):

            line_atom = traj_file.readline()
            line_atom_cut = line_atom.split()
            z_atom = float(line_atom_cut[5])

            if min_height[iframe] > z_atom:

               min_height[iframe] = z_atom

            if max_height[iframe] < z_atom:

               max_height[iframe] = z_atom

            minmax_height[iframe] = max_height[iframe]-min_height[iframe]

        max_height[iframe] = max_height[iframe]-ref_height
        min_height[iframe] = min_height[iframe]-ref_height

        osef = traj_file.readline()

    traj_file.seek(0)

    noxy_max = 0
    noxy_min = 0

    osef = traj_file.readline()
    osef = traj_file.readline()

    line_ref = traj_file.readline()
    line_ref_cut = line_ref.split()
    ref_height = float(line_ref_cut[5])

    for iatom in range(natoms-1):
        line_atom = traj_file.readline()
        line_atom_cut = line_atom.split()
        z_atom = float(line_atom_cut[5])
        if line_atom_cut[1] == 'OW' and z_atom - ref_height > 0:
            noxy_max = noxy_max+1
        elif line_atom_cut[1] == 'OW' and z_atom - ref_height < 0:
            noxy_min = noxy_min+1

    traj_file.seek(0)

    for iframe in range(nframe):

        osef = traj_file.readline()
        osef = traj_file.readline()
        line_ref = traj_file.readline()
        line_ref_cut = line_ref.split()
        ref_height = float(line_ref_cut[5])

        for iatom in range(natoms - 1):
            line_atom = traj_file.readline()
            line_atom_cut = line_atom.split()
            z_atom = float(line_atom_cut[5])

            if line_atom_cut[1] == 'OW' and z_atom - ref_height > 0:
                aver_height_max[iframe] = aver_height_max[iframe]+z_atom/noxy_max
            elif line_atom_cut[1] == 'OW' and z_atom - ref_height < 0:
                aver_height_min[iframe] = aver_height_min[iframe]+z_atom/noxy_min

        osef = traj_file.readline()

    output_file = open('../{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Output_Files/Heights/heights_{2}_{0}_{4}ns.out'.format(file, run, system, ramp, Ttime), 'w')

    line_to_write = 'Time     Max Height (A)   Min Height (A)    Max-Min (A)   Aver Max (A)    Aver Min (A)\n'
    output_file.write(line_to_write)

    for iframe in range(nframe):

        line_frame = str(time_frame[iframe])+'   '+str(max_height[iframe])+'   '+str(min_height[iframe])+'   '+str(minmax_height[iframe])+'   '+str(aver_height_max[iframe])+'   '+str(aver_height_min[iframe])+' \n'
        output_file.write(line_frame)

    output_file.close()

for ramp in ramps:
    
    for run in runs:
        
        for Ttime in Ttimes:
            
            for system in systems:
                
                system_cut = system.split('_')
                system_temp = system_cut[2].split('K')
                temp_system = int(system_temp[0])
                
                for temp in range(temp_system+10, 210, 10):
                    
                    print(ramp, system, temp)
                    file = 'heating_{0}K'.format(temp, ramp)
                    calc_heights(file, run, system, ramp, Ttime)
                    
                if ramp == '10K':
                    
                    file = 'relax_{0}K'.format(temp_system)
                    calc_heights(file, run, system, ramp, Ttime)




##############PLOT SIMPLE HEIGHTS PLOT###################################################################



def Simple_Heights(file, run, system, ramp, Ttime):
    
    heights_file = open('../{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Output_Files/Heights/heights_{2}_{0}_{4}ns.out'.format(file, run, system, ramp, Ttime), 'r')
    
    nlines = -1
    for line in heights_file:
        if line != '':
            nlines = nlines + 1
    
    heights_file.seek(0)
    osef = heights_file.readline()
    
    time = np.zeros(nlines)
    maxheight = np.zeros(nlines)
    
    for iline in range(nlines):
    
        line_heights = heights_file.readline()
        line_heights_cut = line_heights.split()
        maxheight [iline] = float(line_heights_cut[1])
        time [iline] = float(line_heights_cut[0])
    
    plt.plot(time, maxheight)
    plt.xlabel('Time (ps)')
    plt.ylabel('Max Height (A)')
    plt.savefig('../{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Images/Heights/heights_{2}_{0}_{4}ns.png'.format(file, run, system, ramp, Ttime))
    plt.close()

for ramp in ramps:
    
    for run in runs:
        
        for Ttime in Ttimes:
            
            for system in systems:
                
                system_cut = system.split('_')
                system_temp = system_cut[2].split('K')
                temp_system = int(system_temp[0])
                print(temp_system)
                
                for temp in range(temp_system+10, 210, 10):
                    
                    print(ramp, system, temp)
                    file = 'heating_{0}K'.format(temp, ramp)
                    Simple_Heights(file, run, system, ramp, Ttime)
                    
                if ramp == '10K':
                    
                    file = 'relax_{0}K'.format(temp_system)
                    Simple_Heights(file, run, system, ramp, Ttime)
                    
                    
###################PLOT TRAJ MAXHEIGHT STEP########################################################################

maxtypes = {'MinMax', 'Max', 'Min'}


def plot_maxheights(file, system, ramp, maxtype, run, Ttime):

    heights_file = open('../{1}/{3}/Heat_Ramps/{4}_ns/Analysis/Output_Files/Heights/heights_{1}_{0}_{4}ns.out'.format(file, system, ramp, run, Ttime), 'r')

    nlines = -1
    for line in heights_file:
        if line != '':
            nlines = nlines + 1

    heights_file.seek(0)
    osef = heights_file.readline()

    time_frame = np.zeros(nlines)
    maxheights = np.zeros(nlines)

    for iline in range(nlines):

        line_heights = heights_file.readline()
        line_heights_cut = line_heights.split()
        time_frame[iline] = float(line_heights_cut[0])

        if maxtype == 'Max':

            maxheights[iline] = float(line_heights_cut[1])

        elif maxtype == 'Min':

            maxheights[iline] = float(line_heights_cut[2])

        elif maxtype == 'MinMax':

            maxheights[iline] = float(line_heights_cut[3])

    plt.plot(time_frame, maxheights, c=cm.jet((temp - 10) / (200 - 10)))

for ramp in ramps:

    for system in systems:
        
        for run in runs:
            
            for Ttime in Ttimes:
                
                for maxtype in maxtypes:
                    
                    print(system)
            
                    system_cut = system.split('_')
                    system_temp = system_cut[2].split('K')
                    temp_system = int(system_temp[0])

                    temp_range = range(temp_system, 210, 10)
                    ntemp = len(temp_range)
                    temp = int(temp_system)
         
                    file = 'relax_{0}K'.format(temp_system)
                    plot_maxheights(file, system, ramp, maxtype, run, Ttime)

                    for itemp in range(1, ntemp):
                
                        temp = temp_range[itemp]
                        file = 'heating_{0}K'.format(temp)
                        plot_maxheights(file, system, ramp, maxtype, run, Ttime)


                    plt.xlabel('Time (ps)')
                    plt.ylabel('Ice Thickness (A)')
                    plt.title('Ice Thickness')
                    # setup the colorbar
                    scalarmappaple = cm.ScalarMappable(cmap=cm.jet)
                    scalarmappaple.set_array(range(10, 210, 10))
                    plt.colorbar(scalarmappaple, label= 'Temperature (K)')
                    plt.savefig('D:/My_Work/XY_PBC_Runs/Structure_1/{1}/{4}/Heat_Ramps/{5}_ns/Analysis/Images/Heights/{3}_{1}_{5}ns.png'.format(file, system, ramp, maxtype, run, Ttime), dpi=1200)
                    plt.close()                    
                    
                    
        
####################PLOT TRAJ MAXHEIGHT LAST POINT###############################################################


maxtypes = {'MinMax', 'Max', 'Min'}


def plot_maxheights_lastpoint(file, run, system, ramp, Ttime):

    heights_file = open('../{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Output_Files/Heights/heights_{2}_{0}_{4}ns.out'.format(file, run, system, ramp, Ttime), 'r')

    nlines = -1
    for line in heights_file:
        if line != '':
            nlines = nlines + 1

    heights_file.seek(0)
    osef = heights_file.readline()

    for iline in range(nlines-1):

        osef = heights_file.readline()

    line_heights = heights_file.readline()
    line_heights_cut = line_heights.split()

    maxheight = float(line_heights_cut[1])
    minheight = float(line_heights_cut[2])
    minmax = float(line_heights_cut[3])

    return maxheight, minheight, minmax

for ramp in ramps:
    
    for run in runs:
        
        for Ttime in Ttimes:
            
            for system in systems:
                
                print(ramp, system)
                
                system_cut = system.split('_')
                system_temp = system_cut[2].split('K')
                temp_system = int(system_temp[0])

                temp_range = range(temp_system, 210, 10)
                ntemp = len(temp_range)

                maxheights_last = np.zeros(ntemp)
                minheights_last = np.zeros(ntemp)
                minmax_last = np.zeros(ntemp)

                file = 'relax_{0}K'.format(temp_system)
                maxheights_last[0], minheights_last[0], minmax_last[0] = plot_maxheights_lastpoint(file, run, system, ramp, Ttime)

                for itemp in range(1, ntemp):

                    temp = temp_range[itemp]
                    file = 'heating_{0}K'.format(temp, ramp)
                    maxheights_last[itemp], minheights_last[itemp], minmax_last[itemp] = plot_maxheights_lastpoint(file, run, system, ramp, Ttime)


                plt.scatter(temp_range, maxheights_last)

                plt.xlabel('Temperature')
                #plt.xlim([25, 205])
                plt.ylabel('Ice Thickness (nm)')
                plt.title('Ice Thickness')
                plt.savefig('../{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Images/Heights/Max_{2}.png'.format(file, run, system, ramp, Ttime), dpi=1200)
                plt.close()

                plt.scatter(temp_range, minheights_last)

                plt.xlabel('Temperature')
                #plt.xlim([25, 205])
                plt.ylabel('Ice Thickness (nm)')
                plt.title('Ice Thickness')
                plt.savefig('../{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Images/Heights/Min_{2}.png'.format(file, run, system, ramp, Ttime), dpi=1200)
                plt.close()

                plt.scatter(temp_range, minmax_last)

                plt.xlabel('Temperature')
                #plt.xlim([25, 205])
                plt.ylabel('Ice Thickness (nm)')
                plt.title('Ice Thickness')
                plt.savefig('../{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Images/Heights/MinMax_{2}.png'.format(file, run, system, ramp, Ttime), dpi=1200)
                plt.close()
                
    


####################CALC DENSITY MAPS###########################################################


ndens = 19
#binning of the density
nbin = 500


def calc_density(file, system, ramp, run, Ttime, ndens, nbin):

    traj_file = open('../{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Trajectories/traj_{2}_{0}_{4}ns.gro'.format(file, run, system, ramp, Ttime), 'r')

    natoms = 2300 

    nlines = 0

    for line in traj_file:
        nlines=nlines+1

    nframe = int(nlines/2303)
    nframe_densities = ndens

    traj_file.seek(0)

    for iosef in range(2302):

        osef = traj_file.readline()

    line_size = traj_file.readline()
    line_size_cut = line_size.split()
    size_Z = float(line_size_cut[2])

    Z_range = np.zeros(nbin)

    for ibin in range(nbin):
        Z_range[ibin] = ibin*size_Z/nbin - size_Z/(2)

    traj_file.seek(0)

    time_frame = np.zeros(nframe_densities)

    mat_dens = np.zeros((nframe_densities, nbin))

    for iframe in range(nframe_densities):

        line_time = traj_file.readline()
        line_time_cut = line_time.split()
        time_frame[iframe] = float(line_time_cut[5])
        print(iframe)
        print(line_time)
        
        osef = traj_file.readline()

        line_ref = traj_file.readline()
        line_ref_cut = line_ref.split()
        ref_height = float(line_ref_cut[5])

        for iatom in range(natoms-1):

            line_atom = traj_file.readline()
            line_atom_cut = line_atom.split()
            z_atom = float(line_atom_cut[5])

            for ibin in range(nbin):

                if Z_range[ibin] <= z_atom - ref_height < Z_range[ibin+1] and line_atom_cut[1] == 'OW':

                    mat_dens[iframe][ibin] = mat_dens[iframe][ibin]+1

        osef = traj_file.readline()

        for iosef in range(2303*(int((nframe-nframe_densities)/nframe_densities-1))):

            osef = osef = traj_file.readline()

    return time_frame, mat_dens, Z_range

#then the procedure to automate the calculation on the list of systems and ramps ; and plotting the maps.

for ramp in ramps:
    
    for run in runs:
        
        for Ttime in Ttimes:
            
            for system in systems:
                
                system_cut = system.split('_')
                system_temp = system_cut[2].split('K')
                temp_system = int(system_temp[0])
                mat_temp = np.zeros((len(range(temp_system, 210, 10)),nbin))

                for temp in range(temp_system + 10, 210, 10):

                    itemp = int((temp-temp_system)/10)
                    print(ramp, system, temp)
                    file = 'heating_{0}K'.format(temp, ramp)
                    times, densities_map, Z_range = calc_density(file, system, ramp, run, Ttime, ndens, nbin)

                    plt.imshow(densities_map, extent=[-15, 15, 500000, 0], aspect='auto', cmap=cm.jet)
                    plt.xlim([0, 3])
                    plt.ylim([500000, 0])                                                                                                                                                                                                                                                                                                                                                                           
                    plt.xlabel('Ice Z Coordinate')
                    plt.ylabel('Time (ps)')
                    scalarmappaple = cm.ScalarMappable(cmap=cm.jet)
                    plt.colorbar(scalarmappaple, label='Oxygen Density')
                    plt.tight_layout()
                    plt.savefig('../{1}/{2}/Heat_Ramps/{3}_ns/Analysis/Images/DensityMaps/Map_density_vtime_{0}_{3}ns.png'.format(file, system, run, Ttime), dpi=1200)
                    plt.close()

                    mat_temp[itemp][:] = densities_map[-1][:]

                if ramp == '10K':

                    file = 'relax_{0}K'.format(temp_system)
                    times, densities_map, Z_range = calc_density(file, system, ramp, run, Ttime, ndens, nbin)

                    plt.imshow(densities_map, extent=[-15, 15, 500000, 0], aspect='auto', cmap=cm.jet)
                    plt.xlim([0, 3])
                    plt.ylim([500000, 0])
                    plt.xlabel('Ice Z Coordinate')
                    plt.ylabel('Time (ps)')              
                    scalarmappaple = cm.ScalarMappable(cmap=cm.jet)
                    plt.colorbar(scalarmappaple, label='Oxygen Density')
                    plt.tight_layout()
                    plt.savefig('../{1}/{2}/Heat_Ramps/{3}_ns/Analysis/Images/DensityMaps/Map_density_vtime_{0}_{3}ns.png'.format(file, system, run, Ttime), dpi=1200)
                    plt.close()

                    mat_temp[0][:] = densities_map[-1][:]

                plt.imshow(mat_temp, extent=[-15, 15, 200, temp_system], aspect='auto', cmap=cm.jet)
                plt.xlim([0, 3])
                plt.ylim([200, temp_system])
                plt.xlabel('Ice Z Coordinate')
                plt.ylabel('Temperature (K)')
                scalarmappaple = cm.ScalarMappable(cmap=cm.jet)
                plt.colorbar(scalarmappaple, label='Oxygen Density')
                plt.savefig('../{1}/{2}/Heat_Ramps/{3}_ns/Analysis/Images/DensityMaps/Map_density_vtemp_{3}ns_final.png'.format(file, system, run, Ttime), dpi=1200)
                plt.close()



#################CALC DENSITY PROFILES#################################################


ndens = 10
#binning of the density
nbin = 500


def calc_density(file, system, ramp, run, Ttime, ndens, nbin):

    traj_file = open('../{1}/{3}/Heat_Ramps/{4}_ns/Analysis/Trajectories/traj_{1}_{0}_{4}ns.gro'.format(file, system, ramp, run, Ttime), 'r')

    natoms = 2300

    nlines = 0

    for line in traj_file:
        nlines=nlines+1

    nframe = int(nlines/2303)
    nframe_densities = ndens

    traj_file.seek(0)

    for iosef in range(2302):

        osef = traj_file.readline()

    line_size = traj_file.readline()
    line_size_cut = line_size.split()
    size_Z = float(line_size_cut[2])

    Z_range = np.zeros(nbin)

    for ibin in range(nbin):
        Z_range[ibin] = ibin*size_Z/nbin - size_Z/(2)

    traj_file.seek(0)

    time_frame = np.zeros(nframe_densities)

    mat_dens = np.zeros((nframe_densities, nbin))

    for iframe in range(nframe_densities):

        line_time = traj_file.readline()
        line_time_cut = line_time.split()
        time_frame[iframe] = float(line_time_cut[5])

        osef = traj_file.readline()

        line_ref = traj_file.readline()
        line_ref_cut = line_ref.split()
        ref_height = float(line_ref_cut[5])

        for iatom in range(natoms-1):

            line_atom = traj_file.readline()
            line_atom_cut = line_atom.split()
            z_atom = float(line_atom_cut[5])

            for ibin in range(nbin):

                if Z_range[ibin] <= z_atom - ref_height < Z_range[ibin+1] and line_atom_cut[1] == 'OW':

                    mat_dens[iframe][ibin] = mat_dens[iframe][ibin]+1

        osef = traj_file.readline()

        for iosef in range(2303*(int((nframe-nframe_densities)/nframe_densities-1))):

            osef = osef = traj_file.readline()

    return time_frame, mat_dens, Z_range

#then the procedure to automate the calculation on the list of systems and ramps ; and plotting the profiles as just snapshots of the densitymaps

for ramp in ramps:
    
    for run in runs:
        
        for Ttime in Ttimes:
            
            for system in systems:
                
                system_cut = system.split('_')
                system_temp = system_cut[2].split('K')
                temp_system = int(system_temp[0])

                for temp in range(temp_system + 10, 210, 10):

                    print(ramp, system, temp)
                    file = 'heating_{0}K'.format(temp, ramp)
                    times, densities_map, Z_range = calc_density(file, system, ramp, run, Ttime, ndens, nbin)

                    for idens in range(ndens):
                        dens_idens = np.zeros(nbin)

                        plt.plot(Z_range, densities_map[idens][:],
                                 c=cm.jet((times[idens] - times[0]) / (times[-1] - times[0])))

                    plt.xlabel('Z-Coordinate (nm)')
                    plt.ylabel('Oxygen Density')
                    plt.xlim([0, 3])
                    scalarmappaple = cm.ScalarMappable(cmap=cm.jet)
                    scalarmappaple.set_array(range(0, 500000, 1000))
                    plt.colorbar(scalarmappaple, label='Time (ps)')
                    # plt.legend()
                    plt.savefig('../{0}/{3}/Heat_Ramps/{4}_ns/Analysis/Images/DensityProfiles/Oxy_density_vtime_{0}_{2}_{4}ns.png'.format(system, ramp, file, run, Ttime), dpi=1200)
                    plt.close()

                if ramp == '10K':

                    file = 'relax_{0}K'.format(temp_system)
                    times, densities_map, Z_range = calc_density(file, system, ramp, run, Ttime, ndens, nbin)

                    plt.plot(Z_range, densities_map[idens][:],
                             c=cm.jet((times[idens] - times[0]) / (times[-1] - times[0])))

                    plt.xlim([0, 3])
                    plt.xlabel('Z-Coordinate (nm)')
                    plt.ylabel('Oxygen Density')
                    scalarmappaple = cm.ScalarMappable(cmap=cm.jet)
                    scalarmappaple.set_array(range(0, 500000, 10000))
                    plt.colorbar(scalarmappaple, label='Time (ps)')
                    # plt.legend()
                    plt.savefig('../{0}/{3}/Heat_Ramps/{4}_ns/Analysis/Images/DensityProfiles/Oxy_density_vtime_{0}_{2}_{4}ns.png'.format(system, ramp, file, run, Ttime), dpi=1200)
                    plt.close()

                for temp in range(temp_system + 10, 210, 10):

                    print(ramp, system, temp)
                    file = 'heating_{0}K'.format(temp, ramp)
                    times, densities_map, Z_range = calc_density(file, system, ramp, run, Ttime, ndens, nbin)

                    plt.plot(Z_range, densities_map[-1][:],
                                 c=cm.jet((temp) / (200)))

                file = 'relax_{0}K'.format(temp_system)
                times, densities_map, Z_range = calc_density(file, system, ramp, run, Ttime, ndens, nbin)

                plt.plot(Z_range, densities_map[-1][:],
                         c=cm.jet((temp_system) / (200)))

                plt.xlabel('Z-Coordinate (nm)')
                plt.ylabel('Oxygen Density')
                plt.xlim([0, 3])
                scalarmappaple = cm.ScalarMappable(cmap=cm.jet)
                scalarmappaple.set_array(range(0, 210, 10))
                plt.colorbar(scalarmappaple, label='Temperature (K)')
                # plt.legend()
                plt.savefig('../{0}/{2}/Heat_Ramps/{3}_ns/Analysis/Images/DensityProfiles/Oxy_density_vtemp_{0}_last_{3}ns.png'.format(system, ramp, run, Ttime), dpi=1200)
                plt.close()



###########################CALC SURF OCC#################################################################################


distances = {0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, -1}


def calc_surfocc(file, system, ramp, dist, probe, run, Ttime):

#if dist  == -1 ; occlusion above and below on full ice thickness
    traj_file = open('../{1}/{3}/Heat_Ramps/{4}_ns/Analysis/Trajectories/traj_{1}_{0}_{4}ns.gro'.format(file, system, ramp, run, Ttime), 'r')

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

    output_file = open('../{1}/{4}/Heat_Ramps/{5}_ns/Analysis/Output_Files/Surface_Occ/surf_occ_{1}_{0}_dist_{3}.out'.format(file, system, ramp, dist, run, Ttime), 'w')

    line_to_write = 'Surf_occ_above_ini (%)    Surf_occ_below_ini (%)      Surf_occ_above_fin (%)    Surf_occ_below_fin (%)\n'
    output_file.write(line_to_write)

    line_to_write = 'Dist = {0} nm         probe = {1} nm\n'.format(dist, probe)
    output_file.write(line_to_write)

    line_frame = str(surf_occ_above_ini)+'   '+str(surf_occ_below_ini)+'     '+str(surf_occ_above_fin)+'   '+str(surf_occ_below_fin)+ '\n'
    output_file.write(line_frame)

    output_file.close()

for ramp in ramps:
    
    for run in runs:
        
        for Ttime in Ttimes:
            
            for system in systems:
                
                for dist in distances:
                    
                    system_cut = system.split('_')
                    system_temp = system_cut[2].split('K')
                    temp_system = int(system_temp[0])

                    for temp in range(temp_system+10, 210, 10):

                        print(ramp, system, temp, dist)
                        file = 'heating_{0}K'.format(temp, ramp)
                        calc_surfocc(file, system, ramp, dist, 0.275, run, Ttime)

                    if ramp == '10K':

                        file = 'relax_{0}K'.format(temp_system)
                        calc_surfocc(file, system, ramp, dist, 0.275, run, Ttime)


#####################PLOT SURF OCC###############################################################


def plot_surfocc(file, system, ramp, dist, run, Ttime):

    surf_file = open('../{1}/{4}/Heat_Ramps/{5}_ns/Analysis/Output_Files/Surface_Occ/surf_occ_{1}_{2}_dist_{3}.out'.format(ramp, system, file, dist, run, Ttime), 'r')

    osef = surf_file.readline()
    line_probe = surf_file.readline()
    line_probe_cut = line_probe.split()
    probe = float(line_probe_cut[6])

    line_surf = surf_file.readline()
    line_surf_cut = line_surf.split()

    surfocc_above_ini = float(line_surf_cut[0])
    surfocc_below_ini = float(line_surf_cut[1])
    surfocc_above_fin = float(line_surf_cut[2])
    surfocc_below_fin = float(line_surf_cut[3])

    return probe, surfocc_above_ini, surfocc_below_ini, surfocc_above_fin, surfocc_below_fin

for ramp in ramps:
    
    for run in runs:
        
        for Ttime in Ttimes:
            
            for system in systems:
                
                for dist in distances:
                    
                    print(ramp, system, dist)
                    system_temp = system_cut[2].split('K')
                    temp_system = int(system_temp[0])

                    temp_range = range(temp_system, 210, 10)
                    ntemp = len(temp_range)
                    surf_occ_above = np.zeros(ntemp)
                    surf_occ_below = np.zeros(ntemp)
                    surf_occ_above_ini = 0
                    surf_occ_above_fin = 0

                    if ramp == '10K':
                        
                        file = 'relax_{0}K'.format(temp_system)
                        probe, surf_occ_above_ini, surf_occ_below_ini, surf_occ_above[0], surf_occ_below[0] = plot_surfocc(file, system, ramp, dist, run, Ttime)

                    for itemp in range(1, ntemp):

                        temp = temp_range[itemp]
                        file = 'heating_{0}K'.format(temp)
                        probe_osef, surf_occ_above_osef, surf_occ_below_osef, surf_occ_above[itemp], surf_occ_below[itemp] = plot_surfocc(file, system, ramp, dist, run, Ttime)

                    plt.scatter(temp_range, surf_occ_above, label = 'Probe = {0} nm'.format(probe))
                    plt.axhline(y=surf_occ_above_ini, label = 'initial value', color = 'red')
                    plt.xlabel('Temperature (K)')
                    plt.ylabel('Percentage of Surface')
                    plt.title('Above Surface Occlusion - dist = {0} Å'.format(dist))
                    plt.legend()
                    plt.savefig('D:/My_Work/XY_PBC_Runs/Structure_1/{0}/{3}/Heat_Ramps/{4}_ns/Analysis/Images/Surface_Occ/surfocc_above_{0}_dist_{2}.png'.format(system, ramp, dist, run, Ttime), dpi=1200)
                    plt.close()

                    plt.scatter(temp_range, surf_occ_below, label = 'Probe = {0} nm'.format(probe))
                    plt.axhline(y=surf_occ_below_ini, label = 'initial value', color = 'red')
                    plt.xlabel('Temperature (K)')
                    plt.ylabel('Percentage of Surface')
                    plt.title('Below Surface Occlusion - dist = -1')
                    plt.legend()
                    plt.savefig('D:/My_Work/XY_PBC_Runs/Structure_1/{0}/{3}/Heat_Ramps/{4}_ns/Analysis/Images/Surface_Occ/surfocc_below_{0}_dist_{2}.png'.format(system, ramp, dist, run, Ttime), dpi=1200)
                    plt.close()
                
                for dist in distances:

                    print(ramp, system, dist)

                    system_cut = system.split('_')
                    system_temp = system_cut[2].split('K')
                    temp_system = int(system_temp[0])
                    temp_range = range(temp_system, 210, 10)
                    ntemp = len(temp_range)
                    surf_occ_above = np.zeros(ntemp)
                    surf_occ_below = np.zeros(ntemp)
                    surf_occ_above_ini = 0
                    surf_occ_above_fin = 0
            
                    if ramp == '10K':
                                file = 'relax_{0}K'.format(temp_system)
                                probe, surf_occ_above_ini, surf_occ_below_ini, surf_occ_above[0], surf_occ_below[0] = plot_surfocc(file, system, ramp, dist, run, Ttime)

                    for itemp in range(1, ntemp):
                                    temp = temp_range[itemp]
                                    file = 'heating_{0}K'.format(temp)
                                    probe_osef, surf_occ_above_osef, surf_occ_below_osef, surf_occ_above[itemp], surf_occ_below[
                                        itemp] = plot_surfocc(file, system, ramp, dist, run, Ttime)

                    if dist == -1:

                        plt.scatter(temp_range, surf_occ_below, color='pink')

                    else:

                        plt.scatter(temp_range, surf_occ_below, color=cm.jet((10*dist-4)/(24-4)))

                plt.axhline(y=surf_occ_below_ini, label='initial value', color='red')
                plt.xlabel('Temperature (K)')
                plt.ylabel('Percentage of Surface')
                plt.title('Below Surface Occlusion - dist = -1')
                scalarmappaple = cm.ScalarMappable(cmap=cm.jet)
                scalarmappaple.set_array(range(4, 30, 1))
                plt.colorbar(scalarmappaple, label='Distance to the silicon surface (Å)')
                plt.legend()
                plt.savefig('../{0}/{2}/Heat_Ramps/{3}_ns/Analysis/Images/Surface_Occ/surfocc_below_CompDist_{0}.png'.format(system, ramp, run, Ttime), dpi=1200)
                plt.close()

                for dist in distances:

                    print(ramp, system, dist)

                    system_cut = system.split('_')
                    system_temp = system_cut[2].split('K')
                    temp_system = int(system_temp[0])

                    temp_range = range(temp_system, 210, 10)
                    ntemp = len(temp_range)
                    surf_occ_above = np.zeros(ntemp)
                    surf_occ_below = np.zeros(ntemp)
                    surf_occ_above_ini = 0
                    surf_occ_above_fin = 0

                    if ramp == '10K':
                        file = 'relax_{0}K'.format(temp_system)
                        probe, surf_occ_above_ini, surf_occ_below_ini, surf_occ_above[0], surf_occ_below[
                            0] = plot_surfocc(file, system, ramp, dist, run, Ttime)

                    for itemp in range(1, ntemp):
                        temp = temp_range[itemp]
                        file = 'heating_{0}K'.format(temp)
                        probe_osef, surf_occ_above_osef, surf_occ_below_osef, surf_occ_above[itemp], surf_occ_below[
                            itemp] = plot_surfocc(file, system, ramp, dist, run, Ttime)

                    if dist == -1:

                        plt.scatter(temp_range, surf_occ_above, color='pink')

                    else:

                        plt.scatter(temp_range, surf_occ_above, color=cm.jet((10 * dist - 4) / (24 - 4)))

                plt.axhline(y=surf_occ_above_ini, label='initial value', color='red')
                plt.xlabel('Temperature (K)')
                plt.ylabel('Percentage of Surface')
                plt.title('Above Surface Occlusion - dist = -1')
                scalarmappaple = cm.ScalarMappable(cmap=cm.jet)
                scalarmappaple.set_array(range(4, 30, 1))
                plt.colorbar(scalarmappaple, label='Distance to the silicon surface (Å)')
                plt.legend()
                plt.savefig('../{0}/{2}/Heat_Ramps/{3}_ns/Analysis/Images/Surface_Occ/surfocc_above_CompDist_{0}.png'.format(system, ramp, run, Ttime), dpi=1200)
                plt.close()


####################PLOTTING RDF####################################################################################


#ndens = 10
#nbin = 500

#def read_rdf(file, system, ramp, ndens, nbin, run, Ttime):
        
#    rdf_file = open('../{1}/{3}/Heat_Ramps/{4}_ns/Analysis/RDF/fixed_rdf_{1}_{0}_{4}ns.txt'.format(file, system, ramp, run, Ttime), 'r')
#    
#    nrdf = 774
#
#    dist = np.zeros(nrdf)
#    rdf = np.zeros(nrdf)

#    for irdf in range(nrdf):

#        line = rdf_file.readline()
#        line_cut = line.split()
#        dist[irdf] = float(line_cut[0])
#        rdf[irdf] = float(line_cut[1])
#
#    return dist, rdf

#for ramp in ramps:
    
#    for run in runs:
        
#        for Ttime in Ttimes:
            
#            for system in systems:
                
#                system_cut = system.split('_')
#                system_temp = system_cut[2].split('K')
#                temp_system = int(system_temp[0])
#                print(temp_system)

#                for temp in range(temp_system + 20, 210, 10):

#                    print(ramp, system, temp)
#                    file = 'heating_{0}K'.format(temp, ramp)
#                    dist, rdf = read_rdf(file, system, ramp, ndens, nbin, run, Ttime)

 #                   plt.plot(dist, rdf, c=cm.jet((temp-10)/200))
  #          
   #             file = 'relax_{0}K'.format(temp_system)
    #            dist, rdf = read_rdf(file, system, ramp, ndens, nbin, run, Ttime)
     #           plt.plot(dist, rdf, c=cm.jet((temp_system - 10) / 200))

      #          plt.xlabel('O-O distance (nm)')
       #         plt.ylabel('$g_{OO}(r)$')
        #        #plt.xlim([0.2, 1.5])
         #       #plt.ylim([0, 30])    #I added this
          #      scalarmappaple = cm.ScalarMappable(cmap=cm.jet)
           #     scalarmappaple.set_array(range(30, 210, 10))
            #    plt.colorbar(scalarmappaple, label='Temperature (K)')
             #   plt.savefig('../{0}/{3}/Heat_Ramps/{4}_ns/Analysis/Images/RDF_fixed_{0}_{4}ns.png'.format(system, ramp, file, run, Ttime), dpi=1200)
              #  plt.close()















