import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import pandas as pd
import os

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

# fig, ax = plt.subplots()
# current_axes = plt.gca()

for index, target in tgt_location.iterrows():
    # ax.plot_wireframe([target['xMin'], target['xMax']], [target['yMin'], target['yMax']],
    #                   [target['zMin'], target['zMax']], c='r')

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

    # x = [target['xMin'], target['xMax'], target['xMax'], target['xMin']]
    # y = [target['yMin'], target['yMin'], target['yMax'], target['yMax']]
    # z = [target['zMin'], target['zMax'], target['zMin'], target['zMax']]

    # verts = [list(zip(x, y, z))]

    ax.add_collection3d(Poly3DCollection(verts, linewidth=1, edgecolor='r', facecolors='cyan', alpha=0.25))
    # rect = patches.Rectangle((int(target['left']), int(target['bottom'])), int(target['width']),
    #                          int(target['height']), linewidth=1, edgecolor='r', facecolor='none')
    # current_axes.add_patch(rect)

ax.scatter(actor_location['xMin'], actor_location['yMin'], actor_location['zMin'], s=1, color='black')
plt.title('Target Deck with Caught Actors')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.annotate("%s Targets Caught \n%s Targets in deck" % (totalActorsCaught, totalTargets), xy=(0.8, 1.01),
             xycoords='axes fraction', fontsize=10)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
