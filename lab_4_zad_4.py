import numpy as np

def funct(a, b, N):
    x = np.arange(a, b, N) 
    y = x**2
    return y
a = funct(0, 2, 0.1)
print(a)


