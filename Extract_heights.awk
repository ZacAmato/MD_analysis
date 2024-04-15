BEGIN{
iLine=0;
ZSum=0;
# This variable must be provided from command line along with ZZero
# iMaxDep=500; # must be an even number
}

/OW/ {iLine++; Z[iLine]=$4; ZSum=ZSum+$4}

END{

asort(Z);

# The height of the topmost water molecule.
MaximumHeight = Z[iMaxDep] - ZZero;
printf("Maximum height is %16.12f Angstrom\n",MaximumHeight);

# The height of the median molecule (251th for 500-molecule deposition)
iMedian=(iMaxDep / 2) + 1;
MedianHeight = Z[iMedian] - ZZero;
printf(" Median height is %16.12f Angstrom\n",MedianHeight);

# The average height of all molecules
AverageHeight = (ZSum / iMaxDep) - ZZero;
printf("Average height is %16.12f Angstrom\n",AverageHeight);

}
