import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import linspace,exp,asarray

import sys


def integrator(file_name,x0,x1):
  
  input_file = open(file_name,'r')
  x0 = float(x0)
  x1 = float(x1)
  index = -1
  all_x = []
  all_y = []
  input_lines = input_file.readlines()
  input_file.close()
  for input_line in input_lines:
    index += 1
    tmp = input_line.split()
    x = float(tmp[0])
    y = float(tmp[1])
    #print t,I
    if ( x>x0 ):
      all_x.append(x)
      all_y.append(y)
  
  
  sall_x = asarray(all_x)
  sall_y = asarray(all_y)
  
  
  splrepint = interpolate.splrep(sall_x, sall_y, s=0) 
  integral = interpolate.splint(x0, x1, splrepint)
  
  
  
  return integral
  
if __name__ == "__main__":
  if (len(sys.argv)!=4):
    print "Usage:",sys.argv[0],"<filename> <x0> <x1>"
    exit(2)
  filename = sys.argv[1]
  x0 = sys.argv[2]
  x1 = sys.argv[3]
  integral = integrator(filename,x0,x1)
  print integral
