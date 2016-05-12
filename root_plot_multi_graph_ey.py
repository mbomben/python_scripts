import sys
import root_multi_graph
from ROOT import gROOT, TCanvas, TGraph, TAxis, TMultiGraph, TLegend, gPad, TH1F, TGraphErrors, nullptr 
from array import array

import xml.etree.ElementTree as ET

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
  curves = plot.get_curve()
  for curve in curves:
    file=curve.get_data()
    input_file = open(file,'r')
    lines = input_file.readlines()
    Y = []
    X = []
    EY = []
    for line in lines:
      tmp = line.split()
      X.append(float(tmp[0]))
      Y.append(float(tmp[1]))
      EY.append(float(tmp[2]))
    input_file.close()
    X=array('d',X)
    Y=array('d',Y)
    EY=array('d',EY)
    gr = TGraphErrors(len(X),X,Y,nullptr,EY)
    gr.SetTitle(curve.get_label())
    gr.SetMarkerStyle(curve.get_marker().get_style())
    gr.SetMarkerSize(curve.get_marker().get_size())
    gr.SetMarkerColor(curve.get_marker().get_color())
    gr.SetLineStyle(curve.get_line().get_style())
    gr.SetLineWidth(int(curve.get_line().get_size()))
    gr.SetLineColor(curve.get_line().get_color())
    mgr.Add(gr)
    leg.AddEntry(gr,gr.GetTitle(),'elp')


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

if (__name__ == "__main__"):
  show = False
  if (len(sys.argv) < 2 or len(sys.argv) > 3 ):
    print "Usage:",sys.argv[0],"<filename.xml> [show]\n";
    exit(2)
  if (len(sys.argv) == 3 ):
    show = True
  name = sys.argv[1]
  etreeminiparser(name,show)
