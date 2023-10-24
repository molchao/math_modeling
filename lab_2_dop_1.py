import math
a = int(input("Введите 1 коэффициент: "))
b = int(input("Введите 2 коэффициент: "))
c = int(input("Введите свободный член: "))
D = b^2-4*a*c
if  D>0:
    
    x1 = (-b +sqrt D)/2*a
    x2 = (-b -sqrt D)/2*a
    print("2 корня", x1, x2)
if  D<0:
    print("Корней нет")
if D==0:
    x1=-b/2*a
    print(x1)
    