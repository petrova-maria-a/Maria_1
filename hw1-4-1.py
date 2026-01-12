num = int(input("Введите целое неотрицательное число \n"))
a = 0
b = 1
count = 0

if num < 0:
    print("Номер должен быть неотрицательным числом")
elif num == 0:
    print(f"Число Фибоначчи под номером {num} равно {a}")
elif num == 1:
    print(f"Число Фибоначчи под номером {num} равно {b}")
else:
    while count < num:
        c = a + b
        a = b
        b = c
        count += 1
    print(f"Число Фибоначчи под номером {num} равно {a}")