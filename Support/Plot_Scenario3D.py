"""
Plot_Scenario3D.py must be ran after intial run of Wx_Simulation
file ingest: Collections3D.csv, Target_deck3D.csv

"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import pandas as pd
import os
# import cartopy.crs as ccrs

ROOT = os.getcwd()
filePath = os.path.abspath(os.path.join(ROOT, "..\\.."))

actor_location = pd.read_csv(os.path.join(filePath, "Desktop\\Collections3D.csv"))
tgt_location = pd.read_csv(os.path.join(filePath, "Desktop\\Target_deck3D.csv"))

totalActorsCaught = len(actor_location.iloc[:, 0].drop_duplicates())
totalTargets = len(tgt_location.iloc[:, 0].drop_duplicates())

# tgt_location['height'] = tgt_location['top'] - tgt_location['bottom']
# tgt_location['width'] = tgt_location['right'] - tgt_location['left']
# tgt_location = pd.DataFrame(tgt_location)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax = Axes3D(fig)


# proj_ax = plt.figure().add_axes([0, 0, 1, 1], projection=ccrs.Robinson())
# cs = proj_ax.contourf(X, Y, Z, transform=ccrs.PlateCarree(), alpha=1)

# ax.projection = proj_ax.projection

# fig, ax = plt.subplots()
# current_axes = plt.gca()
# ax.plot_surface()

for index, target in tgt_location.iterrows():

    # Each vert is a different face of each polygon
    vert1 = [[target['xMin'], target['yMin'], target['zMin']],
             [target['xMin'], target['yMin'], target['zMax']],
             [target['xMin'], target['yMax'], target['zMax']],
             [target['xMin'], target['yMax'], target['zMin']]]

    vert2 = [[target['xMax'], target['yMin'], target['zMin']],
             [target['xMax'], target['yMin'], target['zMax']],
             [target['xMax'], target['yMax'], target['zMax']],
             [target['xMax'], target['yMax'], target['zMin']]]

    vert3 = [[target['xMin'], target['yMin'], target['zMin']],
             [target['xMin'], target['yMin'], target['zMax']],
             [target['xMax'], target['yMin'], target['zMax']],
             [target['xMax'], target['yMin'], target['zMin']]]

    vert4 = [[target['xMin'], target['yMax'], target['zMin']],
             [target['xMin'], target['yMax'], target['zMax']],
             [target['xMax'], target['yMax'], target['zMax']],
             [target['xMax'], target['yMax'], target['zMin']]]

    vert5 = [[target['xMin'], target['yMin'], target['zMin']],
             [target['xMin'], target['yMax'], target['zMin']],
             [target['xMax'], target['yMax'], target['zMin']],
             [target['xMax'], target['yMin'], target['zMin']]]

    vert6 = [[target['xMin'], target['yMin'], target['zMax']],
             [target['xMin'], target['yMax'], target['zMax']],
             [target['xMax'], target['yMax'], target['zMax']],
             [target['xMax'], target['yMin'], target['zMax']]]

    verts = [vert1, vert2, vert3, vert4, vert5, vert6]

    ax.add_collection3d(Poly3DCollection(verts, linewidth=1, edgecolor='r', facecolors='cyan',
                                         alpha=0.25))


ax.scatter(actor_location['xMin'], actor_location['yMin'], actor_location['zMin'], s=1,
           color='black')
ax.invert_xaxis()

# The limit of the plot is the region in question
ax.set(xlim=(55, 125), ylim=(15, 80), zlim=(0, 60000))

plt.title('Target Deck with Caught Actors')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
ax.set_zlabel('Altitude (ft)')
plt.annotate("%s Targets Caught \n%s Targets in deck" % (totalActorsCaught, totalTargets),
             xy=(0.8, 1.01), xycoords='axes fraction', fontsize=10)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
