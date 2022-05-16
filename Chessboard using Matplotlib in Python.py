# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:10:33 2022

@author: Reza
"""

import matplotlib.pyplot as plt
import numpy as np
dx, dy =0.015,0.05
x = np.arange(-4.0,4.0,dx)
y = np.arange(-4.0,4.0,dy)
x,y = np.meshgrid(x,y)
extent = np.min(x),np.max(x), np.min(y),np.max(y)
z1 = np.add.outer(range(8), range(8))%2
plt.imshow(z1, cmap="binary_r",interpolation="nearest",extent = extent)
plt.title("chess Board with Python")
plt.show()

