import numpy as np
import matplotlib.pyplot as plt
def f(x,a,b,c):
    return a*x**2+b*x+c

xlist = np.linspace(-10,10,num=1000)
#xlist = np.arrange(-10,10.1,.1)

ylist = f(xlist,3,1,4)

plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist)
plt.show()
