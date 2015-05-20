import sys
import trapping_parser
import trap_state
import xml.etree.ElementTree as ET
import numpy 
from sci_round import sci_round,  trim_err 

def average(nums):
  nums=numpy.asarray(nums)
  av=numpy.mean(nums)
  return av

def RMS(nums):
  nums=numpy.asarray(nums)
  rms=numpy.var(nums,ddof=1)
  return rms/numpy.sqrt(len(nums))


# parsing arguments
args = trapping_parser.trapping_parser(sys.argv[1:])
xml=args.xml[0]
velocities=args.velocities
ve=velocities[0]
vh=velocities[1]
fluence=args.fluence[0]
outputfilename=args.output[0]
f_Ts=args.f_T

# parsing xml
tree = ET.parse(xml)
root = tree.getroot()
model = trap_state.model()
model.build(root)
model_name = model.get_name()
print "Model name = ",model_name
traps = model.get_trap()
ntraps=len(traps)
nf_Ts=len(f_Ts)
if ( ntraps != nf_Ts ):
  print "For each trap a ionizing probabilities file is required"
  print "You have",ntraps,"traps but",nf_Ts,"ionizing probabilities files"
  exit(-1)


average_occ=list()
RMS_occ=list()
for f_T in f_Ts:
  with open(f_T,'rb') as f_Tfile:
    f_T_lines=f_Tfile.readlines()
  Z=list()
  for lines in f_T_lines:
    z=float(lines.split()[2])
    Z.append(z)
  mean=average(Z)
  rms=RMS(Z)
  average_occ.append(mean)
  RMS_occ.append(rms)
  print f_T,mean


index = 0
invtaue=0
invtauh=0
efactor=list()
hfactor=list()
for trap in traps:
  type=trap.get_type()
  eta=trap.get_eta()
  sigmae=trap.get_sigmae()
  sigmah=trap.get_sigmah()
  deg=trap.get_deg()
  energy=trap.get_energy()

  # electrons 
  occ=0
  if ( type == "A" ):
    occ = 1-average_occ[index]
  else:
    occ = average_occ[index]
  invtaue = invtaue+eta*fluence*occ*ve*sigmae
  efactor.append(eta*fluence*occ*ve*sigmae)

  # holes
  occ=0
  if ( type == "A" ):
    occ = average_occ[index]
  else:
    occ = 1-average_occ[index]
  invtauh = invtauh+eta*fluence*occ*vh*sigmah
  hfactor.append(eta*fluence*occ*vh*sigmah)

  index = index + 1

taue=1./invtaue  
tauh=1./invtauh

print "taue =",taue,"s"
print "tauh =",tauh,"s"

betae=invtaue/fluence
betah=invtauh/fluence

print "betae =",betae/1e9,"cm^2/ns"
print "betah =",betah/1e9,"cm^2/ns"

etausratio=0
htausratio=0
taue_sigma=0
tauh_sigma=0
index = 0
for index in range(ntraps):
  etausratio = etausratio+(RMS_occ[index]*(taue*efactor[index])**2)**2
  htausratio = htausratio+(RMS_occ[index]*(tauh*hfactor[index])**2)**2
tauesigma=etausratio**(0.5)
tauhsigma=htausratio**(0.5)


betaesigma=1/fluence*1/(taue*taue)*tauesigma
betahsigma=1/fluence*1/(tauh*tauh)*tauhsigma

print "tauesigma =",tauesigma,"s"
print "tauhsigma =",tauhsigma,"s"
tauesigma=sci_round(tauesigma)
tauhsigma=sci_round(tauhsigma)
betaesigma=sci_round(betaesigma)
betahsigma=sci_round(betahsigma)
print "tauesigma =",tauesigma,"s"
print "tauhsigma =",tauhsigma,"s"
print "betaesigma =",betaesigma,"s"
print "betahsigma =",betahsigma,"s"
short_taue=trim_err(taue,tauesigma)
short_tauh=trim_err(tauh,tauhsigma)
short_betae=trim_err(betae,betaesigma)
short_betah=trim_err(betah,betahsigma)
print "taue = ",short_taue,"+/-",tauesigma,"s"
print "tauh = ",short_tauh,"+/-",tauhsigma,"s"
print "betae = ",short_betae,"+/-",betaesigma,"s"
print "betah = ",short_betah,"+/-",betahsigma,"s"
taue_str= "taue = "+str(short_taue)+" +/- " + str(tauesigma) +" s"
tauh_str= "tauh = "+str(short_tauh)+" +/- " + str(tauhsigma) +" s"
betae_str= "betae = "+str(short_betae)+" +/- " + str(betaesigma) +" s"
betah_str= "betah = "+str(short_betah)+" +/- " + str(betahsigma) +" s"

outputfilename = outputfilename + '.txt'
with open(outputfilename,'wb') as ofile:
  ofile.write('%s\n' % model_name);
  ofile.write('%s\n' % taue_str);
  ofile.write('%s\n' % tauh_str);

