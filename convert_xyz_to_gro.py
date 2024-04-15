# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as plt
from math import *

input_file = open('../Input_structures/RUN04_120K_final_structure.xyz', 'r')
output_file = open('../Input_structures/input_ST3_300Kwater_on_120Ksilic.gro', 'w')

line = 'Water on SiO2 \n'
output_file.write(line)

line_natom = input_file.readline()
natom = int(line_natom)
output_file.write(line_natom)

osef = input_file.readline()
count_water = 301
count_H = True

for iatom in range(1, natom+1):
    line_input = input_file.readline()
    line_cut = line_input.split()
    
    if iatom < 10:
        first_space = '     '
        second_space = '   '
    elif iatom < 100:
        first_space = '    '
        second_space = '  '
    elif iatom < 301:
        first_space = '   '
        second_space = '  '
    elif iatom < 1000:
        first_space = '  '
        second_space = '  '
    elif iatom < 10000:
        first_space = '  '
        second_space = ' '
    
    if line_cut[0] == 'SZ':
        
        if iatom == 100:
        
            line = first_space + str(iatom) + 'SZ' + '    SZ1 ' + str(iatom) + '   ' + '{:.3f}'.format(float(line_cut[1])/10.0+50.0) + '   ' + '{:.3f}'.format(float(line_cut[2])/10.0+50.0) + '  ' + '{:.3f}'.format((float(line_cut[3]) / 10) -50.0) + '\n'
            output_file.write(line)
        
        else:
            line = first_space + str(iatom) + 'SZ' + '    SZ1' + second_space + str(iatom) + '   ' + '{:.3f}'.format(float(line_cut[1])/10.0+50.0) + '   ' + '{:.3f}'.format(float(line_cut[2])/10.0+50.0) + '  ' + '{:.3f}'.format((float(line_cut[3]) / 10) -50.0) + '\n'
            output_file.write(line)
        
    elif line_cut[0] == 'SO':
        
        line = first_space + str(iatom) + 'SZ' + '     SZ' + second_space + str(iatom) + '   ' + '{:.3f}'.format(float(line_cut[1])/10.0+50.0) + '   ' + '{:.3f}'.format(float(line_cut[2])/10.0+50.0) + '  ' + '{:.3f}'.format((float(line_cut[3]) / 10) -50.0) + '\n'
        output_file.write(line)
        
        
    elif line_cut[0] == 'OW': 

        line = first_space + str(count_water) + 'H2O' + '     OW' + second_space + str(iatom) + '   ' + '{:.3f}'.format(float(line_cut[1])/10.0+50.0) + '   ' + '{:.3f}'.format(float(line_cut[2])/10.0+50.0) + '  ' + '{:.3f}'.format((float(line_cut[3]) / 10) -50.0) + '\n'
        output_file.write(line)

    elif line_cut[0] == 'HW' and count_H == True: 

        line = first_space + str(count_water) + 'H2O' +  '    HW1' + second_space + str(iatom) + '   ' + '{:.3f}'.format(float(line_cut[1])/10.0+50.0) + '   ' + '{:.3f}'.format(float(line_cut[2])/10.0+50.0) + '  ' + '{:.3f}'.format((float(line_cut[3]) / 10) -50.0) + '\n'
        output_file.write(line)
        count_H = False

    elif line_cut[0] == 'HW' and count_H == False: 

        line = first_space + str(count_water) + 'H2O' + '    HW2' + second_space + str(iatom) + '   ' + '{:.3f}'.format(float(line_cut[1])/10.0+50.0) + '   ' + '{:.3f}'.format(float(line_cut[2])/10.0+50.0) + '  ' + '{:.3f}'.format((float(line_cut[3]) / 10) -50.0) + '\n'
        output_file.write(line)
        count_H = True

    elif line_cut[0] == 'QW': 

        line = first_space + str(count_water) + 'H2O' + '     MW' + second_space + str(iatom) + '   ' + '{:.3f}'.format(float(line_cut[1])/10.0+50.0) + '   ' + '{:.3f}'.format(float(line_cut[2])/10.0+50.0) + '  ' + '{:.3f}'.format((float(line_cut[3]) / 10) -50.0) + '\n'
        output_file.write(line)
        count_water = count_water + 1
line2 = '   3.12506   3.12506  30.00000'
output_file.write(line2)