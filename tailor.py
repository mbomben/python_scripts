import os
import sys
if (len(sys.argv) != 3):
  print "Usage:",sys.argv[0]," <filename> <number of lines to cut>",
  exit(2)
filename=sys.argv[1]
num_of_lines_to_cut = int(sys.argv[2])
#print os.path.splitext(filename)[0]
basename=os.path.splitext(filename)[0]
#print os.path.splitext(filename)[1]
ext = os.path.splitext(filename)[1]

newname = basename + "_tailored" + ext
print "The tailored file is:\n\t",newname
f = open(filename,'r')
g = open(newname,'w')
lines = f.readlines()
index = -1
for line in lines:
  index = index +1
  if ( index > num_of_lines_to_cut ):
    continue
  else:
    tmp = line.split()
    X = float(tmp[0])  
    Y = float(tmp[1]) 
    values = str(X) + ' ' +str(Y) + '\n'
    g.write(values)
f.close()
g.close() 
