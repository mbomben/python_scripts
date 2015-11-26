import os
import sys
if (len(sys.argv) != 3):
  print "Usage:",sys.argv[0]," <filename> <tmin>",
  exit(2)
filename=sys.argv[1]
tmin = float(sys.argv[2])
#print os.path.splitext(filename)[0]
basename=os.path.splitext(filename)[0]
#print os.path.splitext(filename)[1]
ext = os.path.splitext(filename)[1]

s_tmin = "%s%2.1e" % ('_min_',tmin)
newname = basename + s_tmin + ext
print "The tmin file is:\n\t",newname
f = open(filename,'r')
g = open(newname,'w')
lines = f.readlines()
index = -1
for line in lines:
  index = index +1
  tmp = line.split()
  X = float(tmp[0])  
  if ( X < tmin ):
    continue
  else:
    Y = float(tmp[1]) 
    values = str(X) + ' ' +str(Y) + '\n'
    g.write(values)
f.close()
g.close() 
