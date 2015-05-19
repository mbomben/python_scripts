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

save_file = template+'_ChargeProfile.txt'

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
  PX2_y[0] = -P/2
  PX2_y[1] =  P/2
  if functions.inverse_func(PX2_y[0],T,y0) < 0:
    PX2_y[0] = functions.direct_func(0,T,y0)
  if functions.inverse_func(PX2_y[1],T,y0) > W:
    PX2_y[1] = functions.direct_func(W,T,y0)
  mid_point = sum(PX2_y)/2.
  track_length = mid_point - y0
  #print "track_length = ",track_length
  file_name = template+'_'+str(index)+fixed_appendix
  file_name
  if (os.path.isfile(file_name)):
    q = integrateCurr(file_name,t0)
    output_file.write('%f %e\n' % (track_length, q))
    trk_len.append(track_length)
    Q.append(q)
  y0+=dY
  index += 1
#print "index = ",index,"\tnstes = ",nsteps
plt.plot(trk_len, Q,'ro' )
#plt.plot([0,1,2], [0,1,4],'ro' )
minX = min(trk_len)*0.9
maxX = max(trk_len)*1.1
minY = min(Q)*0.9
maxY = max(Q)*1.1
plt.axis( [minX,maxX,minY,maxY])
plt.title(save_file)
#plt.text(0.5,0.98,save_file,fontsize=20,horizontalalignment='center')
plt.xlabel('track length [um]')
plt.ylabel('Q [a.u.]')
output_file.close()
#plt.show()
save_pic  = template+'_ChargeProfile.png'
plt.savefig(save_pic)
