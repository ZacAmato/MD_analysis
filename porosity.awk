BEGIN{
Rho_c=0.94;              # in g/cm^3
N=500;                   # in shtukah
NAvogadro=6.02214129E23; # in 1/mol
mWater=18.0153;          # in g/mol
a=31.250566137700E-08;   # in cm.
}

function Phi(x) { return 1-(x/Rho_c) }
function Rho(x) { return ((N/NAvogadro) *mWater) / (a*a*x) }

/Maximum height/ {
  h=$4*1E-08; Density=Rho(h); Porosity=Phi(Density);
  printf("From MxHeight: Density  is %6.3f\n", Density);
  printf("From MxHeight: Porosity is %6.3f\n\n", Porosity) }

#/Average height/ {
 # h=$4*1E-08; Density=Rho(h); Porosity=Phi(Density);
  #printf("From AvHeight: Density  is %6.3f\n", Density);
  #printf("From AvHeight: Porosity is %6.3f\n", Porosity) }

END{}
