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

fixed_appendix = '_PX2_Current.dat'
file_name = ''

save_file = template+'_DepthProfile.txt'

output_file = open(save_file,'w')

PX2_y=[0,0]
mid_point=0.0
track_length=0.0
index=int()
y0=y0min
trk_len=[]
Q=[]
q=0.0


while ( y0<y0max):
  #print "track_length = ",track_length
  file_name = template+'_'+str(index)+fixed_appendix
  file_name
  if (os.path.isfile(file_name)):
    q = integrateCurr(file_name,t0)
    depth = functions.inverse_func(0,T,y0)
    output_file.write('%f %e\n' % (depth, q))
    Q.append(q)
  y0+=dY
  index += 1
output_file.close()
