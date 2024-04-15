#!/bin/awk -f

# This script will multiply the provided cell either by 1x1 (i.e.leaving
# it the same) or by 2x2, or by 3x3 in the XY plane. In the output xyz file,
# the origin of the coordinate system in X and Y directions is located at the 
# center of the new cell.

# Input: Standarr .xyz file.
# Requiremnts: -- Concerning the XY plane, the origin of the coordinate system 
#                 must be located in the center of the cell.
#              -- The cell size in X and Y directions is 31.25...
# The variable iCell must be provided from outside, i.e. via `awk -v iCell=%i`.

BEGIN{iLine=0;CellSizeXY=31.250566137700; HalfCell=CellSizeXY/2.0}
FNR>2 {iLine++; Name[iLine]=$1; X[iLine]=$2; Y[iLine]=$3; Z[iLine]=$4}
END{
if(iCell==1){
  printf("%i\n=======\n", 1*iLine)
  for(i=1;i<=iLine;i++){
    printf("%5s%20.10f%20.10f%20.10f\n", Name[i],X[i],Y[i],Z[i])}}

if(iCell==2){
  printf("%i\n=======\n", 4*iLine)
  A=CellSizeXY;
  for(i=1;i<=iLine;i++) {NewX[i]=X[i]-HalfCell; NewY[i]=Y[i]+HalfCell}
  # The left-top, right-top, left-bot, and right-bot quadrants in the order of printing.
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],NewX[i]+0, NewY[i]+0, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],NewX[i]+A, NewY[i]+0, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],NewX[i]+0, NewY[i]+A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],NewX[i]+A, NewY[i]+A, Z[i])}}

if(iCell==3){
  printf("%i\n=======\n", 9*iLine)
  A=CellSizeXY;
  # The top-left, top-mid, and top-right quadrants in the order of printing.
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],   X[i]-A,    Y[i]+A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],   X[i]+0,    Y[i]+A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],   X[i]+A,    Y[i]+A, Z[i])}

  # The mid-left, mid-mid, and mid-right quadrants in the order of printing.
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],   X[i]-A,    Y[i]+0, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],   X[i]-0,    Y[i]+0, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],   X[i]+A,    Y[i]+0, Z[i])}

  # The bot-left, bot-mid, and bot-right quadrants in the order of printing.
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],   X[i]-A,    Y[i]-A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],   X[i]+0,    Y[i]-A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],   X[i]+A,    Y[i]-A, Z[i])}}

if(iCell==4){
  printf("%i\n=======\n",16*iLine)
  v3o2 = (3.0*CellSizeXY)/2.0
  v1o2 = (1.0*CellSizeXY)/2.0

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v3o2, Y[i]+v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1o2, Y[i]+v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1o2, Y[i]+v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v3o2, Y[i]+v3o2, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v3o2, Y[i]+v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1o2, Y[i]+v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1o2, Y[i]+v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v3o2, Y[i]+v1o2, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v3o2, Y[i]-v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1o2, Y[i]-v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1o2, Y[i]-v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v3o2, Y[i]-v1o2, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v3o2, Y[i]-v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1o2, Y[i]-v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1o2, Y[i]-v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v3o2, Y[i]-v3o2, Z[i])}
}

if(iCell==5){
  printf("%i\n=======\n",25*iLine)
  A=CellSizeXY
  v0A=0.0
  v1A=1*A
  v2A=2*A
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v2A, Y[i]+v2A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1A, Y[i]+v2A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v0A, Y[i]+v2A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1A, Y[i]+v2A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v2A, Y[i]+v2A, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v2A, Y[i]+v1A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1A, Y[i]+v1A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v0A, Y[i]+v1A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1A, Y[i]+v1A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v2A, Y[i]+v1A, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v2A, Y[i]+v0A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1A, Y[i]+v0A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v0A, Y[i]+v0A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1A, Y[i]+v0A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v2A, Y[i]+v0A, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v2A, Y[i]-v1A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1A, Y[i]-v1A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v0A, Y[i]-v1A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1A, Y[i]-v1A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v2A, Y[i]-v1A, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v2A, Y[i]-v2A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1A, Y[i]-v2A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v0A, Y[i]-v2A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1A, Y[i]-v2A, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v2A, Y[i]-v2A, Z[i])}}

if(iCell==6){
  printf("%i\n=======\n",36*iLine)
  v5o2=(5.0*CellSizeXY)/2.0
  v3o2=(3.0*CellSizeXY)/2.0
  v1o2=(1.0*CellSizeXY)/2.0

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v5o2, Y[i]+v5o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v3o2, Y[i]+v5o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1o2, Y[i]+v5o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1o2, Y[i]+v5o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v3o2, Y[i]+v5o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v5o2, Y[i]+v5o2, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v5o2, Y[i]+v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v3o2, Y[i]+v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1o2, Y[i]+v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1o2, Y[i]+v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v3o2, Y[i]+v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v5o2, Y[i]+v3o2, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v5o2, Y[i]+v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v3o2, Y[i]+v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1o2, Y[i]+v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1o2, Y[i]+v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v3o2, Y[i]+v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v5o2, Y[i]+v1o2, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v5o2, Y[i]-v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v3o2, Y[i]-v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1o2, Y[i]-v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1o2, Y[i]-v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v3o2, Y[i]-v1o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v5o2, Y[i]-v1o2, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v5o2, Y[i]-v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v3o2, Y[i]-v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1o2, Y[i]-v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1o2, Y[i]-v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v3o2, Y[i]-v3o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v5o2, Y[i]-v3o2, Z[i])}

  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v5o2, Y[i]-v5o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v3o2, Y[i]-v5o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]-v1o2, Y[i]-v5o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v1o2, Y[i]-v5o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v3o2, Y[i]-v5o2, Z[i])}
  for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i], X[i]+v5o2, Y[i]-v5o2, Z[i])}
}
}
