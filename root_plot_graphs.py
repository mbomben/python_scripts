import sys
import superimpose
import pylab as plt
from ROOT import gROOT, TCanvas, TGraph, TAxis, TMultiGraph, TLegend
from array import array

import xml.etree.ElementTree as ET

def etreeminiparser(filename,show): 
  filename = filename[0]
  tree = ET.parse(filename)
  root = tree.getroot()
  plot = superimpose.plot()
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

  X = []
  Y = []
  data = []
  ifile = 0
  minX = 0
  maxX = 0
  minY = 0
  maxY = 0

  graph = []
  labels =[]
  markers = []
  colors = []
  curves = plot.get_curve()
  for curve in curves:
    file=curve.get_data()
    input_file = open(file,'r')
    markers.append(curve.get_marker())
    colors.append(curve.get_color())
    labels.append(curve.get_label())
    lines = input_file.readlines()
    Y = []
    X = []
    for line in lines:
      tmp = line.split()
      X.append(float(tmp[0]))
      Y.append(float(tmp[1]))
    graph = [X,Y]
    data.append(graph)
    ifile += 1

  #print markers
  #print labels

  input_file.close()
# real design part

# here starts the ROOT part
  graphs = []
  mgr = TMultiGraph('mgr','')

  index = 0
  for graph in data:
    X = graph[0]
    Y = graph[1]
    X=array('d',X)
    Y=array('d',Y)
    gr = TGraph(len(X),X,Y)
    gr.SetTitle(labels[index])
    gr.SetMarkerStyle(int(markers[index]))
    gr.SetMarkerColor(int(colors[index]))
    graphs.append(gr)
    mgr.Add(gr)

#    plt.scatter(X,Y,marker=markers[index],label=labels[index],color=colors[index])
#    plt.plot(X,Y,marker=markers[index],label=labels[index],color=colors[index],linestyle='None')
    index += 1


  c1 = TCanvas('c1','',2000,1000)
  c1.cd()
  mgr.Draw('AP')
  minX = Xaxe.get_min()
  maxX = Xaxe.get_max()
  minY = Yaxe.get_min()
  maxY = Yaxe.get_max()
  mgr.GetXaxis().SetRangeUser(minX,maxX)
  mgr.GetXaxis().SetTitle(Xaxe.get_label())
  mgr.GetYaxis().SetRangeUser(minY,maxY*1.2)
  mgr.GetYaxis().SetTitle(Yaxe.get_label())
  c1.SetGrid(1,1)
  c1.SetTicks(1)
  leg = TLegend(.6,.75,.89,.89)
  for graph in graphs:
    leg.AddEntry(graph,graph.GetTitle(),'p')
  leg.Draw()
  #leg.SetFillColor(10)
  c1.Update()
#  plt.axis( [minX,maxX,minY,maxY])
#  plt.legend(loc='upper right')
#  plt.grid(True)
#  plt.title(title)
#  plt.xlabel(Xaxe.get_label())
#  plt.ylabel(Yaxe.get_label())
  save_pic = saveFile + '.png'
  print "Results will be saved in:\n\t",save_pic
  c1.SaveAs(save_pic)
  save_pic = saveFile + '.pdf'
  print "Results will be saved in:\n\t",save_pic,
  c1.SaveAs(save_pic)
#  if ( show ):
#    plt.show()

if (__name__ == "__main__"):
  show = False
  if (len(sys.argv) < 2 or len(sys.argv) > 3 ):
    print "Usage:",sys.argv[0],"<filename.xml> [show]\n";
    exit(2)
  if (len(sys.argv) == 3 ):
    show = True
  etreeminiparser(sys.argv[1:],show)
