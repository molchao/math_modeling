import numpy as np

def ploshad_kruga(fig, a, r, h, b):
    if a == "круг":       
        S = np.pi *(r**2)
    elif a == "прямоугольник":
        S = a*b
    elif a == "треугольник":
        S = 0.5*a*h
        
        