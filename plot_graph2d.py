import sys
import plt_graph2d
import numpy as np
import matplotlib.pyplot as plt
import griddata
from matplotlib.colors import LogNorm

import xml.etree.ElementTree as ET

def etreeminiparser(filename):
  X = []
  Y = []
  V = []
  tree = ET.parse(filename)
  root = tree.getroot()
  plot = plt_graph2d.plot()
  plot.build(root)

  title = plot.get_title()
  saveFile = plot.get_filename()
  axes = plot.get_axe()
  for axe in axes:
    #print "axe.get_name()",axe.get_name()
    if ( axe.get_name() == 'X'  ):
      Xaxe = axe
    elif ( axe.get_name() == 'Y'  ):
      Yaxe = axe
    else:
      Zaxe = axe

  graph = plot.get_graph()
  file=graph.get_data()
  input_file = open(file,'r')
  lines = input_file.readlines()
  for line in lines:
    tmp = line.split()
    x = float(tmp[0])
    y = float(tmp[1])
    v = float(tmp[2])
    X.append(x)
    Y.append(y)
    V.append(v)
  input_file.close()
  npts = len(X)                           # the total number of data points.
  X = np.asarray(X)            # x data in array format
  Y = np.asarray(Y)            # y data in array format
  V = np.asarray(V)            # v data in array format
  
  # plot some profiles / cross-sections for some visualization.  our
  # function is a symmetric, upward opening paraboloid z = x**2 + y**2.
  # We expect it to be symmetric about and and y, attain a minimum on
  # the origin and display minor Gaussian noise.
  
  plt.ion()   # pyplot interactive mode on
  
  #plt.rc('text', usetex=True)
  #plt.rc('font', family='serif')
  
  # enter the gridding.  imagine drawing a symmetrical grid over the
  # plot above.  the binsize is the width and height of one of the grid
  # cells, or bins in units of x and y.
  bs=graph.get_binsize()
  binsize = bs
  grid, bins, binloc = griddata.griddata(X, Y, V, binsize=binsize)  # see this routine's docstring
  
  
  # minimum values for colorbar.
  vmin    = float( Zaxe.get_min() )
  vmax    = float( Zaxe.get_max() )
  # minimum values for x,y axes. 
  xmin    = Xaxe.get_min()
  xmax    = Xaxe.get_max()
  ymin    = Yaxe.get_min()
  ymax    = Yaxe.get_max()
  
  # colorbar stuff
  palette = plt.matplotlib.colors.LinearSegmentedColormap('jet3',plt.cm.datad['jet'],2048)
  palette.set_under(alpha=0.0)
  
  # plot the results.  first plot is x, y vs v, where v is a filled level plot.
  extent = (xmin,xmax,ymin,ymax) # extent of the plot
  #plt.subplot(1, 2, 1)
  log = Zaxe.get_log()
  if ( log ):
    #plt.imshow(grid, extent=extent, cmap=palette, origin='lower', vmin=vmin, vmax=vmax, aspect='auto', interpolation='bicubic', norm=LogNorm())
    plt.imshow(grid, extent=extent, cmap='jet', origin='lower', vmin=vmin, vmax=vmax, aspect='auto', interpolation='bicubic', norm=LogNorm())
  else:
    plt.imshow(grid, extent=extent, cmap=palette, origin='lower', vmin=vmin, vmax=vmax, aspect='auto', interpolation='bicubic')

  xtitle = Xaxe.get_label()
  plt.xlabel(xtitle)
  ytitle = Yaxe.get_label()
  plt.ylabel(ytitle)
  
  plt.title(title)
  cbar = plt.colorbar()
  ztitle = Zaxe.get_label()
  cbar.set_label(ztitle)
  plt.gca().invert_yaxis()
  #plt.clim(-500,0)
  plt.clim(vmin,vmax)
  #plt.zscale('log')
  #plt.savefig('razor.png')
  save_pic = saveFile + '.png'
  print("Results will be saved in:\n\t%s" % (save_pic))
  plt.savefig(save_pic)
  save_pic = saveFile + '.pdf'
  print("Results will be saved in:\n\t%s" % (save_pic))
  plt.savefig(save_pic)
  (nx,ny) = grid.shape
  Xmin, Xmax = X.min(), X.max()
  Ymin, Ymax = Y.min(), Y.max()
  xi      = np.arange(Xmin, Xmax+binsize, binsize)
  yi      = np.arange(Ymin, Ymax+binsize, binsize)
  xi, yi  = np.meshgrid(xi,yi)
  print(xi)
  #print yi
  #print grid
  print(nx, ny)
  print(type(xi))
  savefile = saveFile + '.txt'
  output_file = open(savefile,'w')
  for ix in range(nx):
    for iy in range(ny):
      output_file.write('%e %e %e\n' % (xi[ix][iy], yi[ix][iy], grid[ix][iy]))

if (__name__ == "__main__"):
  if ( len(sys.argv) != 2 ):
    print("Usage: %s <filename.xml>\n" % (sys.argv[0]))
    exit(2)
  name = sys.argv[1]
  etreeminiparser(name)
