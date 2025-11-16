num = int(input("Введите целое неотрцательное число \n"))
a = 0
b = 1
if a == 0:
    print('Число Фибоначчи = 1')
elif a == 1:
    print('Число Фибоначчи = 2')
else:
    num = (num-1)+(num-2)
    print(num)
