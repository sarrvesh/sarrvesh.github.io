#!/usr/bin/env python
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 

# Create a Miller project 
map = Basemap(projection='hammer', lon_0=20, resolution='l')

# Plot coastlines
map.drawcoastlines(linewidth=0.)
map.fillcontinents(alpha=0.85)

# Parse telescopes.txt and plot the points on the map
for line in open('telescopes.txt', 'r').readlines():
   if line[0] == '#': continue
   lat = float( line.split()[1][:-1] )
   lon = float( line.split()[2] )
   xpt, ypt = map(lon, lat)
   map.plot([xpt],[ypt],'ro', markersize=0.75)

# 
plt.savefig('radiotelescopes.png', dpi=500, bbox_inches='tight')
