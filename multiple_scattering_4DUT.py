# module to evaluate the MS effect at the DESY 2015 testbeam
# 2 DUTs, 200 um thick each + 200 um FE

import math
pi = math.pi
tan = math.tan
sqrt = math.sqrt
log = math.log

def thetaMS(p,w,X0):
  theta = 13.6/p*sqrt(w/X0)*(1+0.038*log(w/X0))
  return theta
  
  

#p = 4e3 # MeV - DESY
p = 120e3 # MeV - CERN
X0Si=9.36 # cm
#w =4e-2 # cm - detector only
w =4.5 # cm - with box included
L1 = 25.7 #cm
L2 = 1.5 #cm
L3 = 9.5 #cm
L4 = 3.0 #cm
L5 = 32.5 # cm
print "L1=",L1,"cm"
print "L2=",L2,"cm"
print "L3=",L3,"cm"
print "L4=",L4,"cm"
print "L5=",L5,"cm"
theta = thetaMS(p,w,X0Si)
print "theta=",theta,"rad"     
deltay_tele1=L2*tan(theta)+L3*tan(sqrt(2)*theta)+L4*tan(sqrt(3)*theta)+L5*(sqrt(4)*theta)
#print "deltay_tele1=",deltay_tele1*1e4,"um"
deltay_dut0=L1/(L1+L2+L3+L4+L5)*deltay_tele1/((3.)**0.5)
print "deltay_dut0=",deltay_dut0*1e4,"um"
deltay_dut3=(L1+L2+L3+L4)/(L1+L2+L3+L4+L5)*deltay_tele1/((3.)**0.5)
print "deltay_dut3=",deltay_dut3*1e4,"um"

