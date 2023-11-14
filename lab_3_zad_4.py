import numpy as np
N = 2
M = 3
NxM  = np.zeros((2, 3))
for i in range (N):
    for j in range(M):
        NxM[i, j] = np.sin(N * i + M * j)
for i in range(N):
    for j in range(M):
        if NxM[i, j]<0:
            NxM[i, j] = 0 
print(NxM[i, j])
