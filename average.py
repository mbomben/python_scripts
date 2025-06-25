
import sys

def average(x1,x2):
  return ((x1+x2)/2.)


if (__name__ == "__main__" ):
  if (len(sys.argv) != 3):
    print("Usage: ",sys.argv[0], "<num1> <num2>\n")
    exit(1)
  x1  = float(sys.argv[1])
  x2  = float(sys.argv[2])
  myaverage = average(x1,x2)
  print(myaverage)

