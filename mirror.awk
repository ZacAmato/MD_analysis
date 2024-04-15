#!/bin/awk -f

BEGIN{iLine=0;Shift=Separation/2}

FNR>2 {iLine++; Name[iLine]=$1; X[iLine]=$2; Y[iLine]=$3; Z[iLine]=$4}

END{
asort(Z,ZSorted);
ZZero=ZSorted[1];
printf("%i\n=======\n", 2*iLine )
for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],X[i],Y[i],  Z[i]-ZZero+Shift) }
for(i=1;i<=iLine;i++) {printf("%5s%20.10f%20.10f%20.10f\n", Name[i],X[i],Y[i],-(Z[i]-ZZero+Shift))}
}
