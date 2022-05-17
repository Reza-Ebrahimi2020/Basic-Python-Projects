# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:13:47 2022

@author: Reza
"""

import numpy as np
import matplotlib.pyplot as plt
#Data for a three dimentional line
ax = plt.axes(projection='3d')
z = np.linspace(0,15,1000)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x,y,z,'red')
#Data for three dimentional scattered points
z = 15 * np.random.random(100)
x = np.sin(z)+ 0.1* np.random.randn(100)
y = np.cos(z)+ 0.1* np.random.randn(100)
ax.scatter3D(x,y,z,c=z,cmap='Greens')
plt.show()