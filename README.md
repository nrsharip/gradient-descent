## Overview
The intention of this project is to review and implement the existing Gradient Descent optimization algorithms.

## Test Functions

<table>
  <tr>
    <td><img src="/python/images/function-ackley-surface.png?raw=true" width="100%"></td>
    <td><img src="/python/images/function-f1-surface.png?raw=true" width="100%"></td>
    <td><img src="/python/images/function-himmelblau-surface.png?raw=true" width="100%"></td>
  </tr>
  <tr>
    <td><img src="/python/images/function-ackley-contour.png?raw=true" width="100%"></td>
    <td><img src="/python/images/function-f1-contour.png?raw=true" width="100%"></td>
    <td><img src="/python/images/function-himmelblau-contour.png?raw=true" width="100%"></td>
  </tr>
  <tr>
    <td><img src="/python/images/function-ackley.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/function-f1.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/function-himmelblau.gif?raw=true" width="100%"></td>
  </tr>
</table>

## Gradient Descent

<table>
  <tr>
    <td><img src="/python/images/grad-ackley.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/grad-f1.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/grad-himmelblau.gif?raw=true" width="100%"></td>
  </tr>
</table>

## Nesterov Accelerated Gradient

<table>
  <tr>
    <td align="center" colspan = 3><img src="https://latex.codecogs.com/svg.latex?\gamma=0.995" title="\gamma=0.995"/></td>
  </tr>
  <tr>
    <td><img src="/python/images/nag-ackley-gamma-995.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/nag-f1-gamma-995.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/nag-himmelblau-gamma-995.gif?raw=true" width="100%"></td>
  </tr>
  <tr>
    <td align="center" colspan = 3><img src="https://latex.codecogs.com/svg.latex?\gamma=0.997" title="\gamma=0.997"/></td>
  </tr>
  <tr>
    <td><img src="/python/images/nag-ackley-gamma-997.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/nag-f1-gamma-997.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/nag-himmelblau-gamma-997.gif?raw=true" width="100%"></td>
  </tr>
  <tr>
    <td align="center" colspan = 3><img src="https://latex.codecogs.com/svg.latex?\gamma=0.999" title="\gamma=0.999"/></td>
  </tr>
  <tr>
    <td><img src="/python/images/nag-ackley-gamma-999.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/nag-f1-gamma-999.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/nag-himmelblau-gamma-999.gif?raw=true" width="100%"></td>
  </tr>
</table>

## AdaGrad — Adaptive Gradient

[wiki](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad)

<table>
  <tr>
    <td><img src="/python/images/adagrad-ackley.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/adagrad-f1.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/adagrad-himmelblau.gif?raw=true" width="100%"></td>
  </tr>
</table>

## RMSProp - Root Mean Square Propagation

<table>
  <tr>
    <td align="center" colspan = 3><img src="https://latex.codecogs.com/svg.latex?\gamma=0.75" title="\gamma=0.995"/></td>
  </tr>
  <tr>
    <td><img src="/python/images/rmsprop-ackley-gamma-075.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/rmsprop-f1-gamma-075.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/rmsprop-himmelblau-gamma-075.gif?raw=true" width="100%"></td>
  </tr>
  <tr>
    <td align="center" colspan = 3><img src="https://latex.codecogs.com/svg.latex?\gamma=0.80" title="\gamma=0.995"/></td>
  </tr>
  <tr>
    <td><img src="/python/images/rmsprop-ackley-gamma-080.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/rmsprop-f1-gamma-080.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/rmsprop-himmelblau-gamma-080.gif?raw=true" width="100%"></td>
  </tr>
  <tr>
    <td align="center" colspan = 3><img src="https://latex.codecogs.com/svg.latex?\gamma=0.85" title="\gamma=0.995"/></td>
  </tr>
  <tr>
    <td><img src="/python/images/rmsprop-ackley-gamma-085.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/rmsprop-f1-gamma-085.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/rmsprop-himmelblau-gamma-085.gif?raw=true" width="100%"></td>
  </tr>
</table>
