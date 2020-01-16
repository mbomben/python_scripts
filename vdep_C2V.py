import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import linspace,exp,asarray
from mini_derivative import mini_derivative
import sys
from ROOT import gROOT, TCanvas, TGraph, TAxis, TMultiGraph, TLegend, gPad, TH1F, TString, TMath, TF1
from array import array

def vdep_C2V(original_file):
  with open(original_file,'rb') as original:
    original_lines=original.readlines()
  with open(original_file,'rb') as points:
    points_lines=points.readlines()

  all_V  = []
  all_C2 = []

  for original_line in original_lines:
    tmp = original_line.split()
    V  = float(tmp[0])
    C2 = float(tmp[1])
    #print t,I
    all_V.append(V)
    all_C2.append(C2)


  new_points = []
  for points_line in points_lines:
    tmp = points_line.split()
    V = float(tmp[0])
    #print t
    new_points.append(V)

  devC2 = []
  for new_point in new_points:
    devc2 = mini_derivative(original_file,new_point)
    devC2.append(float(devc2)) 

  #print devC2

  new_points = array('d',new_points)
  devC2 = array('d',devC2)

  gr = TGraph(len(new_points),new_points,devC2)
  imid = 0
  X = gr.GetX()
  Y = gr.GetY()
  devC20=devC2[0]
  new_all_C2 = array('d',all_C2)
  imax = TMath.LocMax(len(devC2),devC2)
  devC2max = devC2[imax]

  for i in range(len(new_points)):
    if ( Y[i] <  devC2max / 2.0 ):
      imid = i
      break

  f1 = TF1("f1","[0]*TMath::Erfc((x-[1])/[2])")
  f1.SetParameter(0,devC20)
  f1.SetParameter(1,X[imid])
  f1.SetParameter(2,X[imid]/5)
  f1.SetLineColor(2)
  gr.Fit("f1","Q")

  p1    = f1.GetParameter(1)
  p2    = f1.GetParameter(2)
  ep1   = f1.GetParError(1)
  ep2   = f1.GetParError(2)
  vdep  = p1+1.5*p2
  evdep = TMath.Sqrt((2*p2)**2+(ep1)**2+(ep2)**2)
  return (vdep,evdep)

if __name__ == "__main__":
  if (len(sys.argv)!=2):
    print "Usage:",sys.argv[0],"<original file>"
    exit(2)
  original_filename = sys.argv[1]
  (vdep,evdep)=vdep_C2V(original_filename)
  print "vdep = (",vdep," +/- ",evdep,") V"
