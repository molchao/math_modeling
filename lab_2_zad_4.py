n = int(input("Введите количество: "))
a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: ")) 
i = 0  
while i < n: 
    print(a) 
    c = a + b 
    a = b 
    b = c 
    i += 1
