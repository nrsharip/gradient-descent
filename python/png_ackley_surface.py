# https://matplotlib.org/3.1.0/gallery/mplot3d/surface3d.html

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import math

# https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
fig = plt.figure(figsize=(15, 10))
ax = fig.gca(projection='3d')

# https://stackoverflow.com/questions/20228546/how-do-i-apply-some-function-to-a-python-meshgrid
@np.vectorize
def ackley_function(x1,x2):
  # https://github.com/adhishagc/Ackley-Function/blob/master/build/lib/ackleyf/ackley-function.py
  #returns the point value of the given coordinate
  part_1 = -0.2*math.sqrt(0.5*(x1*x1 + x2*x2))
  part_2 = 0.5*(math.cos(2*math.pi*x1) + math.cos(2*math.pi*x2))
  value = math.exp(1) + 20 -20*math.exp(part_1) - math.exp(part_2)
  #returning the value
  return value

# Make data.
x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
X, Y = np.meshgrid(x, y)

Z = ackley_function(X,Y)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, rstride=10, cstride=10, edgecolors='k')

ax.view_init(30, 60)

plt.savefig('images/function-ackley-surface.png')