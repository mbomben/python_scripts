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
  
  

p = 4e3 # MeV
X0Si=9.36 # cm
w =4e-2 # cm
L1 = 59.800-15.200 #cm
L2 = 65.300-59.800 #cm
L3 = 104.100-65.300 #cm
print "L1=",L1,"cm"
print "L2=",L2,"cm"
print "L3=",L3,"cm"
theta = thetaMS(p,w,X0Si)
print "theta=",theta,"rad"     
deltay_tele1=L2*tan(theta)+L3*tan(sqrt(2)*theta)
print "deltay_tele1=",deltay_tele1*1e4,"um"
deltay_dut0=L1/(L1+L2+L3)*deltay_tele1
print "deltay_dut0=",deltay_dut0*1e4,"um"

