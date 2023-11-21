def my_func(a, b):
    x = 3*a-b
    return x

#tmp = my_func() #Ошибка, 0 аргументов передали функцию

def my_func(a=1, b=0):
    x = 3*a-b
    return x

print(my_func())
print(my_func(3, 4))
print(my_func(3))  #a=3
print(my_func(b=3))
print(my_func(b=3, a=9))

def my_func(a, b=0):  #только так
    x = 3*a-b
    return x

def my_funk(*args):
    x = 3*args[0]-args[1]
    return x
print(my_func(3,4))
print(my_func(3,4, 8))

def my_func(**kwrgs):
    x = 3*kwrgs["obj_1"] - kwrgs["obj_2"]
    return x
print(my_func(obj_1=3, obj_2=4))
print(my_func(obj_1=3, obj_2=4, obj_3=8))
