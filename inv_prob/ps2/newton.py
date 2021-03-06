#!/bin/py
# From calculation, we expect that the local minimum occurs at (x,y) = (0,0)
#
# min f(x,y) = -cos(x)cos(y/10)
#
import numpy as np
import matplotlib.pylab as plt

x_old  = np.array([0, 0])
eps    = 0.01               # step size
thresh = 0.00001

x_guess = np.pi/4.
y_guess = -np.pi
x_new  = np.array([x_guess, y_guess])
 
def f_prime(xv):    
    """ Gradient f = [sin(x)cos(y/10), cos(x) sin(y/10)/10 ]"""
    x = xv[0]
    y = xv[1]
    return np.array([np.sin(x)*np.cos(y/10.), np.cos(x)*np.sin(y/10.)/10.])

def f_hess(xv):    
    """ Hessian f"""
    x = xv[0]
    y = xv[1]
    return np.matrix([[ np.cos(x)*np.cos(y/10.)    , -np.sin(x)*np.sin(y/10.)/10. ],
                     [ -np.sin(x)*np.sin(y/10.)/10.,  np.cos(x)*np.cos(y/10.)/100.]])

xdat = []
ydat = []
while np.linalg.norm(x_new-x_old) > thresh:
    x_old = x_new
    #xdat.append(x_new[0])
    #ydat.append(x_new[1])
    a = f_hess(x_old)
    print a
    inv_hess = np.linalg.inv(a)
    print inv_hess
    # line search
    #eps = 

    x_new = x_old - eps * np.dot(inv_hess,f_prime(x_old))
print "Local minimum occurs at ", x_new

# plot movement
#
# plt.plot(xdat,ydat)
# plt.xlabel('time (s)')
# plt.ylabel('voltage (mV)')
# plt.title('About as simple as it gets, folks')
# plt.grid(True)
# plt.savefig("test.png")
# plt.show()


#
# nick 
# 3/1/14
#
