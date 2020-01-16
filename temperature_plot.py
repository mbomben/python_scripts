import sys
import numpy as np
import matplotlib.pyplot as plt
import griddata
import matplotlib.tri as tri

def temperature_plot(filename):  
  X = []
  Y = []
  V = []
  for line in open(filename):
    tmp = line.split()
    x = float(tmp[0])
    y = float(tmp[1])
    v = float(tmp[2])
    X.append(x)
    Y.append(y)
    V.append(v)
  
  X = np.asarray(X)            # x data in array format
  Y = np.asarray(Y)            # y data in array format
  V = np.asarray(V)            # v data in array format
  
  # plot some profiles / cross-sections for some visualization.  our
  # function is a symmetric, upward opening paraboloid z = x**2 + y**2.
  # We expect it to be symmetric about and and y, attain a minimum on
  # the origin and display minor Gaussian noise.
  
  plt.ion()   # pyplot interactive mode on
  
  
  # enter the gridding.  imagine drawing a symmetrical grid over the
  # plot above.  the binsize is the width and height of one of the grid
  # cells, or bins in units of x and y.
  binsize = 5
  grid, bins, binloc = griddata.griddata(X, Y, V, binsize=binsize)  # see this routine's docstring
  
  
  # minimum values for colorbar. filter our nans which are in the grid
  vmin    = grid[np.where(np.isnan(grid) == False)].min()
  vmax    = grid[np.where(np.isnan(grid) == False)].max()
  
  # colorbar stuff
  palette = plt.matplotlib.colors.LinearSegmentedColormap('jet3',plt.cm.datad['jet'],2048)
  palette.set_under(alpha=0.0)


  # plot the results.  first plot is x, y vs v, where v is a filled level plot.
  extent = (X.min(), X.max(), Y.min(), Y.max()) # extent of the plot
  #plt.subplot(1, 2, 1)
  plt.imshow(grid, extent=extent, cmap=palette, origin='lower', vmin=vmin, vmax=vmax, aspect='auto', interpolation='bicubic')
  #plt.imshow(grid, extent=extent, cmap=palette, origin='lower', vmin=vmin, vmax=vmax, aspect='auto', interpolation='bicubic',levels=[0,100,200,300,400,500])
  plt.xlabel(r'$X\, [\mu m]$')
  plt.ylabel(r'$Y\, [\mu m]$')
  plt.title('Potential map')
  cbar = plt.colorbar()
  cbar.set_label(r'$V_{bias}\, [V]$')
  plt.gca().invert_yaxis()
  plt.clim(V.min(),V.max())
  plt.savefig('razor.png')
  #cset = plt.contour(grid,np.arange(-1000,0,-100),linewidths=2,cmap=plt.cm.Set2)
  triang = tri.Triangulation(X, Y)
  plt.tricontour(triang, V, colors='k')
  plt.tricontourf(X,Y,V, 20)
  plt.savefig('razor2.png')
  
  # now show the number of points in each bin.  since the independent data are
  # Gaussian distributed, we expect a 2D Gaussian.
  #plt.subplot(1, 2, 2)
  #plt.imshow(bins, extent=extent, cmap=palette, origin='lower', vmin=0, vmax=bins.max(), aspect='auto', interpolation='bilinear')
  #plt.xlabel('X values')
  #plt.ylabel('Y values')
  #plt.title('X, Y vs The No. of Pts Per Bin')
  #plt.colorbar()
  #plt.show()
  #plt.savefig('razor.png')
  
if (__name__ == "__main__") :
  if (len(sys.argv) < 2 or len(sys.argv) > 2 ):
    print "Usage:",sys.argv[0],"<filename>";
    exit(2)
  name = sys.argv[1]
  temperature_plot(name)

 
