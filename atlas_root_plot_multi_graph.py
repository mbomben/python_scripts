import sys
import atlas_root_multi_graph
from ROOT import gROOT, TCanvas, TGraph, TAxis, TMultiGraph, TLegend, gPad, TH1F, TString
import ROOT
from array import array
import xml.etree.ElementTree as ET
import AtlasStyle
import AtlasUtils
import AtlasLabels

def mp(filename,show=False): 
  ROOT.SetAtlasStyle()
  #filename = filename[0]
  tree = ET.parse(filename)
  root = tree.getroot()
  plot = atlas_root_multi_graph.plot()
  plot.build(root)
  #print "plot.get_filename()",plot.get_filename()
  #print "plot.get_title()",plot.get_title()

  title = plot.get_title()
  saveFile = plot.get_filename()
  axes = plot.get_axe()
  if (len(axes) != 2):
    print("\nThere must be 2 and only 2 axes, named X and Y.\nExiting...\n")
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
  tstring_title = TString(title)
  mgr = TMultiGraph('mgr',tstring_title.Data())
  if ( plot.get_legend() ):
    leg = plot.get_legend()
    x1 = leg.get_x1()
    x2 = leg.get_x2()
    y1 = leg.get_y1()
    y2 = leg.get_y2()
    leg = TLegend(x1,y1,x2,y2)
  else:  
    leg = TLegend(.6,.65,.89,.89)
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
  print ('X range %f %f' % (minX,maxX))
  minY = Yaxe.get_min()
  maxY = Yaxe.get_max()
  print ('Y range %f %f' % (minY,maxY))
  c1 = TCanvas('c1',title)
  c1.cd()
  gPad.Range(minX,maxX,minY,maxY)
  gPad.Draw()
  mgr.Draw('ALP')
  mgr.GetXaxis().SetRangeUser(minX,maxX)
  mgr.GetXaxis().SetTitle(Xaxe.get_label())
  mgr.GetYaxis().SetRangeUser(minY,maxY)
  mgr.GetYaxis().SetTitle(Yaxe.get_label())
  mgr.GetYaxis().SetTitleOffset(1.5)
  hmg = TH1F()
  hmg = mgr.GetHistogram();
  hmg.SetBins(100000000,hmg.GetXaxis().GetXmin(),hmg.GetXaxis().GetXmax());
  gPad.SetLogx(Xaxe.get_log())
  gPad.SetLogy(Yaxe.get_log())
  gPad.Modified()
  gPad.Update()
  mgr.GetXaxis().SetRangeUser(minX,maxX)
  mgr.GetYaxis().SetRangeUser(minY,maxY)

  try:
    atlaslabel = plot.get_atlasl()
  except:
    pass 
  try:
    xatlaslabel = atlaslabel.get_x()
  except:
    pass
  try:
    yatlaslabel = atlaslabel.get_y()
  except:
    pass
  try:
    coloratlaslabel = atlaslabel.get_color()
  except:
    pass
  try:
    #AtlasUtils.ATLAS_LABEL(xatlaslabel,yatlaslabel)
    #AtlasUtils.ATLASLabel(xatlaslabel,yatlaslabel)
    ROOT.ATLASLabel(xatlaslabel,yatlaslabel)
  except Exception as e: 
    print(e)
    #print("impossible to AtlasUtils.ATLAS_LABEL(xatlaslabel,yatlaslabel)")
    #print("impossible to AtlasUtils.ATLASLabel(xatlaslabel,yatlaslabel)")
    print("impossible to AtlasLabels.ATLASLabel(xatlaslabel,yatlaslabel)")
    pass
  
  try:
    mytext = plot.get_mytext()
    for mt in mytext:
      #AtlasUtils.myText(mt.get_x(),mt.get_y(),mt.get_color(),mt.get_label())
      ROOT.myText(mt.get_x(),mt.get_y(),mt.get_color(),mt.get_label())
  except:
    pass


  #c1.SetGrid(1,1)
  c1.SetTicks(1)
  leg.SetBorderSize(0)
  leg.SetTextSize(0.04)
  leg.SetFillStyle(0)
  leg.SetFillColor(0)
  leg.Draw()
  #leg.SetFillColor(10)
  save_pic = saveFile + '.png'
  print("Results will be saved in: %s\n\t" %(save_pic))
  c1.SaveAs(save_pic)
  save_pic = saveFile + '.pdf'
  print("Results will be saved in: %s\n\t" %(save_pic))
  c1.SaveAs(save_pic)
  save_pic = saveFile + '.C'
  print("Results will be saved in: %s\n\t" %(save_pic))
  c1.SaveAs(save_pic)
  mgr.DrawClone()
  leg.DrawClone()
  return c1

if (__name__ == "__main__"):
  ROOT.SetAtlasStyle()
  show = False
  if (len(sys.argv) < 2 or len(sys.argv) > 3 ):
    print("Usage: %s <filename.xml> [show]\n" % (sys.argv[0]))
    exit(2)
  if (len(sys.argv) == 3 ):
    show = True
  name = sys.argv[1]
  c = mp(name,show)
