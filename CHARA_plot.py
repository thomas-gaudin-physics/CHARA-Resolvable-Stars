#Created on Fri Feb 19 21:42:08 2021

#@author: Thomas Gaudin
import matplotlib.pyplot as plt
import numpy as np

def alpha_function(alpha):
    ang = alpha / 206625
    return ang

alph_max = alpha_function(0.01)
alph_min = alpha_function(0.0005)

def diameter(dist, angle):
    RS = 2.254610e-8
    d = (dist / angle) * RS
    return d

diam = np.vectorize(diameter)
D = np.linspace(0.0, 4000.0, 10000)

plt.plot(D, diam(D, alph_max), 'm')
plt.plot(D, diam(D, alph_min), 'g')
plt.hlines(y=1700, xmin=0, xmax=4000)
plt.ylim((0.0,2000.0))
plt.legend(['CHARA Max Resolution', 'CHARA Min Resolution','Max Stellar Diameter'], loc='lower right')
plt.title('Diameters Resolvable by CHARA as a Function of Distance')
plt.xlabel('Distance (parsec)')
plt.ylabel('Diameter (Solar Radii)')
plt.show()
