import sys
import os

def divide(filename,scale_factor):


  input_file = open(filename,'r')

  input_lines = input_file.readlines()

  basename=os.path.splitext(filename)[0]
  ext = os.path.splitext(filename)[1]
  savefile = "%s_divided%s" % (basename,ext)
  print("savefile is" + savefile)

  output_file = open(savefile,'w')

  nlines = len(input_lines)


  for line in input_lines:
    tmp = line.split()
    X = float(tmp[0])
    Y = float(tmp[1])
    if (Y == 0):
      continue
    newY = Y/scale_factor
    output_file.write('%f %e\n' % (X,newY))

if __name__ == "__main__":
  if (len(sys.argv)!=3):
    print("Usage: "+sys.argv[0]+" <filename> <scale_factor>")
    exit(2)
  filename = sys.argv[1]
  scale_factor = float(sys.argv[2])
  divide(filename,scale_factor)
