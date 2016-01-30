import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import linspace,exp,asarray
from mini_interpolate import mini_interpolate as mini_interpolate

import sys


def integrateCurr2(IT_filename,t0,t1,IV_filename,Vbias):
  
  input_file = open(IT_filename,'r')
  t0 = float(t0)
  t1 = float(t1)
  Vbias = float(Vbias)
  IV_filename = str(IV_filename)
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
    if ( t>t0 ):
      if ( t<t1 ):
        all_time.append(t)
        all_current.append(I)
  
  
  sall_time = asarray(all_time)
  sall_current = asarray(all_current)
  
  
  
  
  
  splrepint = interpolate.splrep(sall_time, sall_current, s=0)
  currentnew = interpolate.splev(sall_time, splrepint, der=0)
  initial_time = [t0/2.0]
  sinitial_time = asarray(initial_time)
  
  
  charge = interpolate.splint(sall_time[0], sall_time[len(all_time)-1], splrepint)
  dt = 0
  if ( t1 < sall_time[len(sall_time)-1] ):
    dt = t1-sall_time[0]
  else:
    dt = sall_time[len(sall_time)-1]-sall_time[0]
  Ileak = sall_current[len(sall_time)-1]
  currentnew = mini_interpolate(IV_filename,Vbias)
  #print "Ileak =", Ileak
  #print "currentnew =", currentnew
  charge -= Ileak*dt
  return charge
  
if __name__ == "__main__":
  if (len(sys.argv)!=6):
    print "Usage:",sys.argv[0],"<IT_filename> <t0> <t1> <IV_filename> <Vbias>"
    exit(2)
  IT_filename = sys.argv[1]
  t0 = sys.argv[2]
  t1 = sys.argv[3]
  IV_filename = sys.argv[4]
  Vbias = sys.argv[5]
  q = integrateCurr2(IT_filename,t0,t1,IV_filename,Vbias)
  print q
