# https://matplotlib.org/3.1.0/gallery/mplot3d/surface3d.html

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import math

# https://pythonhosted.org/algopy/examples/minimization/himmelblau_minimization.html
@np.vectorize
# https://en.wikipedia.org/wiki/Gradient_descent#Examples
def grad_descent_function(x,y):
    a = 0.5*x*x - 0.25*y*y + 3
    b = 2*x + 1 - math.exp(y)

    return math.sin(a)*math.cos(b)

# https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
fig = plt.figure(figsize=(15, 10))
ax = fig.gca(projection='3d')

# Make data.
x = np.arange(-2, 2, 0.01)
y = np.arange(-2, 2, 0.01)
X, Y = np.meshgrid(x, y)

Z = grad_descent_function(X,Y)

# https://stackoverflow.com/questions/21418255/changing-the-line-color-in-plot-surface
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, rstride=5, cstride=5, edgecolors='k')

ax.view_init(40, 60)

plt.savefig('images/function-f1-surface.png')