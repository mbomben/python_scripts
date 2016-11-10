import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import linspace,exp,asarray

import sys


def cumulativeCurr(file_name):
  
  input_file = open(file_name,'r')
  index = -1
  all_time = []
  all_current = []
  Q = 0.0
  input_lines = input_file.readlines()
  input_file.close()
  for input_line in input_lines:
    index += 1
    tmp = input_line.split()
    t = float(tmp[0])
    I = float(tmp[1])
    all_time.append(t)
    all_current.append(I)
  
  
  sall_time = asarray(all_time)
  sall_current = asarray(all_current)
  
  
  
  
  
  splrepint = interpolate.splrep(sall_time, sall_current, s=0)
  
  for time in all_time:
    charge = interpolate.splint(sall_time[0], time, splrepint)
    print time,charge
  
if __name__ == "__main__":
  if (len(sys.argv)!=2 ):
    print "Usage:",sys.argv[0],"<filename>"
    exit(2)
  filename = sys.argv[1]
  cumulativeCurr(filename)
