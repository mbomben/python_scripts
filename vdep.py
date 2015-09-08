import sys


def vdep(neff,d=300):
  d = d * 1e-4 # from um to cm
  e0 = 8.85e-14 # F/cm
  er = 11.8 
  q0 = 1.6e-19 # C
  v = q0*neff*d*d/2/e0/er # V
  return v


if __name__ == "__main__":
  if (len(sys.argv)< 2 or len(sys.argv) > 3):
    print "Usage:",sys.argv[0],"<Neff (cm-3)> [<d (um)>]"
    exit(2)
  neff = float(sys.argv[1])
  d=300
  if ( len(sys.argv) == 2):
    v=vdep(neff)
  if ( len(sys.argv) == 3):
    d = float(sys.argv[2])
    v=vdep(neff,d)
  print "Neff =",neff,"cm^-3"
  print "d    =",d,"um"
  print " ==>\tVdep =",v,"V"
