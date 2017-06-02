import sys
import os
import read
def exchange_X_Y(filename):

  #input_file = open(filename,'r')

  #input_lines = input_file.readlines()

  basename=os.path.splitext(filename)[0]
  ext = os.path.splitext(filename)[1]
  savefile = "%s_exchanged_X_Y%s" % (basename,ext)
  print "savefile is",savefile

  output_file = open(savefile,'w')

  #nlines = len(input_lines)

  X=[]
  Y=[]
  (X,Y)=read.read(filename)

  index = 0

  for x in X:
    y = Y[index]
    output_file.write('%e %e\n' % (y,x))
    index = index + 1

if __name__ == "__main__":
  if (len(sys.argv)!=2):
    print "Usage:",sys.argv[0],"<filename>"
    exit(2)
  filename = sys.argv[1]
  exchange_X_Y(filename)
