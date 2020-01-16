from mini_derivative import mini_derivative as mini_derivative
from math import fabs
import sys


def get_vdepl_from_C2V(file_name):
  input_file = open(file_name,'r')
  input_lines = input_file.readlines()
  X = []
  Y = []
  for input_line in input_lines:
    tmp = input_line.split()
    x = float(tmp[0])
    y = float(tmp[1])
    X.append(fabs(x))
    Y.append(fabs(y))
  maxder = 0
  vdepl =0
  vprev=0
  vnext=0
  nlines = len(X)
  index = -1
  for x in X:
    index = index + 1
    if ( index == 0 or index == nlines -1 ):
      continue
    #der = rough_derivative(file_name,x)
    der = mini_derivative(file_name,x)
    print x,der
    if ( fabs(der) > maxder ):
      maxder = der
      vdepl = x
      vprev=X[index-1]
      vnext=X[index+1]
  return vdepl

if __name__ == "__main__":
  if (len(sys.argv)!=2):
    print "Usage:",sys.argv[0],"<filename>"
    exit(2)
  filename = sys.argv[1]
  vdepl = get_vdepl_from_C2V(filename)
  print vdepl



