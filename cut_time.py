import os
import sys
if (len(sys.argv) != 3):
  print "Usage:",sys.argv[0]," <filename> <tmax>",
  exit(2)
filename=sys.argv[1]
tmax = float(sys.argv[2])
#print os.path.splitext(filename)[0]
basename=os.path.splitext(filename)[0]
#print os.path.splitext(filename)[1]
ext = os.path.splitext(filename)[1]

s_tmax = "%s%2.1e" % ('_',tmax)
newname = basename + s_tmax + ext
print "The tmax file is:\n\t",newname
f = open(filename,'r')
g = open(newname,'w')
lines = f.readlines()
index = -1
for line in lines:
  index = index +1
  tmp = line.split()
  X = float(tmp[0])  
  if ( X > tmax ):
    continue
  else:
    Y = float(tmp[1]) 
    values = str(X) + ' ' +str(Y) + '\n'
    g.write(values)
f.close()
g.close() 
