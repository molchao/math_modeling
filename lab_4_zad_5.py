import numpy as np

def ploshad_kruga(fig, a, r, h, b):
    if fig == "круг":       
        S = np.pi *(r**2)
    elif fig == "прямоугольник":
        S = a*b
    elif fig == "треугольник":
        S = 0.5*a*h
    return S
f = ploshad_kruga("круг", 6, 5, 4, 3)
print(f)
        