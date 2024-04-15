#! /usr/bin/bash

Prefix=$1;
ScrDir=$2;
TSurS=$3;
RUN=$5;
Heat=$6;
Type=$7;
Time=$8;


if [ $# -ne 8 ]; then
   echo "Full_Analysis.sh expects precisely 8 arguments:"
   echo "   Full path to a RUN directory of interest"
   echo "   Full path to a scratch directory"
   echo "   Space-separated list of TSurS of interest; it must be enclosed in \" \""
   echo "   Run number/Heating type/Time"
   echo "   Heating value"
   echo "   relax or heating?"
   echo "   time"
   exit 1;
fi

for TSur in $TSurS; do

   Folder=$Prefix/300Kwater_on_${TSurS}Ksilic

   if [ ! -f "$Folder/${RUN}/Analysis/XYZ/300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.xyz" ]; then
      echo
	  echo "The file 300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.xyz doesn't exist in"
	  echo "$Folder/${RUN}/Analysis/XYZ/"
	  echo "Generate this file by using Pierre's script";
	  exit 1;
   fi

   Zmax_folder=$Folder/${RUN}/Analysis/XYZ

   ZZero=$(<$Zmax_folder/Zmax_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.txt)

   echo "$ZZero"

   awk --assign ZZero=$ZZero --assign iMaxDep=500 \
     -f ./Extract_heights.awk $Folder/${RUN}/Analysis/XYZ/300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.xyz \
	 > $Folder/${RUN}/Analysis/Output_Files/Bash/Heights/heights_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.txt

   awk -f porosity.awk $Folder/${RUN}/Analysis/Output_Files/Bash/Heights/heights_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.txt > $Folder/${RUN}/Analysis/Output_Files/Bash/Porosity/density-porosity_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.txt
   done

RSphere="      1.0      1.25      1.5      1.75      2.0      2.25      2.5      2.75      3.0      3.25     3.5      "

for RSphere in $RSphere; do
	./Calculate_sphere-accessible_surface_area.sh ${Prefix} ${RSphere} ${TSurS} ${RUN} ${Type} ${Heat} ${ScrDir} ${Time}
done

RWater="1.70"
iCell="2";
PSDCycle="190"
PSDStart="0.05"
PSDGrid="0.05"

for TSur in $TSurS; do

   printf "\n  Working on TSur=${TSur}...\n"

   Folder=$Prefix/300Kwater_on_${TSur}Ksilic

   if [ ! -f "$Folder/${RUN}/Analysis/XYZ/300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.xyz" ]; then
     echo
     echo "The file 300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.xyz doesn't exist in"
     echo "$Folder/${RUN}/Analysis/XYZ/"
     echo "Generate this file by running Pierre's scripts";
     exit 1;
   fi

   TmpDir=`mktemp --directory --tmpdir=${ScrDir}/scratch/ psd-XXXXX`

   awk \
     '
       BEGIN{ iLine=0; }
       $1=="QW" { iLine++; Array[iLine]=$0; }
       END{ printf("%i\n====\n",iLine); for(i=1; i<=iLine; i++) { print Array[i] }  }
     ' \
     $Folder/${RUN}/Analysis/XYZ/300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.xyz \
   | sed 's/QW/WM/g' \
   | ./multicell.awk -v "iCell=$iCell" \
   | ./box.awk -v Part="WM" \
     > $TmpDir/tmp-psd.xyz

    printf "WM  %f Water_molecule\n\n" $RWater > $TmpDir/radii_list.dat

    cwd='pwd'
    cd $TmpDir

    PathPSD="/mnt/c/Users/PSDsolv-1.1/"
    $PathPSD/psd $TmpDir/tmp-psd.xyz $PSDStart $PSDGrid  1>/dev/null &
    pid=$!

    iIter="0";
    while [ $iIter -lt $PSDCycle ]; do
      sleep 5s
      iIter=`awk 'END{print NR}' $TmpDir/error.dat`
    done
    kill $pid 2>/dev/null

    cd $cwd

    printf "PSDsolv parameters are 2nd= %f 3rd= %f; NConverge=%i .\n" $PSDStart $PSDGrid $PSDCycle \
      >> $TmpDir/psd_error.dat
    echo "The last 10 lines of error.dat are"  >> $TmpDir/psd_error.dat
    tail -n 10 $TmpDir/error.dat >> $TmpDir/psd_error.dat

    mv $TmpDir/psd_error.dat $Folder/${RUN}/Analysis/Output_Files/Bash/PSD/psd_error_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.dat 2>/dev/null
    mv $TmpDir/psd_cumm.dat  $Folder/${RUN}/Analysis/Output_Files/Bash/PSD/psd_cumm_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.dat  2>/dev/null
    mv $TmpDir/psd_diff.dat  $Folder/${RUN}/Analysis/Output_Files/Bash/PSD/psd_diff_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.dat  2>/dev/null

    rm $TmpDir/radii_list.dat
    rm $TmpDir/tmp-psd.xyz
    rm $TmpDir/error.dat
    rmdir $TmpDir

done

gnuplot << EOGNUPLOT
set terminal postscript enhanced ",20"

set xrange [1:15]
set label 2 "TInc=300K" at graph 0.8,0.90 font "Bitstream Vera Sans Mono,18"
set label 3 "TSur=${TSurS}K" at graph 0.8,0.85 font "Bitstream Vera Sans Mono,18"
set label 4 "${Type}" at graph 0.8,0.80 font "Bitstream Vera Sans Mono,18"
set label 5 "${Heat}K" at graph 0.8,0.75 font "Bitstream Vera Sans Mono,18"

set label 1 " PSD Cumm" at graph 0.8,0.95 font "Bitstream Vera Sans Mono,18"
set yrange [-0.01:1.1]
set xlabel "Pore diameter, Angstroms"
set ylabel "Cummulative distribution
set output "${ScrDir}scratch/psd_cumm.ps"
plot "$Folder/${RUN}/Analysis/Output_Files/Bash/PSD/psd_cumm_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.dat" u 1:2  w lp lw 2.0 notitle

set label 1 " PSD Diff" at graph 0.8,0.95 font "Bitstream Vera Sans Mono,18"
set yrange [-0.01:1.1]
set xlabel "Pore diameter, Angstroms"
set ylabel "Probability density"
set output "${ScrDir}scratch/psd_diff.ps"
plot "$Folder/${RUN}/Analysis/Output_Files/Bash/PSD/psd_diff_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.dat" u 1:2  w impulses lw 2.0 notitle 

EOGNUPLOT

ps2pdf ${ScrDir}scratch/psd_cumm.ps ${ScrDir}scratch/psd_cumm.pdf
cp  ${ScrDir}scratch/psd_cumm.pdf $Folder/${RUN}/Analysis/Images/Bash/psd_cumm_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.pdf

ps2pdf ${ScrDir}scratch/psd_diff.ps ${ScrDir}scratch/psd_diff.pdf
cp  ${ScrDir}scratch/psd_diff.pdf $Folder/${RUN}/Analysis/Images/Bash/psd_diff_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.pdf

rm -f ${ScrDir}scratch/tmp-1 ${ScrDir}scratch/psd_cumm.{ps,pdf} ${ScrDir}scratch/psd_diff.{ps,pdf}

for TSur in ${TSurS}; do

   Folder=${Prefix}/300Kwater_on_${TSurS}Ksilic/${RUN}/Analysis/Output_Files/Bash/PSD

   tail -n 10 ${Folder}/psd_diff_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.dat \
     | awk '$2==0 {printf("Max poresize is %f\n", $1); exit; }' \
     > ${Folder}/maxporesize_300Kwater_on_${TSurS}Ksilic_${Type}_${Heat}K_${Time}ns.txt
done

