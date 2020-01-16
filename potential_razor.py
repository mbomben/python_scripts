import numpy as np
import matplotlib.pyplot as plt
import griddata
from matplotlib.colors import LogNorm

X = []
Y = []
V = []
#for line in open('potential.dat'):
#for line in open('hConc.dat'):
for line in open('hConc_100ps.dat'):
  tmp = line.split()
  x = float(tmp[0])
  y = float(tmp[1])
  v = float(tmp[2])
  X.append(x)
  Y.append(y)
  V.append(v)

npr = np.random              # Tue Apr 12 08:43:15 CEST 2016 consider to remove
npts = len(X)                           # the total number of data points.
X = np.asarray(X)            # x data in array format
Y = np.asarray(Y)            # y data in array format
V = np.asarray(V)            # v data in array format

# plot some profiles / cross-sections for some visualization.  our
# function is a symmetric, upward opening paraboloid z = x**2 + y**2.
# We expect it to be symmetric about and and y, attain a minimum on
# the origin and display minor Gaussian noise.

plt.ion()   # pyplot interactive mode on

# x vs z cross-section.  notice the noise.
plt.plot(x, v, '.')
plt.title('X vs V=F(X,Y=constant)')
plt.xlabel('X')
plt.ylabel('V')

# y vs z cross-section.  notice the noise.
plt.plot(y, v, '.')
plt.title('Y vs V=F(Y,X=constant)')
plt.xlabel('Y')
plt.ylabel('V')

# now show the dependent data (x vs y).  we could represent the v data
# as a third axis by either a 3d plot or contour plot, but we need to
# grid it first....
plt.plot(x, y, '.')
plt.title('X vs Y')
plt.xlabel('X')
plt.ylabel('Y')

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
plt.imshow(grid, extent=extent, cmap=palette, origin='lower', vmin=vmin, vmax=vmax, aspect='auto', interpolation='bicubic', norm=LogNorm())
plt.xlabel(r'$X\, [\mu m]$')
plt.ylabel(r'$Y\, [\mu m]$')
#plt.title('Potential map')
plt.title('Hole concentration map')
cbar = plt.colorbar()
#cbar.set_label(r'$V_{bias}\, [V]$')
cbar.set_label(r'$Hole\,conc.\, [cm^{-3}]$')
plt.gca().invert_yaxis()
#plt.clim(-500,0)
plt.clim(1e1,1e20)
#plt.zscale('log')
#plt.savefig('razor.png')
plt.savefig('holeConc_100ps.png')

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
