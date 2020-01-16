import sys
from math import fabs as fabs


def get_maximum(file_name):
  input_file = open(file_name,'r')
  input_lines = input_file.readlines()
  X = []
  Y = []
  for input_line in input_lines:
    tmp = input_line.split()
    x = float(tmp[0])
    y = float(tmp[1])
    X.append(fabs(x))
    Y.append(y)
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
    der = Y[index]
    #print x,der
    if ( der > maxder ):
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
  vdepl = get_maximum(filename)
  print vdepl



