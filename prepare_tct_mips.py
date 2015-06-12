import argsParser_tct_mips
import sys
import re
import math
from readAndWrite import readAndWrite

pi = math.pi
args = argsParser_tct_mips.parser(sys.argv[1:])
template = args.template[0]

P = args.pitch[0]
W = args.thickness[0]
N = args.npixels[0]
# change it to rad
dY = args.deltay[0]
y0min = 0
y0max = W

nsteps = int((y0max-y0min)/dY)+1
print "expected number of steps:",nsteps

entry_point=[]
exit_point=[]
index=int()
y0=y0min
while ( y0<y0max):
  entry_point = [-N*P/2,y0]
  exit_point  = [N*P/2,y0]
  readAndWrite(template,index,entry_point,exit_point)
  y0+=dY
  index += 1
print "index = ",index,"\tnstes = ",nsteps
