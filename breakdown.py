import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import linspace,exp,asarray
from mini_derivative import mini_derivative

import sys

def breakdown(filename,threshold):
  print "IV file is: ",filename
  formula="(dI/dV)/(I/V)"
  look_for_threshold = True
  if ( threshold < 0 ):
    print "I will look for the maximum of:",formula
    look_for_threshold = False
  else:
    print "I will look for the voltage at which:",formula,">",threshold

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
  interpolation_of_iv = interpolate.splrep(V, I,k=5)
  interpolated_I = interpolate.splev(V,interpolation_of_iv,der=0)
  # plot a comparison
  #plt.figure()
  #plt.plot(V, I, 'xb',V,interpolated_I,'-r')
  #plt.legend(['Data','Interpolation'],loc=6)
  #plt.xlabel('Vbias [V]')
  #plt.ylabel('Ileak [nA]')
  #plt.yscale('log')
  #plt.title('IV, W93, S1')
  #plt.show()


  # calculating derivative and ratios
  I_over_V = I/V
  dIdV = interpolate.splev(V,interpolation_of_iv,der=1)
  observable_values = dIdV/I_over_V
  v_bd = 0
  index = 0
  nlines = len(V)
  if ( look_for_threshold ):
    for v in V:
      observable = observable_values[index]
      i = I[index]
      if ( observable > threshold ):
        v_bd = v
        break
      index = index + 1
  else:
    max_obs = 0
    save_index = 0
    for v in V:
      observable = observable_values[index]
      if ( observable > max_obs ):
        save_index = index
        max_obs = observable
      index = index + 1
    v_bd = V[save_index]

  print "Breakdown voltage is:", v_bd,"V"


  # returning the interpolated current
  return interpolated_I



if __name__ == "__main__":
  if (len(sys.argv)!=2 and len(sys.argv)!=3):
    print "Usage:",sys.argv[0],"<iv curve file> [<threshold>]"
    exit(2)
  filename = sys.argv[1]
  threshold = -1
  if (len(sys.argv)==3):
    threshold = float(sys.argv[2])
  I = breakdown(filename,threshold)
