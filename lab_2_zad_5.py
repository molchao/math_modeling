a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
if a%b == 0:
    print("1 число делится на второе")
    print(a/b)
else:
    print("1 число не делится на второе")
    print(a%b)
    print(a/b)