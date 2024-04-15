#! /usr/bin/bash

TInc=$1;
Surf=$2;
Prefix=$3;
TSurS=$4;

if [ $# -ne 4 ]; then
   echo "Calculate_porosity.sh expects precisely 4 arguments:"
   echo "   Incoming temperature in the format %3.3i"
   echo "   Name of the surface (silic or water)"
   echo "   Full path to a RUN directory of interest"
   echo "   Space-separated list of TSurS of interest; it must be enclosed in \" \""
   exit 1;
fi

for TSur in $TSurS; do
   Folder=$Prefix/${TInc}Kwater_on_${TSurS}K${Surf}

   if [ ! -f "$Folder/Heat_Ramps/5_ns/Analysis/Output_Files/Bash_Heights/heights_300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.txt" ]; then
      echo
	  echo "The file heights_300Kwater_${TSurS}K${Surf}_relax_${TSurS}K.txt doesn't exist in"
	  echo "$Folder/Heat_Ramps/5_ns/Analysis/Output_Files/Bash_Heights/"
	  echo "Generate this file by running Extract_heights.sh";
	  exit 1;
   fi

   awk -f porosity.awk $Folder/Heat_Ramps/5_ns/Analysis/Output_Files/Bash_Heights/heights_300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.txt > $Folder/Heat_Ramps/5_ns/Analysis/Output_Files/Bash_Porosity/density-porosity_300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.txt

done

