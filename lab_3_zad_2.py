import numpy as np
from lab_3_zad_1 import g
h = 100
a = np.pi/ 3
b = 30
T = 200
e = 300



v1 = (g*h*(np.tan(b)**2))/(2*(np.cos(a)**2)*(1-np.tan(b)*np.tan(a)))
v = np.sqrt(v1)
print(v)
