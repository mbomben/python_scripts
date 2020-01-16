from ROOT import *
import sys


def array_info(originale_file):
  gr = TGraph(originale_file)
  Y = gr.GetY()
  N = gr.GetN()
  mean = TMath.Mean(N,Y)
  rms  = TMath.RMS(N,Y)
  minY = Y[TMath.LocMin(N,Y)]
  maxY = Y[TMath.LocMax(N,Y)]
  print "Mean =",mean
  print "RMS  =",rms
  print "Min  =",minY
  print "Max  =",maxY
  
if __name__ == "__main__":
  if (len(sys.argv)!=1):
    print "Usage:",sys.argv[0],"<original file>"
    exit(2)
  original_filename = sys.argv[1]
  print "reading file:", original_filename
  array_info(original_filename)
