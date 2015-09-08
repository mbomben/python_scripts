import sys
from math import exp as exp
from math import pow as pow

def tScaleRD50(t,I=1,tref=20):
  offset = 273.15 # K
  T = t + offset # K
  Tref = tref + offset # K

  kboltz = 8.617343e-5 # eV/K
  egap = 1.21 # eV

  scale = pow((Tref/T),2) * exp( (-egap/(2.*kboltz)) * (1./Tref -1./T))

  return I*scale

if (__name__=="__main__"):
  if ( len(sys.argv) < 2 or len(sys.argv) > 4 ):
    print "Usage:",sys.argv[0],"<t (C)> [<current (A)>] [<referencetemperature (C)>]"
    exit(2)
  t = float(sys.argv[1])
  I=1
  tref=20
  if ( len(sys.argv) == 3 ):
    I = float(sys.argv[2])
  if ( len(sys.argv) == 4 ):
    tref = float(sys.argv[3])
  scaledCurrent = tScaleRD50(t,I,tref)
  scale = scaledCurrent/I
  print "Scaling",I,"A leakage current from",t,"C t",tref,"C"
  print "Scale factor =",scale
  print "Scaled current =",scaledCurrent
