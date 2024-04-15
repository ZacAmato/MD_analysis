#!/bin/bash

TInc=$1;
Surf=$2;
Prefix=$3;
ScrDir=$4;
TSurS=$5;

NSteps=90; # Gives two accurate decimal places for 31x31 Angstrom surface 
           # and 500 deposited water molecules in ~1 minute.

XEnd="31.2506"; XStart="0.0000"; # Unit cell boundaries in X direction.
YEnd="31.2506"; YStart="0.0000"; # Unit cell boundaries in Y direction.

ORadius="1.4"; # Radius of the oxygen atom, in Angstroms.
HRadius="1.2"; # Radius of the hydrogen atom, in Angstroms.

echo 
echo "   Warning! Number of steps, {X,Y} cell boundaries, and O and H radii"
echo "   are hard-coded in ${0}." 
echo "   Make sure to adjust them for your system."

if [ $# -ne 5 ]; then
  echo "Calculate_surface_occlusion.sh expects precisely 5 arguments:"
  echo "   Incoming temperature in the format %3.3i"
  echo "   Name of the surface (silic or water)"
  echo "   Full path to a RUN directory of interest"
  echo "   Full path to a scratch directory"
  echo "   Space-separated list of TSurS of interest; it must be enclosed in \" \""
  exit 1;
fi

if [ ! `find $ScrDir -empty -type d` ]; then
  echo "   Scratch dir $ScrDir"
  echo "   doesn't exist or not empty. Aborting..."
  exit 1
fi


for TSur in $TSurS; do
  Folder=$Prefix/${TInc}Kwater_on_${TSurS}K$Surf

  if [ ! -f "$Folder/Heat_Ramps/5_ns/Analysis/XYZ/300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.xyz" ]; then
    echo
    echo "The file 300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.xyz doesn't exist in"
    echo "$Folder/Heat_Ramps/5_ns/Analysis/XYZ/"
    echo "Generate this file by using Pierre's script";
    exit 1;
  fi

  awk -v "ORadius=$ORadius" -v "HRadius=$HRadius" \
      '/OW/ {printf("%16.8f %16.8f %16.8f\n",$2,$3,ORadius)}
       /HW/ {printf("%16.8f %16.8f %16.8f\n",$2,$3,HRadius)}' \
       $Folder/Heat_Ramps/5_ns/Analysis/XYZ/300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.xyz > $ScrDir/tmp_pre_final_structure.xyr

  wcl=`wc -l $ScrDir/tmp_pre_final_structure.xyr | awk '{print $1}'`; 

  echo $wcl > $ScrDir/final_structure.xyr
  cat $ScrDir/tmp_pre_final_structure.xyr >> $ScrDir/final_structure.xyr

  # Let Maple compute the surface occlusion.
  /mnt/c/Users/Maple/maple2020/bin/maple -q <<MPEND
    restart;
    fd:=fopen("$ScrDir/final_structure.xyr",READ):
    iLines:=sscanf(readline(fd),"%d")[1]:
    for i from 1 to iLines do
     str:=sscanf(readline(fd),"%f %f %f");
     x0:=str[1]; y0:=str[2]; r0:=str[3];
     q1:=  (x-x0)^2 + (y-y0)^2 < r0^2 ;
     q[i]:= unapply(q1,x,y);
    end do:
    fclose(fd):
    L:=(a,b)->[seq(evalb(q[i](a,b)),i=1..iLines)]:

    NSteps:=$NSteps: 
    XEnd:=$XEnd: XStart:=$XStart: XStep:= (XEnd-XStart)/NSteps:
    YEnd:=$YEnd: YStart:=$YStart: YStep:= (YEnd-YStart)/NSteps:

    #printlevel:=3:

    with(ListTools):
    iShaded:=0: iNonShaded:=0:
    for iX from 0 to NSteps do
      X:= evalf(XStart + iX*XStep):
      for iY from 0 to NSteps do
        Y:= evalf(YStart + iY*YStep):
        ifShaded:= evalb( Occurrences(true, L(X,Y)) > 0):
        if(ifShaded) then 
          iShaded:=iShaded+1 
        else 
          iNonShaded:=iNonShaded+1 
        end if
      end do:
    end do:

    SurfOcclusion := evalf(iShaded / (NSteps+1)^2):

    fd:=fopen("$ScrDir/surface_occlusion.txt",WRITE):
    fprintf(fd,"SurfOcclusion= %f ",SurfOcclusion):
    fprintf(fd," NSteps= %d CPUTime= %f seconds\n",NSteps,time()):
    fclose(fd):
MPEND
  
  cp $ScrDir/surface_occlusion.txt $Folder/Heat_Ramps/5_ns/Analysis/Output_Files/Bash_Surface_Occ/Surface_Occ_300Kwater_on_${TSurS}K${Surf}_relax_${TSurS}K.txt

  rm -f $ScrDir/tmp_pre_final_structure.xyr
  rm -f $ScrDir/final_structure.xyr
  rm -f $ScrDir/surface_occlusion.txt

done
