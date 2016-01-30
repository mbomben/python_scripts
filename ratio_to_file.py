import sys
import os

def ratio_to_file(filename,scale_factor,savefile):


  input_file = open(filename,'r')

  input_lines = input_file.readlines()

  print "savefile is",savefile

  output_file = open(savefile,'w')

  nlines = len(input_lines)


  for line in input_lines:
    tmp = line.split()
    X = float(tmp[0])
    Y = float(tmp[1])
    newY = Y/scale_factor
    output_file.write('%f %e\n' % (X,newY))

if __name__ == "__main__":
  if (len(sys.argv)!=4):
    print "Usage:",sys.argv[0],"<filename> <scale_factor> <savefile>"
    exit(2)
  filename = sys.argv[1]
  scale_factor = float(sys.argv[2])
  savefile = sys.argv[3]
  ratio_to_file(filename,scale_factor,savefile)
