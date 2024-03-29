# https://matplotlib.org/3.1.0/gallery/mplot3d/surface3d.html

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import math
from matplotlib.animation import FuncAnimation

# https://pythonhosted.org/algopy/examples/minimization/himmelblau_minimization.html
@np.vectorize
def himmelblau_function(x,y):
    a = x*x + y - 11
    b = x + y*y - 7
    return a*a + b*b


# https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
fig = plt.figure(figsize=(9, 6))
ax = fig.gca(projection='3d')

# Make data.
x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
X, Y = np.meshgrid(x, y)

#Z = ackley_function(X,Y)
Z = himmelblau_function(X,Y)

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, rstride=30, cstride=30, edgecolors='k')

# rotate the axes and update
# for angle in range(0, 360):

def update(angle):
    ax.view_init(40, angle)
    return ax
#    plt.draw()
#    plt.pause(.001)

# https://eli.thegreenplace.net/2016/drawing-animated-gifs-with-matplotlib/
anim = FuncAnimation(fig, update, frames=np.arange(0, 180, 2), interval=100)
anim.save('images/function-himmelblau.gif', dpi=80, writer='imagemagick')