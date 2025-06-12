#! /usr/bin/bash

Path="/mnt/d/My_Work/XY_PBC_Runs/Structure_1/"

TSur=$1;
RUN=$2;
Time=$3

if [ $# -ne 3 ]; then

	echo "Batch_GROMACS_traj.sh expects 5 arguments:"
	echo "   Space-separated list of TSurS of interest; must be enclosed in \" \""
	echo "   Run number/Heating type/Time"
	echo "   Time"
	exit 1;

fi

for TSur in $TSur; do 

	Folder=$Path/300Kwater_on_${TSur}Ksilic/${RUN}/Analysis/Trajectories

	if [ $TSur == 20 ]; then

	Heat="30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200"

	elif [ $TSur == 40 ]; then

	Heat="50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200"

	elif [ $TSur == 60 ]; then

	Heat="70 80 90 100 110 120 130 140 150 160 170 180 190 200"

	elif [ $TSur == 80 ]; then

	Heat="90 100 110 120 130 140 150 160 170 180 190 200"

	elif [ $TSur == 100 ]; then

	Heat="110 120 130 140 150 160 170 180 190 200"

	elif [ $TSur == 120 ]; then

	Heat="130 140 150 160 170 180 190 200"

	fi

	cd $Folder

	echo "4" | gmx msd -f 300Kwater_on_${TSur}Ksilic_relax_${TSur}K_${Time}ns.trr -s 300Kwater_on_${TSur}Ksilic_relax_${TSur}K_${Time}ns.tpr -o $Path/300Kwater_on_${TSur}Ksilic/${RUN}/Analysis/Output_Files/MSD/timeframe_100/msd_300Kwater_on_${TSur}Ksilic_relax_${TSur}K_${Time}ns.xvg -mol $Path/300Kwater_on_${TSur}Ksilic/${RUN}/Analysis/Output_Files/MSD/timeframe_five/diff_coeff_300Kwater_on_${TSur}Ksilic_relax_${TSur}K_${Time}ns.xvg -trestart 1000 -b 100 \

	for Heat in $Heat; do

	echo "4" | gmx msd -f 300Kwater_on_${TSur}Ksilic_heating_${Heat}K_${Time}ns.trr -s 300Kwater_on_${TSur}Ksilic_heating_${Heat}K_${Time}ns.tpr -o $Path/300Kwater_on_${TSur}Ksilic/${RUN}/Analysis/Output_Files/MSD/timeframe_100/msd_300Kwater_on_${TSur}Ksilic_heating_${Heat}K_${Time}ns.xvg -mol $Path/300Kwater_on_${TSur}Ksilic/${RUN}/Analysis/Output_Files/MSD/timeframe_100/diff_coeff_300Kwater_on_${TSur}Ksilic_heating_${Heat}K_${Time}ns.xvg -trestart 1000 -b 100 \

	done
done
