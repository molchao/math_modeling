import numpy as np

def lala(umnozhoit):
    s = 1
    for i in range(len(umnozhoit)):
        s = s*umnozhoit[i]
    return s
test_1 = np.arange(3, 10, 1)
lala(test_1)
print(lala(test_1))
