import sys
import os
from math import sqrt as sqrt

def CV(filename):


  input_file = open(filename,'r')

  input_lines = input_file.readlines()

  basename=os.path.splitext(filename)[0]
  ext = os.path.splitext(filename)[1]
  savefile = "%s_CV%s" % (basename,ext)
  print "savefile is",savefile

  output_file = open(savefile,'w')

  nlines = len(input_lines)


  for line in input_lines:
    tmp = line.split()
    X = float(tmp[0])
    Y = float(tmp[1])
    newY = 1.0/sqrt(Y)
    output_file.write('%f %e\n' % (X,newY))

if __name__ == "__main__":
  if (len(sys.argv)!=2):
    print "Usage:",sys.argv[0],"<filename>"
    exit(2)
  filename = sys.argv[1]
  CV(filename)
