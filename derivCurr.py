import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import linspace,exp,asarray

import sys


def derivCurr(file_name,t0):
  
  input_file = open(file_name,'r')
  t0 = float(t0)
  index = -1
  all_time = []
  all_current = []
  Q = 0.0
  input_lines = input_file.readlines()
  input_file.close()
  for input_line in input_lines:
    index += 1
    if ( index < 4 ):
      continue
    tmp = input_line.split()
    t = float(tmp[0])
    I = float(tmp[1])
    all_time.append(t)
    all_current.append(I)
  
  
  sall_time = asarray(all_time)
  sall_current = asarray(all_current)
  array_t0 = asarray([t0]) 
  
  
  
  
  splrepint = interpolate.splrep(sall_time, sall_current, s=0)
  derivative_at_t0 = interpolate.splev(array_t0,splrepint, 1)
  
  
  charge = interpolate.splint(sall_time[0], sall_time[len(all_time)-1], splrepint)
  dt = sall_time[len(sall_time)-1]-sall_time[0]
  Ileak = sall_current[len(sall_time)-1]
  charge -= Ileak*dt
  return derivative_at_t0
  
if __name__ == "__main__":
  if (len(sys.argv)!=3):
    print "Usage:",sys.argv[0],"<filename> <t0>"
    exit(2)
  filename = sys.argv[1]
  t0 = sys.argv[2]
  q = derivCurr(filename,t0)
  print q
