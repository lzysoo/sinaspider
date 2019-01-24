# -*- encoding:utf-8 -*-

from scipy import poly1d
import numpy as np
import matplotlib.pyplot as plt

'''
p = poly1d([3,4,5])
print(p)
print(p*p)
'''

x = np.linspace(0,10,1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label = "$sin(x)$",color = "red",linewidth = 2)
plt.plot(x,z,"b--",label = "$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("pp first Ex")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()
