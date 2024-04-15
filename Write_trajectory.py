# -*- coding: utf-8 -*-

import numpy as np

heat = str('40')

input_file = open(f'../300Kwater_on_40Ksilic/RUN01/Heat_Ramps/5_ns/Analysis/Trajectories/traj_300Kwater_on_40Ksilic_relax_{heat}K_5ns.gro', 'r')
output_file = open(f'../300Kwater_on_40Ksilic/RUN01/Heat_Ramps/5_ns/Analysis/RDF/Cut_up/Z_distance/1st_100/first_cutup_traj_300Kwater_on_40Ksilic_relax_{heat}K_5ns.gro', 'w')

nlines = 0

for line in input_file:
        nlines=nlines+1

print('Number of lines =', nlines)

nframe = int(nlines/2303)

print('Number of frames =', nframe)

input_file.seek(0)

for iframe in range(nframe):


    step_line = input_file.readline()
    step_line_cut = step_line.split()
    
    print('Frame =', iframe)
    t = float(step_line_cut[5])
    print('Time =', t)
    step = float(step_line_cut[7])
    print('Step =', step)
    

    line = 'water ice on Sio2 t= %.5f step= %.0f' %(t, step) + '\n'
    output_file.write(line)

    
    line_natom = input_file.readline()
    natom = int(line_natom)
    #output_file.write(line_natom)
    
    line3 = '700' + '\n'
    output_file.write(line3)

    count_water = 301
    
    count_water_atoms = 301

    for iatom in range(1, natom+1):
    
       line = input_file.readline()
       line_cut = line.split()
    
       if iatom < 10:
           first_space = '    '
           second_space = '    '
       elif iatom < 100:
           first_space = '   '
           second_space = '   '
       elif iatom < 1000:
           first_space = '  '
           second_space = '  '
       elif iatom < 10000:
           first_space = '  '
           second_space = ' '
           
          
    
       if line_cut[1] == 'SZ1':
            
           if iatom == 100:
            
               line = first_space + str(iatom) + 'silic' + '  SZ1' + second_space + str(iatom) + '   ' + '{:.3f}'.format(float(line_cut[3])) + '   ' + '{:.3f}'.format(float(line_cut[4])) + '  ' + '{:.3f}'.format(float(line_cut[5])) + '  ' + '{:6.4f}'.format(float(line_cut[6])) + '  ' + '{:6.4f}'.format(float(line_cut[7])) + '  ' + '{:6.4f}'.format(float(line_cut[8])) + '\n'
               output_file.write(line)
            
           else:
                
               line = first_space + str(iatom) + 'silic' + '  SZ1' + second_space + str(iatom) + '   ' + '{:.3f}'.format(float(line_cut[3])) + '   ' + '{:.3f}'.format(float(line_cut[4])) + '  ' + '{:.3f}'.format(float(line_cut[5])) + '  ' + '{:6.4f}'.format(float(line_cut[6])) + '  ' + '{:6.4f}'.format(float(line_cut[7])) + '  ' + '{:6.4f}'.format(float(line_cut[8])) + '\n'
               output_file.write(line)
        
        
       elif line_cut[1] == 'SZ':
        
           line = first_space + str(iatom) + 'silic' + '   SZ' + second_space + str(iatom) + '   ' + '{:.3f}'.format(float(line_cut[3])) + '   ' + '{:.3f}'.format(float(line_cut[4])) + '  ' + '{:.3f}'.format(float(line_cut[5])) + '  ' + '{:6.4f}'.format(float(line_cut[6])) + '  ' + '{:6.4f}'.format(float(line_cut[7])) + '  ' + '{:6.4f}'.format(float(line_cut[8])) + '\n'
           output_file.write(line)


       if 15 < float(line_cut[5]) and  float(line_cut[5]) <= 15.8 and count_water < 401:                                       # if iatom in range(1101, 1501):    < 701 for first layer    range(701, 1101) for 2nd layer  
           
         
            if line_cut[1] == 'OW':

                line = first_space + str(count_water) + 'water' + '   OW' + second_space + str(count_water_atoms) + '   ' + '{:.3f}'.format(float(line_cut[3])) + '   ' + '{:.3f}'.format(float(line_cut[4])) + '  ' + '{:.3f}'.format(float(line_cut[5])) + '  ' + '{:6.4f}'.format(float(line_cut[6])) + '  ' + '{:6.4f}'.format(float(line_cut[7])) + '  ' + '{:6.4f}'.format(float(line_cut[8])) + '\n'
                output_file.write(line)
                count_water_atoms = count_water_atoms + 1

        
            elif line_cut[1] == 'HW1': 

                line = first_space + str(count_water) + 'water' +  '  HW1' + second_space + str(count_water_atoms) + '   ' + '{:.3f}'.format(float(line_cut[3])) + '   ' + '{:.3f}'.format(float(line_cut[4])) + '  ' + '{:.3f}'.format(float(line_cut[5])) + '  ' + '{:6.4f}'.format(float(line_cut[6])) + '  ' + '{:6.4f}'.format(float(line_cut[7])) + '  ' + '{:6.4f}'.format(float(line_cut[8])) + '\n'
                output_file.write(line)
                count_water_atoms = count_water_atoms + 1
    

            elif line_cut[1] == 'HW2':
        
                line = first_space + str(count_water) + 'water' + '  HW2' + second_space + str(count_water_atoms) + '   ' + '{:.3f}'.format(float(line_cut[3])) + '   ' + '{:.3f}'.format(float(line_cut[4])) + '  ' + '{:.3f}'.format(float(line_cut[5])) + '  ' + '{:6.4f}'.format(float(line_cut[6])) + '  ' + '{:6.4f}'.format(float(line_cut[7])) + '  ' + '{:6.4f}'.format(float(line_cut[8])) + '\n'
                output_file.write(line)
                count_water_atoms = count_water_atoms + 1
        

            elif line_cut[1] == 'MW':

                line = first_space + str(count_water) + 'water' + '   MW' + second_space + str(count_water_atoms) + '   ' + '{:.3f}'.format(float(line_cut[3])) + '   ' + '{:.3f}'.format(float(line_cut[4])) + '  ' + '{:.3f}'.format(float(line_cut[5])) + '  ' + '{:6.4f}'.format(float(line_cut[6])) + '  ' + '{:6.4f}'.format(float(line_cut[7])) + '  ' + '{:6.4f}'.format(float(line_cut[8])) + '\n'
                output_file.write(line)
                count_water = count_water + 1
                count_water_atoms = count_water_atoms + 1
                

  
    line2 = '   3.12506   3.12506  30.00000' + '\n'
    output_file.write(line2)
    
    osef = input_file.readline()
    
    
    
