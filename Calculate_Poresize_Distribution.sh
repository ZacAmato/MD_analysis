#! /usr/bin/bash

# A wrapper around the AVP program for calculation 'poresize distributions',
# e.g. the cumulative probability to find a pore of a radius bigger than R,
# and the corresponding probability density of that distribution.

# We first replace water molecules by 'WM' particles which are centered at
# the positions of the Q particles in the TIP4P/2005 model. The radius of
# the WM particles is set using the parameter 'RWater'. We then replicate
# the input ice structure 'iCell' by 'iCell' times in the XY plabe and
# surround it with a box of WM particles. Such a structure is the input to
# PSDsolv program. PSDSolv doesn't terminate on its own and infinitelly
# continues the calculations, so we terminate it after it has done 'PSDCycle'
# iterations. The PSDSolv parameters are 'PSDStart' and 'PSDGrid'. They are
# used to set up the smallest radius in the probability density and the grid
# of the points.

RWater="1.70"
iCell="2";
PSDCycle="90"
PSDStart="0.05"
PSDGrid="0.05"

# Processing arguments...
Prefix=$1;
ScrDir=$2;
TSurS=$3;
RUN=$4;
Heat=$5;
Type=$6;
Time=$7

if [ $# -ne 7 ]; then
   echo "Calculate_poresize_distribution_via_PSDSolv.sh expects precisely 6 arguments:"
   echo "   Full path to the  RUN directory of interest"
   echo "   Full path to a scratch directory"
   echo "   Space-separated list of TSurS of interest; it must be enclosed in \" \""
   echo "   Run number/Heating type/Time"
   echo "   Heating value"
   echo "   relax or heating?"
   echo "   time?"
   exit 1;
fi


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
    $PathPSD/psd $TmpDir/tmp-psd.xyz $PSDStart $PSDGrid 1>/dev/null &
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
