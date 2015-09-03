import sys
import superimpose
import numpy as np
import pylab as plt

import xml.etree.ElementTree as ET

def etreeminiparser(filename,show=False): 
  #filename = filename[0]
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

  index = 0
  for graph in data:
    X = graph[0]
    Y = graph[1]
    #X = np.asarray(X)
    #Y = np.asarray(Y)
#    plt.scatter(X,Y,marker=markers[index],label=labels[index],color=colors[index])
    plt.plot(X,Y,marker=markers[index],label=labels[index],color=colors[index],linestyle='None')
    index += 1
  minX = Xaxe.get_min()
  maxX = Xaxe.get_max()
  minY = Yaxe.get_min()
  maxY = Yaxe.get_max()
  plt.axis( [minX,maxX,minY,maxY])
  plt.legend(loc='upper right')
  plt.grid(True)
  plt.title(title)
  plt.xlabel(Xaxe.get_label())
  plt.ylabel(Yaxe.get_label())
  #stepX = int((maxX-minX)/10)
  #M. Bomben Fri Apr 24 14:49:56 CEST 2015
  #commenting out the 2 lines below
  #plt.xticks(np.arange(minX,maxX,100))
  #plt.yticks(np.arange(minY,maxY,0.1))
  #M. Bomben Fri Apr 24 14:49:56 CEST 2015
  save_pic = saveFile + '.png'
  print "Results will be saved in:\n\t",save_pic
  plt.savefig(save_pic)
  save_pic = saveFile + '.pdf'
  print "Results will be saved in:\n\t",save_pic,
  plt.savefig(save_pic)
  if ( show ):
    plt.show()

if (__name__ == "__main__"):
  show = False
  if (len(sys.argv) < 2 or len(sys.argv) > 3 ):
    print "Usage:",sys.argv[0],"<filename.xml> [show]\n";
    exit(2)
  if (len(sys.argv) == 3 ):
    show = True
  name = sys.argv[1]
  etreeminiparser(name,show)
