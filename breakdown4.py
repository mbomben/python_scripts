import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import linspace,exp,asarray
from mini_derivative import mini_derivative
from math import log as mathlog

from scipy.interpolate import interp1d

import sys

def breakdown4(filename):
  #print "IV file is: ",filename
  formula="max(dI/dV)"

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
  #print V
  #print I



  f2 = interp1d(V, I, kind='cubic')
  #print interpolation_of_iv
  dIdV = f2(V)
  plt.plot(V, I, 'o', V, f2(V), '--')
  plt.legend(['data', 'cubic'], loc='best')
  plt.show()
  v_bd = 0
  v_bd = V[np.argmax(dIdV)]
  #print dIdV
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
  V_bd = breakdown4(filename)
  print V_bd
