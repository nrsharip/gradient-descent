## Overview
The intention of this project is to review and implement the existing Gradient Descent optimization algorithms.

## Table of contents
1. [Test Functions](#test-functions)
2. [Gradient Descent](#gradient-descent)
3. [Nesterov Accelerated Gradient](#nesterov-accelerated-gradient)
4. [AdaGrad — Adaptive Gradient](#adagrad--adaptive-gradient)
5. [RMSProp - Root Mean Square Propagation](#rmsprop---root-mean-square-propagation)
6. [License](#license)

## Test Functions

The following are the functions that are used for testing the algorithms.

1. [Ackley function](https://en.wikipedia.org/wiki/Ackley_function)
2. Gradient descent [example from Wikipedia](https://en.wikipedia.org/wiki/Gradient_descent#Examples)
3. [Himmelblau function](https://en.wikipedia.org/wiki/Himmelblau%27s_function)

Below are 3D surface, contour and 3D animation plots of these functions respectively:

<table>
  <tr>
    <td align=center><a href="https://en.wikipedia.org/wiki/Ackley_function">Ackley function</a></td>
    <td align=center><a href="https://en.wikipedia.org/wiki/Gradient_descent#Examples">example from Wikipedia</a></td>
    <td align=center><a href="https://en.wikipedia.org/wiki/Himmelblau%27s_function">Himmelblau function</a></td>
  </tr>
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
    <td align="center" colspan = 3><img src="https://latex.codecogs.com/svg.latex?\gamma=0.90" title="\gamma=0.90"/></td>
  </tr>
  <tr>
    <td><img src="/python/images/rmsprop-ackley-gamma-090.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/rmsprop-f1-gamma-090.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/rmsprop-himmelblau-gamma-090.gif?raw=true" width="100%"></td>
  </tr>
  <tr>
    <td align="center" colspan = 3><img src="https://latex.codecogs.com/svg.latex?\gamma=0.95 " title="\gamma=0.95"/></td>
  </tr>
  <tr>
    <td><img src="/python/images/rmsprop-ackley-gamma-095.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/rmsprop-f1-gamma-095.gif?raw=true" width="100%"></td>
    <td><img src="/python/images/rmsprop-himmelblau-gamma-095.gif?raw=true" width="100%"></td>
  </tr>
</table>

## License

This project is available under the [MIT license](LICENSE) © Nail Sharipov
