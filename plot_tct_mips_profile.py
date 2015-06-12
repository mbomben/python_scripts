import argsParser_tct_mips2
import sys
import re
import math
from readAndWrite import readAndWrite
from integrateCurr import integrateCurr
import os.path
import matplotlib.pyplot as plt

pi = math.pi
args = argsParser_tct_mips2.parser(sys.argv[1:])
template = args.template[0]

P = args.pitch[0]
W = args.thickness[0]
N = args.npixels[0]
# change it to rad
dY = args.deltay[0]
y0min = 0
y0max = W
t0 = args.t0[0]

nsteps = int((y0max-y0min)/dY)+1
print "expected number of steps:",nsteps

fixed_appendix = '_PX2_Current.dat'
file_name = ''

save_file = template+'_ChargeProfile.txt'

output_file = open(save_file,'w')

index=int()
y0=y0min
bulk_depth=[]
Q=[]
q=0.0


while ( y0<y0max):
  file_name = template+'_'+str(index)+fixed_appendix
  file_name
  if (os.path.isfile(file_name)):
    q = integrateCurr(file_name,t0)
    output_file.write('%f %e\n' % (y0, q))
    bulk_depth.append(y0)
    Q.append(q)
  y0+=dY
  index += 1
#print "index = ",index,"\tnstes = ",nsteps
plt.plot(bulk_depth, Q,'ro' )
#plt.plot([0,1,2], [0,1,4],'ro' )
minX = min(bulk_depth)*0.9
maxX = max(bulk_depth)*1.1
minY = min(Q)*0.9
maxY = max(Q)*1.1
plt.axis( [minX,maxX,minY,maxY])
plt.title(save_file)
#plt.text(0.5,0.98,save_file,fontsize=20,horizontalalignment='center')
plt.xlabel('bulk depth [um]')
plt.ylabel('Q [a.u.]')
output_file.close()
#plt.show()
save_pic  = template+'_ChargeProfile.png'
plt.savefig(save_pic)
