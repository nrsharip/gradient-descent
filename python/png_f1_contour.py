# https://stackoverflow.com/questions/31499689/adding-extra-contour-lines-using-matplotlib-2d-contour-plotting

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

# https://stackoverflow.com/questions/20228546/how-do-i-apply-some-function-to-a-python-meshgrid
@np.vectorize
# https://en.wikipedia.org/wiki/Gradient_descent#Examples
def grad_descent_function(x,y):
    a = 0.5*x*x - 0.25*y*y + 3
    b = 2*x + 1 - math.exp(y)
    return math.sin(a)*math.cos(b)

delta = 0.01
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-3.0, 2.0, delta)

# https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
X, Y = np.meshgrid(x, y)

Z = grad_descent_function(X,Y)

# https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
plt.figure(figsize=(15, 15))
levels = np.arange(-1.0, 1.0, 0.1)
CS = plt.contour(X, Y, Z, levels=levels)
plt.clabel(CS, inline=1, fontsize=10)

plt.savefig('images/function-f1-contour.png')