import sys
import root_multi_graph
from ROOT import gROOT, TCanvas, TGraph, TAxis, TMultiGraph, TLegend, gPad, TH1F, TString
from array import array

import xml.etree.ElementTree as ET

defaultMarkerColor = 1
defaultMarkerStyle = 20
defaultMarkerSize  = 1.0

defaultLineColor = 1
defaultLineStyle = 1
defaultLineSize  = 0

def etreeminiparser(filename,show=False): 
  #filename = filename[0]
  tree = ET.parse(filename)
  root = tree.getroot()
  plot = root_multi_graph.plot()
  plot.build(root)
  #print "plot.get_filename()",plot.get_filename()
  #print "plot.get_title()",plot.get_title()

  title = plot.get_title()
  saveFile = plot.get_filename()
  axes = plot.get_axe()
  if (len(axes) != 2):
    print "\nThere must be 2 and only 2 axes, named X and Y.\nExiting...\n"
    exit(len(axes))
  for axe in axes:
    #print "axe.get_name()",axe.get_name()
    if ( axe.get_name() == 'X'  ):
      Xaxe = axe
    else:
      Yaxe = axe

  minX = 0
  maxX = 0
  minY = 0
  maxY = 0

# here starts the ROOT part
  mgr = TMultiGraph('mgr','')
  leg = TLegend(.6,.65,.89,.89)
  tstring_title = TString(title)
  #leg.SetHeader(tstring_title.Data())
  curves = plot.get_curve()
  for curve in curves:
    file=curve.get_data()
    input_file = open(file,'r')
    lines = input_file.readlines()
    Y = []
    X = []
    for line in lines:
      tmp = line.split()
      X.append(float(tmp[0]))
      Y.append(float(tmp[1]))
    input_file.close()
    X=array('d',X)
    Y=array('d',Y)
    gr = TGraph(len(X),X,Y)
    gr.SetTitle(curve.get_label())
    try:
      gr.SetMarkerStyle(curve.get_marker().get_style())
    except TypeError:
      gr.SetMarkerStyle(defaultMarkerStyle)
    try:
      gr.SetMarkerSize(curve.get_marker().get_size())
    except TypeError:
      gr.SetMarkerSize(defaultMarkerSize)
    try:
      gr.SetMarkerColor(curve.get_marker().get_color())
    except TypeError:
      gr.SetMarkerColor(defaultMarkerColor)
    try:
      gr.SetLineStyle(curve.get_line().get_style())
    except TypeError:
      gr.SetLineStyle(defaultLineStyle)
    try:
      int(curve.get_line().get_size())
    except TypeError:
      gr.SetLineWidth(defaultLineSize)
    try:
      gr.SetLineWidth(int(curve.get_line().get_size()))
    except TypeError:
      gr.SetLineWidth(defaultLineSize)
    gr.SetLineColor(curve.get_line().get_color())
    mgr.Add(gr)
    leg.AddEntry(gr,gr.GetTitle(),'lp')


# real design part



  minX = Xaxe.get_min()
  maxX = Xaxe.get_max()
  print 'X range',minX,maxX
  minY = Yaxe.get_min()
  maxY = Yaxe.get_max()
  print 'Y range',minY,maxY
  c1 = TCanvas('c1',title,2000,1000)
  c1.cd()
  gPad.Range(minX,maxX,minY,maxY)
  gPad.Draw()
  mgr.Draw('ALP')
  mgr.GetXaxis().SetRangeUser(minX,maxX)
  mgr.GetXaxis().SetTitle(Xaxe.get_label())
  mgr.GetYaxis().SetRangeUser(minY,maxY)
  mgr.GetYaxis().SetTitle(Yaxe.get_label())
  hmg = TH1F()
  hmg = mgr.GetHistogram();
  hmg.SetBins(100000000,hmg.GetXaxis().GetXmin(),hmg.GetXaxis().GetXmax());
  gPad.Modified()
  gPad.Update()

  c1.SetGrid(1,1)
  c1.SetTicks(1)
  leg.Draw()
  #leg.SetFillColor(10)
  save_pic = saveFile + '.png'
  print "Results will be saved in:\n\t",save_pic
  c1.SaveAs(save_pic)
  save_pic = saveFile + '.pdf'
  print "Results will be saved in:\n\t",save_pic,
  c1.SaveAs(save_pic)
  save_pic = saveFile + '.C'
  print "Results will be saved in:\n\t",save_pic,
  c1.SaveAs(save_pic)
  mgr.DrawClone()
  leg.DrawClone()
  return c1

if (__name__ == "__main__"):
  show = False
  if (len(sys.argv) < 2 or len(sys.argv) > 3 ):
    print "Usage:",sys.argv[0],"<filename.xml> [show]\n";
    exit(2)
  if (len(sys.argv) == 3 ):
    show = True
  name = sys.argv[1]
  c = etreeminiparser(name,show)
