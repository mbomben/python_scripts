
import sys

def read(filename):
  f = open(filename)
  lines = f.readlines()
  X=[]
  Y=[]
  for line in lines:
    tmp = line.split()
    x = float(tmp[0])
    y = float(tmp[1])
    X.append(x)
    Y.append(y)
  return (X,Y)

if (__name__ == "__main__"):
  if (len(sys.argv) != 2 ):
    print("Usage: %s <filename>\n" % (sys.argv[0]))
    exit(2)
  filename = sys.argv[1]
  X=[]
  Y=[]
  (X,Y) = read(filename)
  

