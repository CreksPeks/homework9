# Урок № 9

# Задание № 1


n = int(input("колличество чисел: "))      # 1 <= n <= 100000
a = []
if 1 <= n <= 100000:
    a = list(map(int, input("Введи числа через пробел: ").split()))
    for i in a:
        if (len(a) > n) or (len(a) > 2*10e9):
            a.pop()
b = set(a)
print(len(b))



# Задание # 2



a = list(map(int, input("первый список чисел, через пробел: ").split()))
b = list(map(int, input("второй список чисел, через пробел: ").split()))
if (len(a)) or (len(b)) <= 1000:
    a = set(a)
    b = set(b)
print(len(a.intersection(b)))


# Задание № 3


a = list(map(int, input("Введи числа: ").split()))   # вводим числа
b = set()                                            # сюда будем заносить число после проветки
for i in a:                                          # тут перебираем список что бы вытощить наши числа
    if i in b:                                       # тут ищем наши числа во множестве
        print(i, "Yes")                              # пока b пустое проскочим мимо, ,будут совпадения задержусь
    else:                                            # так как нет i в b то дальше пошли
        print(i, "No")                               # печатаем, что нету такого
        b.add(i)                                     # добавляем 
