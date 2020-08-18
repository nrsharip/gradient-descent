# https://stackoverflow.com/questions/31499689/adding-extra-contour-lines-using-matplotlib-2d-contour-plotting

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# https://stackoverflow.com/questions/20228546/how-do-i-apply-some-function-to-a-python-meshgrid
@np.vectorize
# https://pythonhosted.org/algopy/examples/minimization/himmelblau_minimization.html
def himmelblau_function(x,y):
    a = x*x + y - 11
    b = x + y*y - 7
    return a*a + b*b

delta = 0.01
x = np.arange(-6.0, 6.0, delta)
y = np.arange(-6.0, 6.0, delta)

# https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
X, Y = np.meshgrid(x, y)

Z = himmelblau_function(X,Y)

# https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
plt.figure(figsize=(15, 15))
levels = np.arange(0.0, 500.0, 25)
CS = plt.contour(X, Y, Z, levels=levels)
plt.clabel(CS, inline=1, fontsize=10)
plt.savefig('images/function-himmelblau-contour.png')