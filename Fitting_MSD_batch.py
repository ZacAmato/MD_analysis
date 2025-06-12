import math
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from matplotlib import cm
from scipy.optimize import curve_fit

systems = {'300Kwater_on_20Ksilic'}
runs = {'RUN01'}
Ttimes = {'100'}
ramps = {'10K'}

def test(x, a, b):
    return a*x + b               

def plot_diff_coeff(file, run, system, ramp, Ttime):

    msd_file = open('D:/My_Work/XY_PBC_Runs/Structure_1/{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Output_Files/MSD/msd_{2}_{0}_{4}ns.xvg'.format(file, run, system, ramp, Ttime), 'r')


    #nlines = -1
    #for line in msd_file:
    #    if line != '':
     #       nlines = nlines + 1

    msd_file.seek(0)
    
    for iosef in range(21):           # to fit over the whole MSD file
        osef = msd_file.readline()
        
    #if file == "heating_30K":
        #nlines = 8144
    #else:       
    nlines = 12000
        
        
    time = np.zeros(nlines)    # - 21 if over whole thing
    msd = np.zeros(nlines)
    
    for iline in range(nlines):
    
        line_msd = msd_file.readline()
        line_msd_cut = line_msd.split()
        
        time [iline] = float(line_msd_cut[0]) 
        msd [iline] = float(line_msd_cut[1]) / 1e+7

    
    plt.plot(time, msd)
    plt.xlabel('∆T')
    plt.ylabel('MSD (cm$^2$)')
    plt.title('{0}'.format(file, run, system, ramp, Ttime))
    #plt.savefig('D:/My_Work/XY_PBC_Runs/Structure_1/{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Images/MSD/msd_{2}_{0}_{4}ns.png'.format(file, run, system, ramp, Ttime), bbox_inches='tight', dpi=800)
    plt.show()
    plt.close()

    popt, _ = curve_fit(test, time, msd)
    a, b = popt
    
    diff_coeff = popt[0]
    
    print(diff_coeff)
    
    
 
    return diff_coeff

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

                diff_coeff_values = np.zeros(ntemp)
                
                output_file = open('D:/My_Work/XY_PBC_Runs/Structure_1/{1}/{0}/Heat_Ramps/{3}_ns/Analysis/Output_Files/MSD/lim_6000_diff_coeff_manual_{1}_{3}ns.txt'.format(run, system, ramp, Ttime), 'w')
                
                file = 'relax_{0}K'.format(temp_system)
                diff_coeff_values[0] = plot_diff_coeff(file, run, system, ramp, Ttime)
                
                line_frame = str(temp_system)+'  '+str(diff_coeff_values[0])+' \n'
                output_file.write(line_frame)
                

                for itemp in range(1, ntemp):

                    temp = temp_range[itemp]
                    file = 'heating_{0}K'.format(temp, ramp)
                    diff_coeff_values[itemp] = plot_diff_coeff(file, run, system, ramp, Ttime)
                    
                    line_frame = str(temp)+'  '+str(diff_coeff_values[itemp])+' \n'
                    output_file.write(line_frame)
                    
                output_file.close()
                

                plt.scatter(temp_range, diff_coeff_values, c='k', marker='s', s=20)

                plt.xlabel('Simulation Annealing Temperature (K)', fontsize=12)
                plt.ylabel('Diffusion Coefficient (cm$^2$/s)', fontsize=12)
                plt.yscale('log')
                plt.tick_params(which="major", labelsize=12, width=2, length=6)
                plt.tick_params(which="minor", labelsize=12, width=2, length=4)
                #plt.savefig('D:/My_Work/XY_PBC_Runs/Structure_1/{2}/{1}/Heat_Ramps/{4}_ns/Analysis/Images/lim_6000_diff_coeff_{2}.png'.format(file, run, system, ramp, Ttime), bbox_inches='tight', dpi=1200)
                plt.show()
                plt.close()


               