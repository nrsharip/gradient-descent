import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# https://stackoverflow.com/questions/20228546/how-do-i-apply-some-function-to-a-python-meshgrid
@np.vectorize
# https://pythonhosted.org/algopy/examples/minimization/himmelblau_minimization.html
def himmelblau_function(x,y):
    a = x*x + y - 11
    b = x + y*y - 7
    return a*a + b*b

def der_x(x,y):
    a = x*x + y - 11
    b = x + y*y - 7
    return 4 * x * a + 2 * b

def der_y(x,y):
    a = x*x + y - 11
    b = x + y*y - 7
    return 2 * a + 4 * y * b

delta = 0.01
x = np.arange(-6.0, 6.0, delta)
y = np.arange(-6.0, 6.0, delta)

# https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
X, Y = np.meshgrid(x, y)
Z = himmelblau_function(X,Y)

# https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
fig, ax = plt.subplots(figsize=[10, 10])
levels = np.arange(0.0, 500.0, 25)
CS = plt.contour(X, Y, Z, levels=levels)
plt.clabel(CS, inline=1, fontsize=10)

A = [0, -4]
B = [0, -1]
C = [4.5, 1]
D = [-5, 0]
E = [-4, 5]

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

# learning_rate = 0.005
# epochs = 100

learning_rate = 0.001
epochs = 150

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
    
    A[0] = A[0] - learning_rate * der_x(A[0], A[1])
    A[1] = A[1] - learning_rate * der_y(A[0], A[1])
    
    B[0] = B[0] - learning_rate * der_x(B[0], B[1])
    B[1] = B[1] - learning_rate * der_y(B[0], B[1])
    
    C[0] = C[0] - learning_rate * der_x(C[0], C[1])
    C[1] = C[1] - learning_rate * der_y(C[0], C[1])
    
    D[0] = D[0] - learning_rate * der_x(D[0], D[1])
    D[1] = D[1] - learning_rate * der_y(D[0], D[1])
    
    E[0] = E[0] - learning_rate * der_x(E[0], E[1])
    E[1] = E[1] - learning_rate * der_y(E[0], E[1])


div = 5
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
anim.save('images/grad-himmelblau.gif', dpi=80)