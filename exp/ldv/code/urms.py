#!/bin/py
#
# open file
# read contents
# (re)start when third column found
#
import sys
import numpy as np

#
# open and read file
#
path = "urms_5.txt"
file = open(path, "r+")
defect1 = []
for line in file:
    defect1.append(float(line))

path = "urms_10.txt"
file = open(path, "r+")
defect2 = []
for line in file:
    defect2.append(float(line))

path = "urms_yd5.txt"
file = open(path, "r+")
yd1 = []
for line in file:
    yd1.append(float(line))
    
path = "urms_yd10.txt"
file = open(path, "r+")
yd2 = []
for line in file:
    yd2.append(float(line))
    
#
# plot
#
import matplotlib.pyplot as plt
plt.subplot(1, 1, 1)
plt.plot(yd1,defect1,color='black',marker='o',label=r'$y/d=5$')
plt.plot(yd2,defect2,color='blue', marker='v',label=r'$y/d=10$')
plt.title('LDV URMS')
plt.ylabel(r'$U_{RMS}/U_{\infty}$')
plt.xlabel('y/d')
plt.legend(loc='best')
plt.savefig('urms.png')
plt.close()

#
# steady as she goes
#
sys.exit(0)
