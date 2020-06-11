import sys
import os

def divide_2D(filename,scale_factor):


  input_file = open(filename,'r')

  input_lines = input_file.readlines()

  basename=os.path.splitext(filename)[0]
  ext = os.path.splitext(filename)[1]
  savefile = "%s_scaled_%2.1e%s" % (basename,scale_factor,ext)
  print("savefile is",savefile)

  output_file = open(savefile,'w')

  nlines = len(input_lines)


  for line in input_lines:
    tmp = line.split()
    X = float(tmp[0])
    Y = float(tmp[1])
    P = float(tmp[2])
    newP = P/scale_factor
    output_file.write('%e %e %e\n' % (X,Y,newP))

if __name__ == "__main__":
  if (len(sys.argv)!=3):
    print("Usage:",sys.argv[0],"<filename> <scale_factor>")
    exit(2)
  filename = sys.argv[1]
  scale_factor = float(sys.argv[2])
  divide_2D(filename,scale_factor)
