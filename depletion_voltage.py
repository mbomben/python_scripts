import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import linspace,exp,asarray
from mini_derivative import mini_derivative
from math import log as mathlog

import sys

def depletion_voltage(filename):
  #print "IV file is: ",filename

  # reading data
  f = open(filename)
  lines = f.readlines()
  # writing data in lists
  V = []
  C = []
  for line in lines:
    tmp = line.split()
    v   = float(tmp[0])
    c   = float(tmp[1])
    if ( v == 0 ):
      continue
    if ( c == 0 ):
      continue
    V.append(v)
    C.append(c)

  # closing file
  f.close()

  # from lists to array
  V = np.asarray(V)
  C = np.asarray(C)
  # creating an interporlation of the IV curve
  #interpolation_of_iv = interpolate.splrep(V, I,k=5)
  #interpolated_I = interpolate.splev(V,interpolation_of_iv,der=0)
  # plot a comparison
  #plt.figure()
  #plt.plot(V, I, 'xb',V,interpolated_I,'-r')
  #plt.legend(['Data','Interpolation'],loc=6)
  #plt.xlabel('Vbias [V]')
  #plt.ylabel('Ileak [nA]')
  #plt.yscale('log')
  #plt.title('IV, W93, S1')
  #plt.show()


  # calculating log and derivative
  #interpolated_I = np.asarray(interpolated_I)
  #print interpolated_I


  logC = []
  logV = []
  for c in C:
    logc = mathlog(c)
    logC.append(logc)

  for v in V:
    logv = mathlog(v)
    logV.append(logv)

  logC = np.asarray(logC)
  logV = np.asarray(logV)
  #logI = np.log(interpolated_I)
  interpolation_of_logClogV = interpolate.splrep(logV, logC,k=5)
  dlogCdV = interpolate.splev(logV,interpolation_of_logClogV,der=1)
  vmin = V[np.argmin(dlogCdV)]
  vmax = V[np.argmax(dlogCdV)]
  v_depl = (vmin+vmax)/2.0
  #v_bd = V[np.argmin(one_over_dlogIdV)]

  #print "Breakdown voltage is:", v_bd,"V"


  # returning the interpolated current
  #return interpolated_I
  return v_depl



if __name__ == "__main__":
  if (len(sys.argv)!=2):
    print "Usage:",sys.argv[0],"<cv curve file>"
    exit(2)
  filename = sys.argv[1]
  V_depl = depletion_voltag(filename)
  print V_depl
