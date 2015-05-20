from math import log10, floor, ceil
from sys import argv

def sci_round(x):
  if (x==0):
    return x
  y=x
  negative=False
  if (x<0):
    y=-x
    negative=True
  w=floor(log10(y))
  z=y/10**w
  little=False
  if (z<3):
    z=y/10**(w-1)
    little=True
  k=floor(z)
  kplus1=ceil(z)
  dk=abs(k-z)
  dkplus1=abs(kplus1-z)
  if ( dk > dkplus1):
    k=ceil(z)
  if (little):
    k=(k)/10
  print x,y,w,z,k
  result=k*10**w
  if (negative):
    result=-result
  print result
  return result

def trim_err(value,err):

  if (not(err>0)):
    print"The error should be positive"
    exit(2)
  if ( abs(value) < err ):
    print"The central value is smaller (in magnitude) than the error"
    print"Consider quoting the result as 0+/-",err
    return 1
  negative=False
  if (value<0):
    negative=True
  value=abs(value)
  evalue=floor(log10(value))
  eerr=floor(log10(err))
  ratio=evalue-eerr
  value=value/10**eerr
  value=floor(value)
  value=value*10**eerr
  if (negative):
    value=-value
  print value
  return value

if (__name__ == "__main__"):
  if (len(argv) !=2):
    print "Usage",argv[0],"<number>"
    exit(-1)
  x = float(argv[1])
  sci_round(x)
