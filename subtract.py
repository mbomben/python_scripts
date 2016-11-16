import sys
import os

def subtract(filename,subtract_factor):


  input_file = open(filename,'r')

  input_lines = input_file.readlines()

  basename=os.path.splitext(filename)[0]
  ext = os.path.splitext(filename)[1]
  savefile = "%s_subtracted_%2.1e%s" % (basename,subtract_factor,ext)
  #print "savefile is",savefile

  output_file = open(savefile,'w')

  nlines = len(input_lines)


  for line in input_lines:
    tmp = line.split()
    X = float(tmp[0])
    Y = float(tmp[1])
    newY = Y-subtract_factor
    output_file.write('%e %e\n' % (X,newY))

if __name__ == "__main__":
  if (len(sys.argv)!=3):
    print "Usage:",sys.argv[0],"<filename> <subtract_factor>"
    exit(2)
  filename = sys.argv[1]
  subtract_factor = float(sys.argv[2])
  subtract(filename,subtract_factor)
