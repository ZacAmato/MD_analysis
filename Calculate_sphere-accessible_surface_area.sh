#!/bin/bash

# A wrapper arround dms program. Dms calculates sphere-accessible surface area
# of a given surface. The input parameters are sphere radius, RSphere, and den-
# sity of the grid, GridDens. See `man dms` for citation for the algorithm and 
# for options of the program.
PrefiX=$1;
RSpherE=$2;  # Radius of a sphere used in dms.
TSur=$3;
RUn=$4;
TypE=$5;
HeaT=$6;
Scratch=$7;
TIme=$8
# Hard-coded parameters for mirroring the cell and for multiplying it by the factor
# (iCell x iCell) in the XY plane. The mirroring and multiplication of the initial 
# cell is introduced in order to improve the precision of SASA calculations. See the
# folder ../SASA-improved for the results of the convergence tests with various iCell
# values and various separations between mirror images, Sep.
iCell="3";
Sep="0.0";
GridDens="10.0"

for TSur in $TSur; do

  printf "\n   Working on TSur=${TSur} and RSphere=${RSpherE}...\n"

  Folder=$PrefiX/300Kwater_on_${TSur}Ksilic

  if [ ! -f "$Folder/${RUn}/Analysis/XYZ/300Kwater_on_${TSur}Ksilic_${TypE}_${HeaT}K_${TIme}ns.xyz" ]; then
    echo
    echo "The file 300Kwater_on_${TSur}Ksilic_${TypE}_${TSur}K_${TIme}ns.xyz doesn't exist in"
    echo "$Folder/${RUn}/Analysis/XYZ"
    echo "Generate this file by running Pierre's script"; 
    exit 1;
  fi

  TmpDir=`mktemp --directory --tmpdir=${Scratch}/scratch/ sasa-XXXXX`

  printf "%i\n=======\n" 1500 > $TmpDir/final_structure_no_substrate.xyz
  cat $Folder/${RUn}/Analysis/XYZ/300Kwater_on_${TSur}Ksilic_${TypE}_${HeaT}K_${TIme}ns.xyz \
    | sed 's/SZ/X /g' \
    | sed 's/SO/X /g' \
    | sed 's/OW/O /g' \
    | sed 's/HW/H /g' \
    | sed 's/QW/Q /g' \
    | sed 's/OZ/O /g' \
    | sed 's/HZ/H /g' \
    | sed 's/QZ/Q /g' \
    | sed 's/HS/H /g' \
    | sed 's/OS/O /g' \
    | sed 's/QS/Q /g' \
    | sed 's/\t/   /g'\
    | grep --invert-match Q \
    | tail -n 1500 >> $TmpDir/final_structure_no_substrate.xyz

   cp $TmpDir/final_structure_no_substrate.xyz $Folder/${RUn}/Analysis/Output_Files/Bash/SASA/300Kwater_on_${TSur}Ksilic_${TypE}_${HeaT}K_no_substrate.xyz

   cat $TmpDir/final_structure_no_substrate.xyz \
    | ./mirror.awk -v "Separation=$Sep" \
    | ./multicell.awk -v "iCell=$iCell" \
      > $TmpDir/tmp-sasa.xyz

  obabel $TmpDir/tmp-sasa.xyz \
        -O $TmpDir/tmp-sasa.pdb \
	2>/dev/null


  LogDMS="$Folder/${RUn}/Analysis/Output_Files/Bash/SASA/300Kwater_on_${TSur}Ksilic_${TypE}_${HeaT}K_SASA_Sphere-${RSpherE}_iCell-${iCell}-by-${iCell}_MirrorSep-${Sep}.txt"

  dms $TmpDir/tmp-sasa.pdb -o /dev/null -g $LogDMS -a -v -w $RSpherE -d $GridDens \
  2>/dev/null

  if [ $? -ne 0  ]; then
    echo ""
    echo "dms exited with non-zero status in"
    echo "$Folder/${RUn}/Analysis/Output_Files/Bash/SASA/"
    exit 1;
  fi

  echo "======= End of dms log =======" >> $LogDMS
  echo >>$LogDMS
  echo "Mirror   = Yes" >> $LogDMS
  echo "Separ.   = $Sep" >> $LogDMS
  echo "iCell    = $iCell" >> $LogDMS
  echo >>$LogDMS
  echo "RSphere  = $RSpherE" >> $LogDMS
  echo "GridDens = $GridDenS" >> $LogDMS
  echo >>$LogDMS
  echo "Invocation command for dms:" >> $LogDMS
  echo "dms $TmpDir/tmp-sasa.pdb -o /dev/null -g $LogDMS -a -v -w $RSpherE -d $GridDens" >> $LogDMS

  rm -f $TmpDir/tmp-sasa.{pdb,xyz} 
  rm -f $TmpDir/final_structure_no_substrate.xyz
  rmdir $TmpDir

done
