import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# https://stackoverflow.com/questions/20228546/how-do-i-apply-some-function-to-a-python-meshgrid
@np.vectorize
# https://github.com/adhishagc/Ackley-Function
def ackley_function(x,y):
  #returns the point value of the given coordinate
  part_1 = -0.2*math.sqrt(0.5*(x*x + y*y))
  part_2 = 0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))
  value = math.exp(1) + 20 - 20 * math.exp(part_1) - math.exp(part_2)
  #returning the value
  return value

def derivative_x(x,y):
    part_1 = 2.82842712474619 * x * math.exp(-0.14142135623731 * math.sqrt(x*x + y*y))/(math.sqrt(x*x + y*y))
    part_2 = math.pi * math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) * math.sin(2*math.pi*x)
    return part_1 + part_2

def derivative_y(x,y):
    part_1 = 2.82842712474619 * y * math.exp(-0.14142135623731 * math.sqrt(x*x + y*y))/(math.sqrt(x*x + y*y))
    part_2 = math.pi * math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) * math.sin(2*math.pi*y)
    return part_1 + part_2

delta = 0.01
x = np.arange(-5.0, 5.0, delta)
y = np.arange(-5.0, 5.0, delta)
# https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
X, Y = np.meshgrid(x, y)
Z = ackley_function(X,Y)

# https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
fig, ax = plt.subplots(figsize=[10, 10])
levels = np.arange(0.0, 15.0, 1)
CS = plt.contour(X, Y, Z, levels=levels)
plt.clabel(CS, inline=1, fontsize=10)

A = [-1, -0.5]
B = [0.2, -1.7]
C = [4.2, 0.4]
D = [-3.5, -0.6]
E = [-2.6, 2.3]

ax.plot(A[0], A[1], 'bo')
ax.plot(B[0], B[1], 'ro')
ax.plot(C[0], C[1], 'co')
ax.plot(D[0], D[1], 'mo')
ax.plot(E[0], E[1], 'ko')

# https://www.kite.com/python/answers/how-to-label-a-single-point-in-a-matplotlib-graph-in-python
ax.annotate("Point A", (A[0], A[1]))
ax.annotate("Point B", (B[0], B[1]))
ax.annotate("Point C", (C[0], C[1]))
ax.annotate("Point D", (D[0], D[1]))
ax.annotate("Point E", (E[0], E[1]))

a_history = [[],[]]
b_history = [[],[]]
c_history = [[],[]]
d_history = [[],[]]
e_history = [[],[]]

#learning_rate = 0.05
#epochs = 300

learning_rate = 0.05
epochs = 150
gamma = 0.75

# a running average of the magnitudes of recent gradients
grad_ra_A = [0,0]
grad_ra_B = [0,0]
grad_ra_C = [0,0]
grad_ra_D = [0,0]
grad_ra_E = [0,0]

for iter in range(epochs):
    #ax.plot(A[0], A[1], 'bo')
    #ax.plot(B[0], B[1], 'ro')
    #ax.plot(C[0], C[1], 'co')
    #ax.plot(D[0], D[1], 'mo')
    #ax.plot(E[0], E[1], 'ko')
    
    a_history[0].append(A[0]); a_history[1].append(A[1])
    b_history[0].append(B[0]); b_history[1].append(B[1])
    c_history[0].append(C[0]); c_history[1].append(C[1])
    d_history[0].append(D[0]); d_history[1].append(D[1])
    e_history[0].append(E[0]); e_history[1].append(E[1])
    
    grad_ra_A[0] = gamma * grad_ra_A[0] + (1 - gamma) * (derivative_x(A[0], A[1]))**2
    grad_ra_A[1] = gamma * grad_ra_A[1] + (1 - gamma) * (derivative_y(A[0], A[1]))**2
    
    A[0] = A[0] - learning_rate * (1/grad_ra_A[0]) * derivative_x(A[0], A[1])
    A[1] = A[1] - learning_rate * (1/grad_ra_A[1]) * derivative_y(A[0], A[1])
    
    grad_ra_B[0] = gamma * grad_ra_B[0] + (1 - gamma) * (derivative_x(B[0], B[1]))**2
    grad_ra_B[1] = gamma * grad_ra_B[1] + (1 - gamma) * (derivative_y(B[0], B[1]))**2
    
    B[0] = B[0] - learning_rate * (1/grad_ra_B[0]) * derivative_x(B[0], B[1])
    B[1] = B[1] - learning_rate * (1/grad_ra_B[1]) * derivative_y(B[0], B[1])
    
    grad_ra_C[0] = gamma * grad_ra_C[0] + (1 - gamma) * (derivative_x(C[0], C[1]))**2
    grad_ra_C[1] = gamma * grad_ra_C[1] + (1 - gamma) * (derivative_y(C[0], C[1]))**2
    
    C[0] = C[0] - learning_rate * (1/grad_ra_C[0]) * derivative_x(C[0], C[1])
    C[1] = C[1] - learning_rate * (1/grad_ra_C[1]) * derivative_y(C[0], C[1])
    
    grad_ra_D[0] = gamma * grad_ra_D[0] + (1 - gamma) * (derivative_x(D[0], D[1]))**2
    grad_ra_D[1] = gamma * grad_ra_D[1] + (1 - gamma) * (derivative_y(D[0], D[1]))**2
    
    D[0] = D[0] - learning_rate * (1/grad_ra_D[0]) * derivative_x(D[0], D[1])
    D[1] = D[1] - learning_rate * (1/grad_ra_D[1]) * derivative_y(D[0], D[1])
    
    grad_ra_E[0] = gamma * grad_ra_E[0] + (1 - gamma) * (derivative_x(E[0], E[1]))**2
    grad_ra_E[1] = gamma * grad_ra_E[1] + (1 - gamma) * (derivative_y(E[0], E[1]))**2
    
    E[0] = E[0] - learning_rate * (1/grad_ra_E[0]) * derivative_x(E[0], E[1])
    E[1] = E[1] - learning_rate * (1/grad_ra_E[1]) * derivative_y(E[0], E[1])

div = 10
#for i in range(0, epochs//10):
def animate(i):
    # https://stackoverflow.com/questions/509211/understanding-slice-notation
    ax.plot(a_history[0][i*div:(i+1)*div + 1], a_history[1][i*div:(i+1)*div + 1], color='blue', linewidth=4)
    ax.plot(b_history[0][i*div:(i+1)*div + 1], b_history[1][i*div:(i+1)*div + 1], color='red', linewidth=4)
    ax.plot(c_history[0][i*div:(i+1)*div + 1], c_history[1][i*div:(i+1)*div + 1], color='cyan', linewidth=4)
    ax.plot(d_history[0][i*div:(i+1)*div + 1], d_history[1][i*div:(i+1)*div + 1], color='magenta', linewidth=4)
    ax.plot(e_history[0][i*div:(i+1)*div + 1], e_history[1][i*div:(i+1)*div + 1], color='black', linewidth=4)

# https://eli.thegreenplace.net/2016/drawing-animated-gifs-with-matplotlib/
anim = FuncAnimation(fig, animate, frames=np.arange(0, epochs//div), interval=200)
    
anim.save('images/rmsprop-ackley-gamma-075.gif', dpi=80)