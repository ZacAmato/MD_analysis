#!/bin/awk -f

# This script builds a box which is '{X,Y,Z}add' angstromes bigger than the initial box 
# provided a s input. The box sides are made of 'Part' particles with the density 
# 'AtmPerAng' atoms per angstrom.
#
# The value of 'Part' must be provided from the outside.

BEGIN{ Xadd=0.0; Yadd=0.0; ZAdd = 0.0; AtmPerAng = 1/3.5; iLine=0; }

FNR==1 { iAtoms=$1; }
FNR>2 { iLine++; Name[iLine]=$1; X[iLine]=$2; Y[iLine]=$3; Z[iLine]=$4; }

END{

iLines = iLine;

asort(X,Xsorted);
asort(Y,Ysorted);
asort(Z,Zsorted);

# Getting the minimum and maxumum values in X, Y and Z directions:
Xmin = Xsorted[1]; Xmax = Xsorted[iLines];
Ymin = Ysorted[1]; Ymax = Ysorted[iLines];
Zmin = Zsorted[1]; Zmax = Zsorted[iLines];

# Setting up the grid of points for the box wall:
iXmax = int( (Xmax-Xmin)*AtmPerAng)+1;  StepX = (Xmax-Xmin) / iXmax;
iYmax = int( (Ymax-Ymin)*AtmPerAng)+1;  StepY = (Ymax-Ymin) / iYmax;
iZmax = int( (Zmax-Zmin)*AtmPerAng)+1;  StepZ = (Zmax-Zmin) / iZmax;

# Printing the number of molecules and the title line;
iTotalAtoms = iAtoms + 2*(iXmax+1)*(iYmax+1) + 2*(iYmax+1)*(iZmax+1) + 2*(iXmax+1)*(iZmax+1);
printf("%i\n=====\n", iTotalAtoms )

# Printing the initial (input) structure:
for (i=1; i<=iLines; i++) {print Name[i], X[i], Y[i], Z[i] }

# Printing the plane parallel to xy plane at Zmin:
for ( iX=1; iX<=iXmax+1; iX++) {
  for ( iY=1; iY <= iYmax+1; iY++ ) {
    printf("%s %f %f %f\n", Part, Xmin+(iX-1)*StepX, Ymin+(iY-1)*StepY, Zmin-Zadd )
  }
}

# Printing the plane parallel to xy plane at Zmax:
for ( iX=1; iX<=iXmax+1; iX++) {
  for ( iY=1; iY <= iYmax+1; iY++ ) {
    printf("%s %f %f %f\n", Part, Xmin+(iX-1)*StepX, Ymin+(iY-1)*StepY, Zmax+Zadd )
  }
}

# Printing the plane parallel to xz plane at Ymin:
for ( iX=1; iX<=iXmax+1; iX++) {
  for ( iZ=1; iZ<=iZmax+1; iZ++) {
    printf("%s %f %f %f\n", Part, Xmin+(iX-1)*StepX, Ymin-Yadd, Zmin+(iZ-1)*StepZ )
  }
}

# Printing the plane parallel to xz plane at Ymax:
for ( iX=1; iX<=iXmax+1; iX++) {
  for ( iZ=1; iZ<=iZmax+1; iZ++) {
    printf("%s %f %f %f\n", Part, Xmin+(iX-1)*StepX, Ymax+Yadd, Zmin+(iZ-1)*StepZ )
  }
}

# Printing the plane parallel to yz plane at Xmin:
for (iY=1; iY<=iYmax+1; iY++) {
  for ( iZ=1; iZ<=iZmax+1; iZ++ ) {
    printf("%s %f %f %f\n", Part, Xmin-Xadd, Ymin+(iY-1)*StepY, Zmin+(iZ-1)*StepZ)
  }
}

# Printing the plane parallel to yz plane at Xmax:
for (iY=1; iY<=iYmax+1; iY++) {
  for ( iZ=1; iZ<=iZmax+1; iZ++ ) {
    printf("%s %f %f %f\n", Part, Xmax+Xadd, Ymin+(iY-1)*StepY, Zmin+(iZ-1)*StepZ)
  }
}

}
