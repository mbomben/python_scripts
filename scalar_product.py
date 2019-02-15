import sys
import math
import numpy as np

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def scalar_product( numbers ):
  names  = ["ax","ay","az","bx","by","bz"]
  index = 0
  for number in numbers:
    if ( not is_number(numbers[index]) ): 
      print names[index],"is not a number:",number,
      print "Exiting...",
      return -1
    index = index + 1
  ax = float(numbers[0])
  ay = float(numbers[1])
  az = float(numbers[2])
  bx = float(numbers[3])
  by = float(numbers[4])
  bz = float(numbers[5])
  a = [ax,ay,az]
  b = [bx,by,bz]
  result = np.dot(a,b) 
  print "result is:", result
  return result

if (__name__ == "__main__"):

  values = []
  result = []
  if (len(sys.argv)!=7):
    print "Usage: ",sys.argv[0], "ax,ay,ax,bx,by,bz",
  else:
    ax = sys.argv[1]
    values.append(ax)
    ay = sys.argv[2]
    values.append(ay)
    az = sys.argv[3]
    values.append(az)
    bx = sys.argv[4]
    values.append(bx)
    by = sys.argv[5]
    values.append(by)
    bz = sys.argv[6]
    values.append(bz)
    result = scalar_product(values)
    print result,
    
