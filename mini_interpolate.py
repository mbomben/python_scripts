from scipy import interpolate
from numpy import asarray

import sys


def mini_interpolate(original_file,point):
  
  #print 'original data:\n'
  with open(original_file,'rb') as original:
    original_lines=original.readlines()
  all_time = []
  all_current = []
  for original_line in original_lines:
    tmp = original_line.split()
    t = abs(float(tmp[0]))
    I = float(tmp[1])
    #print t,I
    all_time.append(t)
    all_current.append(I)

  #print '\n'
  #print 'you want to interpolate to:',point
   
  sall_time = asarray(all_time)
  sall_current = asarray(all_current)
  point = float(point)
  spoint = asarray(point)
  splrepint = interpolate.splrep(sall_time, sall_current)
  currentnew = interpolate.splev(spoint, splrepint, der=0)
  
  #print 'I(',point,') =',currentnew
  return currentnew
  
if __name__ == "__main__":
  if (len(sys.argv)!=3):
    print("Usage: %s <original file> <new point file>\n" %(sys.argv[0]))
    exit(2)
  original_filename = sys.argv[1]
  point  = float(sys.argv[2])
  currentnew = mini_interpolate(original_filename,point)
  print (currentnew)
