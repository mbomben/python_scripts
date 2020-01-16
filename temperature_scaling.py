import sys
from math import exp as exp
from math import pow as pow

def temperature_scaling(T,alpha=4.73e-4,beta=636,Tref=300,Egref=1.08):

  result = Egref + alpha*( (Tref*Tref)/(Tref+beta) - ((T*T)/(T+beta))  )

  return result


if (__name__=="__main__"):
  if ( len(sys.argv) < 2 or len(sys.argv) > 6 or len(sys.argv) == 3 ):
    print "Usage:",sys.argv[0],"<T (K)> [Tref (K) Egref (eV)] [<alpha (eV/K)>] [<beta (K)>]"
    exit(2)
  if ( len(sys.argv) == 2 ):
    T = float(sys.argv[1])
    Eg = temperature_scaling(T=T)
    print "Eg(",T,")=",Eg
  if ( len(sys.argv) == 4 ):
    T = float(sys.argv[1])
    Tref = float(sys.argv[2])
    Egref = float(sys.argv[3])
    Eg = temperature_scaling(T=T,Tref=Tref,Egref=Egref)
    print "Eg(",T,")=",Eg
  if ( len(sys.argv) == 5 ):
    T = float(sys.argv[1])
    Tref = float(sys.argv[2])
    Egref = float(sys.argv[3])
    alpha = float(sys.argv[4])
    Eg = temperature_scaling(T=T,Tref=Tref,Egref=Egref,alpha=alpha)
    print "Eg(",T,")=",Eg
  if ( len(sys.argv) == 6 ):
    T = float(sys.argv[1])
    Tref = float(sys.argv[2])
    Egref = float(sys.argv[3])
    alpha = float(sys.argv[4])
    beta  = float(sys.argv[5])
    Eg = temperature_scaling(T=T,Tref=Tref,Egref=Egref,alpha=alpha,beta=beta)
    print "Eg(",T,")=",Eg
