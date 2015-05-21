import functions
import argsParser2
import sys
import re
import math
from readAndWrite import readAndWrite
from integrateCurr import integrateCurr
import os.path
import matplotlib.pyplot as plt

pi = math.pi
args = argsParser2.parser2(sys.argv[1:])
template = args.template[0]

P = args.pitch[0]
W = args.thickness[0]
T = args.theta[0]
# change it to rad
T *= pi/180.
dY = args.deltay[0]
y0min = functions.y0min_func(W,P,T,dY)
y0max = 1/2*P-dY
t0 = args.t0[0]

nsteps = int((y0max-y0min)/dY)+1
print "expected number of steps:",nsteps

fixed_appendix_PX2 = '_PX2_Current.dat'
fixed_appendix_PX3 = '_PX3_Current.dat'
file_name = ''

save_file = template+'_Cluster_ChargeProfile.txt'

output_file = open(save_file,'w')

PX2_y=[0,0]
mid_point=0.0
track_length=0.0
index=int()
y0=y0min
trk_len=[]
Q2=[]
Q3=[]
q=0.0


while ( y0<y0max):
  PX2_y[0] = -P/2
  PX2_y[1] =  P/2
  if functions.inverse_func(PX2_y[0],T,y0) < 0:
    PX2_y[0] = functions.direct_func(0,T,y0)
  if functions.inverse_func(PX2_y[1],T,y0) > W:
    PX2_y[1] = functions.direct_func(W,T,y0)
  mid_point = sum(PX2_y)/2.
  track_length = mid_point - y0
  #print "track_length = ",track_length
  #PX2 charge
  file_name = template+'_'+str(index)+fixed_appendix_PX2
  file_name
  if (os.path.isfile(file_name)):
    q = integrateCurr(file_name,t0)
    trk_len.append(track_length)
    Q2.append(q)
  #PX3 charge
  file_name = template+'_'+str(index)+fixed_appendix_PX3
  file_name
  if (os.path.isfile(file_name)):
    q = integrateCurr(file_name,t0)
    Q3.append(q)
  y0+=dY
  index += 1

# loop over index - match the exit point in z of PX3 to the entry point of PX2
shift=int(2*P/dY)
print "shift",shift
px1Q = []
px2Q = []
px3Q = []
px4Q = []
px5Q = []
px6Q = []
px7Q = []
px8Q = []
print "index",index

m=index/shift+1
print "m",m

r=index%shift
print "r",r



for i in range(index-1,index-r-1,-1):
  print i
  i12 = i
  i34 = i12 - shift
  i56 = i34 - shift
  i78 = i56 - shift
  px1Q.append(Q2[i12])
  px2Q.append(Q3[i12])
  px3Q.append(Q2[i34])
  px4Q.append(Q3[i34])
  px5Q.append(Q2[i56])
  px6Q.append(Q3[i56])
  px7Q.append(Q2[i78])
  px8Q.append(Q3[i78])
  output_file.write('%f %e %e %e %e %e %e %e %e\n' % (trk_len[i12], Q2[i12], Q3[i12], Q2[i34], Q3[i34], Q2[i56], Q3[i56], Q2[i78], Q3[i78]))
output_file.close()
