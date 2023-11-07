import numpy as np
x0 = 0
vox = 1
voy = 2
g = 9.8
y0 = 0
t = np.arange(0 , 5, 0.1)
x = x0+v0x * t
y = y0+v0y*t - g*t**2/2

print(t)

coords  = np.zeros((len(t), 3))
for i in range(len(t)):
    coords[i, 0 ] = t[i]
    coords[i, 1 ] = x[i]
    coords[i, 2 ] = y[i]
print(cords)