num = int(input("Введите целое неотрцательное число \n"))
if num == 0:
    print(f'У числа {num} индекс 0')
elif num == 1:
    print(f'У числа {num} индекс 1')
else:
    a = 0
    b = 1
    index = 1
    while index < num:
        c = a + b
        a = b
        b = c
        index = index + 1
    if b == num:
            print(f'У числа {num} индекс {index + 1}')
    else:
            print(f'{num} не число Фибоначчи')
    