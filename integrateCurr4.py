import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import linspace,exp,asarray

import sys


def integrateCurr4(file_name,t0,t1,iS):
  
  input_file = open(file_name,'r')
  t0 = float(t0)
  t1 = float(t1)
  index = -1
  all_time = []
  all_current = []
  Q = 0.0
  input_lines = input_file.readlines()
  input_file.close()
  Ileak = 0
  for input_line in input_lines:
    index += 1
    tmp = input_line.split()
    t = float(tmp[0])
    I = float(tmp[1])
    #print t,I
    if ( index == 0 ):
      Ileak = I
    if ( t>t0 ):
      all_time.append(t)
      all_current.append(I)
  
  
  sall_time = asarray(all_time)
  sall_current = asarray(all_current)
  
  
  
  
  
  splrepint = interpolate.splrep(sall_time, sall_current, s=0)
  currentnew = interpolate.splev(sall_time, splrepint, der=0)
  initial_time = [t0/2.0]
  sinitial_time = asarray(initial_time)
  
  tf = 0
  if (t1 == -1):
    tf = sall_time[len(all_time)-1]
  else:
    tf = t1
  
  charge = interpolate.splint(sall_time[0], tf, splrepint)
  dt = tf-sall_time[0]
  #Ileak = sall_current[len(sall_time)-1]
  currentnew = interpolate.splev(sinitial_time, splrepint, der=0)
  #print "Ileak =", Ileak
  #print "currentnew =", currentnew
  if ( iS == 1 ):
    charge -= Ileak*dt
  return charge
  
if __name__ == "__main__":
  if (len(sys.argv)!=3 and len(sys.argv)!=4 and len(sys.argv)!=5):
    print "Usage:",sys.argv[0],"<filename> <t0> [<t1>] [<subtract leakage current>]"
    exit(2)
  if (len(sys.argv)==5):
    filename = sys.argv[1]
    t0 = sys.argv[2]
    t1 = sys.argv[3]
    iS = int(sys.argv[4])
    if ( iS != 0 and iS != 1 ):
      print "subtract leakage current has to be either 1 or 0"
      exit(5)
  elif (len(sys.argv)==4):
    filename = sys.argv[1]
    t0 = sys.argv[2]
    t1 = sys.argv[3]
    iS = 1
  else :
    filename = sys.argv[1]
    t0 = sys.argv[2]
    t1 = -1
    iS = 1
  q = integrateCurr4(filename,t0,t1,iS)
  print q
