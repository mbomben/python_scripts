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
  
  

p = 5e3 # MeV - DESY
#p = 120e3 # MeV - CERN
X0Si=9.36 # cm
w =4e-2 # cm - detector only
#w =1.5 # cm - with box included
L1 = 59.800-15.200 #cm
L2 = 65.300-59.800 #cm
L3 = 104.100-65.300 #cm
print("L1 = %f cm" %(L1))
print("L2 = %f cm" %(L2))
print("L3 = %f cm" %(L3))
theta = thetaMS(p,w,X0Si)
print ("theta = %f rad" %(theta))     
deltay_tele1=L2*tan(theta)+L3*tan(sqrt(2)*theta)
#print "deltay_tele1=",deltay_tele1*1e4,"um"
deltay_dut0=L1/(L1+L2+L3)*deltay_tele1/((3.)**0.5)
print("deltay_dut0 = %f um" %(deltay_dut0*1e4))

