#! /usr/bin/bash

TInc=$1;
Prefix=$2;
iMaxDep=$3;
TSurS=$4;
ZZero=$5

if [ $# -ne 5 ]; then
   echo "Extract_heights.sh expects precisely 5 arguments:"
   echo "   Incoming temperature in the format %3.3i"
   echo "   Full path to a RUN directory of interest"
   echo "   Number of deposited water molecules"
   echo "   Space-separated list of TSurS of interest; it must be enclosed in \" \""
   echo "   Highest Silic atom Z coordinate in Angstrom"
   exit 1;
fi

for TSur in $TSurS; do

   Folder=$Prefix/${TInc}Kwater_on_${TSurS}K${Surf}

   if [ ! -f "$Folder/Heat_Ramps/5_ns/Analysis/XYZ/300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.xyz" ]; then
      echo
	  echo "The file 300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.xyz doesn't exist in"
	  echo "$Folder/Heat_Ramps/5_ns/Analysis/XYZ/"
	  echo "Generate this file by using Pierre's script";
	  exit 1;
   fi

   awk --assign ZZero=$ZZero --assign iMaxDep=$iMaxDep \
     -f ./Extract_heights.awk $Folder/Heat_Ramps/5_ns/Analysis/XYZ/300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.xyz \
	 > $Folder/Heat_Ramps/5_ns/Analysis/Output_Files/Bash_Heights/heights_300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.txt

done
