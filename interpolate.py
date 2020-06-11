from scipy import interpolate
from numpy import asarray
from mini_interpolate import mini_interpolate

import sys


def interpolate(original_file,points_file,result_file):
  
  with open(original_file,'r') as original:
    original_lines=original.readlines()
  with open(points_file,'r') as points:
    points_lines=points.readlines()
  #with open(result_file,'wb') as result:
  all_time = []
  all_current = []
  for original_line in original_lines:
    tmp = original_line.split()
    t = float(tmp[0])
    I = float(tmp[1])
    #print t,I
    all_time.append(t)
    all_current.append(I)

  new_points = []
  for points_line in points_lines:
    tmp = points_line.split()
    t = float(tmp[0])
    #print t
    new_points.append(t)

  #print new_points
  #print len(all_time)
  #print all_current
   
  sall_time = asarray(all_time)
  #print sall_time[3]
  sall_current = asarray(all_current)
  #print sall_current[3]
  new_currents = []
  with open(result_file,'w') as ofile:
    for new_point in new_points:
      new_current = mini_interpolate(original_file,new_point)
      new_currents.append(new_current)
      ofile.write('%e %e\n' % (new_point,new_current))
  
    
  #splrepint = interpolate.splrep(sall_time, sall_current)
#  splrepint = interpolate.splrep(sall_time, sall_current, s=0)
#  currentnew = interpolate.splev(snew_points, splrepint, der=0)
  
#  index = 0
#  for icurrentnew in currentnew:
#    print index,new_points[index],currentnew[index]
  
  
if __name__ == "__main__":
  if (len(sys.argv)!=4):
    print("Usage: %s ""<original file> <points file> <new results file>\n" % (sys.argv[0]))
    exit(2)
  original_filename = sys.argv[1]
  points_filename  = sys.argv[2]
  new_filename = sys.argv[3]
  interpolate(original_filename,points_filename,new_filename)
  print("interpolated file is: %s\n" % (new_filename))
