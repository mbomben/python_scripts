import sys

def bandgap(Eg0,T):
  alpha = 4.73e-4
  beta  = 636
  Eg    = Eg0-alpha*T*T/(T+beta)
  return Eg

if (__name__ == "__main__"):
  if (len(sys.argv) > 3 ):
    print "Usage:",sys.argv[0],"[Eg0 (eV)] [temperature (K)]\n"
    exit(2)
  Eg0   = 1.1696
  T     = 300
  if (len(sys.argv) > 2 ):
    Eg0 = float(sys.argv[1])
  if (len(sys.argv) == 3 ):
    T = float(sys.argv[2])
  Eg = bandgap(Eg0,T)
  print "For Eg0 = ", Eg0, " eV and at T = ",T, " K, bandgap energy is:"
  print "Eg = ", Eg, " eV"
