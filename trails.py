from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0, 10, 25)
y = x * x + 2
print(x)
print(y)
print(np.array([x,y]).reshape(25,2))
pyplot.plt(x,y, 'r') #'r stands for red 
      