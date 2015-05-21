import functions
import mip_tracks_argsParser
import sys
import re
import math
from readAndWrite import readAndWrite

pi = math.pi
args = mip_tracks_argsParser.parser(sys.argv[1:])

P = args.pitch[0]
W = args.thickness[0]
T = args.theta[0]
# change it to rad
T *= pi/180. 
dY = args.deltay[0]
y0min = functions.y0min_func(W,P,T,dY)
y0max = 1/2*P-dY

nsteps = int((y0max-y0min)/dY)+1
#print "expected number of steps:",nsteps
print "y0min = ",y0min
print "y0max = ",y0max

entry_point=[]
exit_point=[]
index=int()
y0=y0min
while ( y0<y0max):
  entry_point = [y0,0]
  exit_point  = [3/2.*P,functions.inverse_func(3/2.*P,T,y0)]
  #print entry_point[0],entry_point[1],exit_point[0],exit_point[1]
  y0+=dY
  index += 1
#print "index = ",index,"\tnstes = ",nsteps
