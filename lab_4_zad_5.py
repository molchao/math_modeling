import numpy as np

a = input("Введите фигуру: ")
if a == "круг":
    r = int(input("Введите радиус"))
    def ploshad_kruga(r):
        S = np.pi * r^2
        print(S)
    ploshad_kruga(r)