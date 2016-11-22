import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import linspace,exp,asarray
from mini_derivative import mini_derivative
from math import log as mathlog

import sys

def breakdown2(filename):
  #print "IV file is: ",filename
  formula="(dI/dV)/(I/V)"

  # reading data
  f = open(filename)
  lines = f.readlines()
  # writing data in lists
  V = []
  I = []
  for line in lines:
    tmp = line.split()
    v   = float(tmp[0])
    i   = float(tmp[1])
    if ( v == 0 ):
      continue
    V.append(v)
    I.append(i)

  # closing file
  f.close()

  # from lists to array
  V = np.asarray(V)
  I = np.asarray(I)
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


  index = 0
  logI = []
  for I in I:
    logi = mathlog(I)
    #print V[index],I,logi
    logI.append(logi)
    index = index + 1

  logI = np.asarray(logI)
  #logI = np.log(interpolated_I)
  interpolation_of_iv = interpolate.splrep(V, logI,k=5)
  dlogIdV = interpolate.splev(V,interpolation_of_iv,der=1)
  #observable_values = 1.0/dlogIdV
  v_bd = 0
  one_over_dlogIdV = 1.0/dlogIdV
  v_bd = V[np.argmax(dlogIdV)]
  #v_bd = V[np.argmin(one_over_dlogIdV)]

  #print "Breakdown voltage is:", v_bd,"V"


  # returning the interpolated current
  #return interpolated_I
  return v_bd



if __name__ == "__main__":
  if (len(sys.argv)!=2):
    print "Usage:",sys.argv[0],"<iv curve file>"
    exit(2)
  filename = sys.argv[1]
  V_bd = breakdown2(filename)
  print V_bd
