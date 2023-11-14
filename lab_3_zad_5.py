import numpy as np
import lab_3_zad_4 as lab
st1 = int(input("1 столбец"))
st2 = int(input("2 столбец"))
for i in range(lab.NxM):
    lab.NxM[i,st1], lab.NxM[i, st2] = lab.NxM[i , st2], lab.NxM[i, st1]
print(lab.NxM[i])

