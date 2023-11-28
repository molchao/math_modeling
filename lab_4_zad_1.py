import numpy as np

def plus(sklad):
    s = 0
    for i in range(len(sklad)):
        s = s+sklad[i]
    return s/len(sklad)
 
test_1 = np.arange(0, 100, 1)
plus(test_1)
print(plus(test_1))