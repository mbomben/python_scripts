import os
import sys
if (len(sys.argv) != 3):
  print("Usage: %s <filename> <number of lines to skip>" % (sys.argv[0]))
  #print("Usage: %s <filename>\n" % (sys.argv[0]))
  exit(2)
filename=sys.argv[1]
num_of_lines_to_skip = int(sys.argv[2])
#print os.path.splitext(filename)[0]
basename=os.path.splitext(filename)[0]
#print os.path.splitext(filename)[1]
ext = os.path.splitext(filename)[1]

newname = basename + "_pruned" + ext
print("The pruned file is:\n\t %s" %(newname))
f = open(filename,'r')
g = open(newname,'w')
lines = f.readlines()
index = -1
for line in lines:
  index = index +1
  if ( index < num_of_lines_to_skip ):
    continue
  else:
    tmp = line.split()
    X = float(tmp[0])  
    Y = float(tmp[1]) 
    values = str(X) + ' ' +str(Y) + '\n'
    g.write(values)
f.close()
g.close() 
