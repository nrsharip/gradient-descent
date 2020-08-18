# https://stackoverflow.com/questions/31499689/adding-extra-contour-lines-using-matplotlib-2d-contour-plotting

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

# https://stackoverflow.com/questions/20228546/how-do-i-apply-some-function-to-a-python-meshgrid
@np.vectorize
# https://github.com/adhishagc/Ackley-Function
def ackley_function(x1,x2):
  #returns the point value of the given coordinate
  part_1 = -0.2*math.sqrt(0.5*(x1*x1 + x2*x2))
  part_2 = 0.5*(math.cos(2*math.pi*x1) + math.cos(2*math.pi*x2))
  value = math.exp(1) + 20 - 20 * math.exp(part_1) - math.exp(part_2)
  #returning the value
  return value

delta = 0.025
x = np.arange(-5.0, 5.0, delta)
y = np.arange(-5.0, 5.0, delta)

# https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
X, Y = np.meshgrid(x, y)

Z = ackley_function(X,Y)

# https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
plt.figure(figsize=(15, 15))
levels = np.arange(0.0,15.0,1)
CS = plt.contour(X, Y, Z, levels=levels)
plt.clabel(CS, inline=1, fontsize=10)
plt.savefig('images/function-ackley-contour.png')