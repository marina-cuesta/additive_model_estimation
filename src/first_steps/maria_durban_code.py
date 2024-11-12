import numpy as np
import pandas as pd
import os
import random
from matplotlib import pyplot as plt
from scipy.interpolate import BSpline



#########################################
##### Univariate case without alpha #####
#########################################

## set seed
np.random.seed(123)

## number of samples
n = 1000

## param for error term (epsilon)
sigma = 0.2

## Data generation
# x data
x1 = np.random.uniform(-1, 1, n)
x1 = x1 - np.mean(x1)
x1 = np.sort(x1)
# y data
f1 = np.cos(2 * np.pi * np.sqrt((x1-0.5)**2))
f1 = f1 - np.mean(f1)
epsilon=np.random.normal(0, sigma, n)
y = f1 + epsilon

# Graficamos la función original
plt.plot(x1, f1, lw=2, label='Función original (f1)', color='blue')
plt.show()

## Function to compute the splines basis
 # x is the sequence of values
 # xl is the left x bound for the splines basis
 # xr is the right x bound for the splines basis
 # ndx is the number of internal knots
 # bdeg is the degree of the basis

def my_bbase(x, xl=np.min(x), xr=np.max(x), ndx=10, bdeg=3):

    # increment in x (steps) to obtain the knots
    dx = (xr - xl) / ndx
    # compute knots (internal and external)
    knots=  np.arange(start=xl - bdeg * dx, stop= xr + bdeg * dx + dx, step=dx)
    B = np.zeros((len(x), len(knots) - bdeg - 1))

    B=BSpline.basis_element(knots)
