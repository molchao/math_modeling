a = int(input("Введите длинну 1 отрезка"))
b = int(input("Введите длинну 2 отрезка"))
c = int(input("Введите длинну 3 отрезка"))
if a>=b+c and b>=a+c and c>=b+a:
    print("Треугольника нет")
elif a==b==c:
    print("Треугольник равносторонний")
elif a!=b!=c:
    print("Треугольник разностороний")   
elif a==b or b==c or c==a or a==c:
    print("Треугольник равнобедренный") 
